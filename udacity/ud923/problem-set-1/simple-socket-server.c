#include <netinet/ip.h>
#include <stdio.h>
#include <string.h>
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

    if (bind(tcp_sock, (struct sockaddr*) &addr, sizeof(addr)) < 0) {
        printf("Cannot bind server to port %d\n", PORT);
        return -1;
    } else {
        listen(tcp_sock, 5);
        printf("Server running on port %d\n", PORT);
    }

    char message[100];
    int in_conn = accept(tcp_sock, NULL, NULL);
    
    if (recv(in_conn, (void *) message, 100, 0) < 0) {
        printf("Error receiving input connection\n");
    }
    printf("Received message %s", message);

    int i;
    for (i = 0; i < strlen(message); ++i) {
        if (message[i] >= 'a' && message[i] <= 'z')
            message[i] = 'A' + message[i] - 'a';
    }

    if (send(in_conn, (void *) message, 100, 0) < 0) {
        printf("Error sending echo\n");
    }
    printf("Sent message %s", message);

    close(in_conn);
    close(tcp_sock);
    return 0;
}