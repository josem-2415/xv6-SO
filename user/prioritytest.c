// Priority scheduler test for xv6-riscv
#include "kernel/types.h"
#include "user/user.h"

static void
busy_work(int id, int prio)
{
  // define priority on process start
  setpriority(prio);
  
  // show info
    for (int i = 0; i < 60; i++) {
      if ((i % 10) == 0) {
        printf("child pid=%d prio=%d id=%d step=%d\n", getpid(), getpriority(), id, i);
      }

      // CPU burn
      volatile int x = 0;
      for (int k = 0; k < 100000; k++) {
        x += k;
      }
    }
    
    // normal exit
    exit(0);
}

int
main(void)
{
  printf("prioritytest: parent pid=%d\n", getpid());

  // Larger value = lower priority in the scheduler
  int prios[4] = { 1, 5, 10, 20 };
  int ids[4]   = { 0,  1,  2,  3 };


  // create 4 process to the test
  for (int i = 0; i < 4; i++) {
    int pid = fork();
    if (pid < 0) {
      printf("fork failed for child %d\n", i);
      exit(1);
    }
    if (pid == 0) {
      // child
      busy_work(ids[i], prios[i]);
    }

    // parent
    printf("spawned child index=%d pid=%d prio=%d\n", i, pid, prios[i]);
  }

  // Wait all children
  for (int i = 0; i < 10; i++) {
    wait(0);
  }

  printf("prioritytest: done\n");
  exit(0);
}

