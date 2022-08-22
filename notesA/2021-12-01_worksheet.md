# Networking: Sockets (continued); TCP/IP model
_COSC 208, Introduction to Computer Systems, 2021-12-01_

## Announcements
* Project 3 due tomorrow at 11pm
* 2nd DEI reflection due Tuesday
* Attend faculty candidate research talks
    * 11:20am Thurs, Dec 2; Tues, Dec 7; Wed, Dec 15
    * Earn 2 points of extra credit on final exam for each talk you attend (earnings capped at 4 points)

## Outline
* SETs
* Warm-up
* Server application 
* TCP/IP model
* Packet switching
* Transport layer

## Warm-up
Q1: _What is wrong with this client application?_
```C
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define HTTP_PORT 80
#define WWW_EXAMPLE_COM 0x5DB8D822 // 93.184.216.34

int main() {
    struct sockaddr_in server_addr;
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = HTTP_PORT;
    server_addr.sin_addr.s_addr = WWW_EXAMPLE_COM;
    int sock = connect((const struct sockaddr *) &server_addr, sizeof(server_addr));

    char buf[1024] = "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n";
    send(sock, buf, strlen(buf), 0);

    int len = recv(sock, buf, 1024, 0);
    buf[len] = '\0';
    printf("%s\n", buf);
}
```

<div style="page-break-after: always;"></div>

## Server application
```C
1   #include <stdio.h>
2   #include <sys/types.h>
3   #include <sys/socket.h>
4   #include <netinet/in.h>
5   #include <string.h>
6   #include <unistd.h>
7
8   int main() {
9       int server_sock = socket(AF_INET, SOCK_STREAM, 0);
10      if (server_sock < 0) {
11         perror("socket failed");
12         return 1;
13      }
14
15      struct sockaddr_in server_addr;
16      server_addr.sin_family = AF_INET;
17      server_addr.sin_port = htons(13346);
18      server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
19      int result = bind(server_sock, &server_addr, sizeof(server_addr));
20      if (result < 0) {
21          perror("bind failed");
22          return 1;
23      }
24
25      result = listen(server_sock, 0);
26      if (result < 0) {
27          perror("listen failed");
28          return 1;
29      }
30
31      struct sockaddr_in client_addr;
32      unsigned int client_addr_len = sizeof(client_addr);
33      int client_sock = accept(server_sock, &client_addr, &client_addr_len);
34
35      char buf[2048];
36      int len = recv(client_sock, buf, 2048, 0);
37      if (len < 0) {
38          perror("recv failed");
39          return 1;
40      }
41      buf[len] = '\0';
42      printf("%s\n", buf);
43
44      strcpy(buf, "Acknowledged\n");
45      len = send(client_sock, buf, strlen(buf), 0);
46      if (len < 0) {
47          perror("send failed");
48          return 1;
49      }
50      
51      close(client_sock);
52      close(server_sock);
53  }
```
