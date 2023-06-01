#include <stdio.h>
#include <time.h>
#include <stdint.h>
#include <assert.h>

#define N 1024
#define BLOCK 4
#define t 1

float A[N][N];
float B[N][N];
float C[N][N];

uint64_t nanos() {
    struct timespec start;
    clock_gettime(CLOCK_MONOTONIC_RAW, &start);
    return (uint64_t)start.tv_sec * (1000000000) + (uint64_t)start.tv_nsec;
}

void printMat(float mat[N][N]) {
    printf("%s", "[");
    for (int y = 0; y < N; y++) {
        printf("%s", "[");
        for (int x = 0; x < N; x++)
        {
            printf("%f", mat[y][x]);
        }
        printf("%s", "s]\n");
    }
    printf("%s", "]\n");
}


float* fast() {
    for (int by = 0; by < N; by += BLOCK) {
        for (int bx = 0; bx < N; bx += BLOCK) {

            for (int y = by; y < by+BLOCK; y++){
                for (int x = bx; x < bx+BLOCK; x++){
                    float acc = 0;
                    for (int k = by; k < by+BLOCK; k++){
                        acc += A[y][k] * B[k][x];
                    }
                    C[y][x] = acc;
                }
            }
        }
    }

    return *C;
}


float* slow() {
    for (int y = 0; y < N; y++){
        for (int x = 0; x < N; x++){
            float acc = 0;
                for (int k = 0; k < N; k++){
                    acc += A[y][k] * B[k][x];
                }
            C[y][x] = acc;
        }
    }

    return *C;
}

int main()
{
    assert(N % BLOCK == 0);

    uint64_t start = nanos();

    if(t) {
        fast();
    } else {
        slow();
    }

    uint64_t end = nanos();
    double gflop = (2.0 * N * N * N) * 1e-12;
    double s = (end - start) * 1e-9;
  
    printMat(C);
    printf("%f GFLOP/s\n", gflop / s);  
    return 0;
}

