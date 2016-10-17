#include <stdio.h>
#include <string.h>
#include <openssl/evp.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <gmp.h>


void random_string(char * string, unsigned char length);

int main(int argc, char *argv[])
{
	EVP_MD_CTX *mdctx;
	EVP_MD_CTX *mdctx2;
	const EVP_MD *md;
	const EVP_MD *md2; char target[] = "test";
	unsigned char md_value[EVP_MAX_MD_SIZE];
	unsigned char md_value2[EVP_MAX_MD_SIZE];
	unsigned char mess2[32];
	char *cut = malloc(4);
	int j = 0;
	int index = 0;
	int md_len, i, k;
	int not_found = 100;
	i = 0;
	
	OpenSSL_add_all_digests();

	mdctx = EVP_MD_CTX_create();
	md = EVP_get_digestbyname("sha1");
	EVP_DigestInit_ex(mdctx, md, NULL);
	
	EVP_DigestUpdate(mdctx, target, strlen(target));
	EVP_DigestFinal_ex(mdctx, md_value, &md_len);
	
	EVP_MD_CTX_destroy(mdctx);

	/*print digest for message target
	printf("Digest m1 is: ");
	for(i = 0; i < md_len; i++){
		printf("%02x", md_value[i]);
	}
	*/
	
	srand((unsigned int) time(0) + getpid());
	printf("\n");
	unsigned long count = 0;
	unsigned long trial_count[101] = { 0 };
	unsigned long sum = 0;
	unsigned long avg = 0;
	int l;

	while(not_found){
		random_string(mess2, 32);
		count++;
		//printf("\n----\nComputing Digest for: ");
		for(k = 0; k < strlen(mess2); ++k){
			//printf("%d", mess2[k]);
		}
		
		//compute hash of random input value
		mdctx2 = EVP_MD_CTX_create();
		md2 = EVP_get_digestbyname("sha1");
		EVP_DigestInit_ex(mdctx2, md2, NULL);
		EVP_DigestUpdate(mdctx2, mess2, strlen(mess2));
		EVP_DigestFinal_ex(mdctx2, md_value2, &md_len);
		EVP_MD_CTX_destroy(mdctx2);

		//printf("\nHash input is: ");
		for(k = 0; k < md_len; k++){
			//printf("%02x ", md_value2[k]);
		}
		//Check to see if first 3 bytes of hash are colliding
		//with target hash
		if(md_value2[0] == md_value[0] &&
				md_value2[1] == md_value[1] &&
				md_value2[2] == md_value[2]){
			printf("\n----Match found:----\n");

			printf("Target hash is:     ");
			for(l = 0; l < md_len; l++){
				printf("%02x ", md_value[l]);
			}

			printf("\nTrial hash is:      ");
			for(k = 0; k < md_len; k++){
				printf("%02x ", md_value2[k]);
			}

			printf("\nColliding Input Value:\n");
			for(k = 0; k < strlen(mess2); ++k){
				printf("%02x", mess2[k]);
			}

			printf("\nTrial number: %d", count);

			printf("\n----\n");
			trial_count[not_found-1] = count;
			count = 0;
			not_found--;
		}
	}	

	printf("All trials: \n");
	for(i = 0; i < 100; ++i){			
		if(trial_count[i] != 0){
			printf("\n%lu", trial_count[i]);
			sum = sum+trial_count[i];
		}
	}

	avg = sum / 100;
	printf("\n Average Number of Trials: %lu\n", avg);
	
	

	printf("\n");

	/* Call this once before exit. */
	EVP_cleanup();
	exit(0);
}

void random_string(char * string, unsigned char length)
{
	/* ASCII characters 33 to 126 */
	int i;  
	for (i = 0; i < length; ++i)
	{
		string[i] = rand() % 94 + 33;
	}

	string[i] = '\0';  
}
