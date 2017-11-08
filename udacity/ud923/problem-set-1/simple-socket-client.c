#include <netinet/ip.h>
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>

const int PORT = 8888;

int main()
{
    int tcp_sock = socket(AF_INET, SOCK_STREAM, 0);

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = INADDR_ANY;
    addr.sin_port = htons(PORT);

    if (connect(tcp_sock, (struct sockaddr *) &addr, sizeof(addr)) == -1) {
        printf("Error connecting to the server\n");
        return 1;
    }
    
    printf("Successfully connected to the server\n");
    
    char message[] = "Hello World!";
    if (send(tcp_sock, (void *) message, 100, 0) < 0) {
        printf("Error sending message\n");
    }
    printf("Sent message %s", message);

    close(tcp_sock);
    return 0;
}
