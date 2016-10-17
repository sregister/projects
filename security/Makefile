INC=/usr/include/openssl/
LIB=/usr/lib/openssl/

default:
	make clean
	make one
	make onep2
	make two

two:
	gcc -I$(INC) -L$(LIB) -o two prog2.c -lcrypto -ldl

one:
	gcc -I$(INC) -L$(LIB) -o one prog1.c -lcrypto -ldl -lgmp -lm

onep2:
	gcc -I$(INC) -L$(LIB) -o onep2 prog1p2.c -lcrypto -ldl -lgmp -lm

clean:
	rm -rf one
	rm -rf two
	rm -rf onep2
