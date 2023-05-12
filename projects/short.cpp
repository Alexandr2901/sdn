#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netinet/ip_icmp.h>
#include <netdb.h>
#include <thread>
#include <unistd.h>
#include <time.h>

unsigned short in_cksum(unsigned short *addr, int len)
{
    unsigned long sum = 0;
    while (len > 1)
    {
        sum += *addr++;
        len -= 2;
    }
    if (len == 1)
    {
        sum += *((unsigned char *)addr);
    }
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    return (unsigned short)(~sum);
}
void sendMany(char ip[])
{
    int sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sockfd < 0)
    {
        perror("socket");
    }
    struct sockaddr_in dest_addr;
    bzero(&dest_addr, sizeof(struct sockaddr_in));
    dest_addr.sin_family = AF_INET;
    dest_addr.sin_port = 0;
    dest_addr.sin_addr.s_addr = inet_addr(ip);
    struct icmp *icmp_hdr;
    for (int i = 0; i < 10; i++)
    {
        auto param2 = sizeof(struct icmp);
        auto param4 = (struct sockaddr *)&dest_addr;
        auto param5 = sizeof(dest_addr);
        icmp_hdr = (struct icmp *)malloc(sizeof(struct icmp));
        icmp_hdr->icmp_type = ICMP_ECHO;
        icmp_hdr->icmp_code = 0;
        icmp_hdr->icmp_code = 0;
        icmp_hdr->icmp_id = getpid();
        icmp_hdr->icmp_seq = i;
        icmp_hdr->icmp_cksum = in_cksum((unsigned short *)icmp_hdr, sizeof(struct icmp));
        sendto(sockfd, icmp_hdr, param2, 0, param4, param5);
    }
    free(icmp_hdr);
    close(sockfd);
}
int main(int argc, char **argv)
{
    time_t start, end;
    time(&start);
    int threads = 10;
    std::thread threadPool[threads];
    char ip[] = "172.17.0.2";
    for (int i = 0; i < threads; i++)
    {
        threadPool[i] = std::thread(sendMany, ip);
    }
    for (int i = 0; i < threads; i++)
    {
        threadPool[i].join();
    }
    time(&end);
    double seconds = difftime(end, start);
    printf("The time: %f seconds\n", seconds);
    return 0;
}