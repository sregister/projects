/*
 * Created By : Scott Register ( scott )
 * File Name : prog2.c
 * Creation Date : Sat 07 Nov 2015 05:49:32 PM PST
 * Last Modified : Mon 16 Nov 2015 09:46:07 PM PST
 * Purpose :
 *
 */ 
#include <stdlib.h>
#include <stdio.h>
#include <openssl/ssl.h>
#include <openssl/conf.h>
#include <openssl/evp.h>
#include <openssl/err.h>
#include <string.h>


//This function was found reading the openssl docs and wiki page
int encrypt(unsigned char *plaintext, int plaintext_len, unsigned char *key,
		unsigned char *iv, unsigned char *ciphertext)
{
	EVP_CIPHER_CTX *ctx;
	int len;
	int ciphertext_len;

	ctx = EVP_CIPHER_CTX_new();

	EVP_EncryptInit_ex(ctx, EVP_aes_128_cbc(), NULL, key, NULL);

	EVP_EncryptUpdate(ctx, ciphertext, &len, plaintext, plaintext_len);

    ciphertext_len = len;

	EVP_EncryptFinal_ex(ctx, ciphertext + len, &len);
	
    ciphertext_len += len;

	EVP_CIPHER_CTX_free(ctx);

    return ciphertext_len;
}

int main(int argc, const char *argv[])
{

	FILE *fp;
	char *line = NULL;
	size_t len = 0;
	size_t read;
	int p = 0;
	int i;

	//unsigned char key[] = "";
	unsigned char key[16] = { 0 };
	
	/* A 128 bit IV */
	unsigned char iv[128] =  { 0 };

	/* Message to be encrypted */
	unsigned char plaintext[] = "This is a top secret.";

	/* Buffer for ciphertext. Ensure the buffer is long enough for the
	 * ciphertext which may be longer than the plaintext, dependant on the
	 * algorithm and mode
	 */
	unsigned char ciphertext[100] = { 0 };

	int decryptedtext_len, ciphertext_len;

	/* Initialise the library */
	ERR_load_crypto_strings();
	OpenSSL_add_all_algorithms();
	OPENSSL_config(NULL);
			
	/* Encrypt the plaintext */
	fp = fopen("words.txt", "r");
	unsigned char target[64] = {
			0x8d, 0x20, 0xe5, 0x05, 0x6a, 0x8d, 0x24, 
			0xd0, 0x46, 0x2c, 0xe7, 0x4e, 0x49, 0x04, 
			0xc1, 0xb5, 0x13, 0xe1, 0x0d, 0x1d, 0xf4,
		   	0xa2, 0xef, 0x2a, 0xd4, 0x54, 0x0f, 0xae,
		   	0x1c, 0xa0, 0xaa, 0xf9};
	
    char temp[32] = {0};
	while((read = getline(&line, &len, fp)) != -1){
		
        if ( read-1 < 16 ){
			strncpy(temp, line, read-1);
			strcpy(key, temp);
            for (i = 0; i < 16-(read-1); i++) {
                strcat(key, " ");
            }
				
			printf("\nKey %s\nKey in Hex: ", key);
			for(i = 0; i < strlen(key); ++i){
				printf("%02x ", key[i]);
			}
			printf("\n");
			
            encrypt (plaintext, strlen ((char *)plaintext), key,
                    iv, ciphertext);

			printf("\nCiphertext of (This is a top secret.) with key \"%s\"\n", key );
			for(i = 0; i < strlen(ciphertext); ++i){
				printf("%02x ", ciphertext[i]);
			}
			
			printf("\n\nTarget (This is a this secret.) is:\n");
			for(i = 0; i < strlen(target); ++i){
				printf("%02x ", target[i]);
            }
           
            if(ciphertext[0] == target[0] &&
               ciphertext[1] == target[1])
            {
                printf("\n---Match found---\n");
                return 0;
            }

            memset(line, 0, sizeof(line));
            memset(temp, 0, sizeof(temp));
			printf("\n--------\n");
		}
	}

	/* Clean up */
	EVP_cleanup();
	ERR_free_strings();
	return 0;
}
