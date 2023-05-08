express 空间会满，用cluser启动dsw任务





DSW 是交互式建模，







训练任务要提交到cluster分区，不要提交到express分区



express 分区是







用户名：yangzhiyuan

密码: kzhkQq



配置按照 GPU：CPU：内存 = 1：10：80 来设定

DSW实例可以打开关闭，所以尽量节省

如果使用了apt安装，就记得保存镜像，使用名字 latest



镜像环境 

```tex
# cat /etc/issue
Ubuntu 20.04

# nvcc -V
cuda 11.4 
```



创建新环境

conda create -p /cpfs2/user/yangzhiyuan/envs/tf1 python=3.7

conda create -p /cpfs2/user/yangzhiyuan/envs/pytorch3d python=3.9



使用先激活环境

```shell
# main
conda activate /cpfs2/user/yangzhiyuan/envs/py39
conda activate /cpfs2/user/yangzhiyuan/envs/tf1

conda activate /cpfs2/user/yangzhiyuan/envs/torch_py38
```



ssh远程连接

```
ssh -p 30012 yangzhiyuan@dsw.c1579777e051a406a97cefbce72177876.cn-shanghai.alicontainer.com

pws: kzhkQq
```



scp 传输数据集

```
scp -P 30012 -r img_align_celeba.tar.gz yangzhiyuan@dsw.c1579777e051a406a97cefbce72177876.cn-shanghai.alicontainer.com:/cpfs2/shared/public/dataset/celeba
```



scp -P 30012 -r list_landmarks_align_celeba.txt list_landmarks_celeba.txt yangzhiyuan@dsw.c1579777e051a406a97cefbce72177876.cn-shanghai.alicontainer.com:/cpfs2/shared/public/dataset/face/celeba







把文件弄下来：

```python
scp -P 30022 yangzhiyuan@dsw.c1579777e051a406a97cefbce72177876.cn-shanghai.alicontainer.com:/cpfs2/user/yangzhiyuan/Generative-Model/log.zip ./
```





ssh -p 30012 





/cpfs2/shared/public/dataset/celeba



/cpfs2/shared/public/dataset/face/img_align_celeba

/cpfs2/user/yangzhiyuan/Gene





```shell
#!/bin/bash
#SBATCH --partition=gpu_7d1g
#SBATCH --job-name="sbatch Example 01"
#SBATCH --nodes=1
#SBATCH
#SBATCH --ntasks-per-node=1 #1 MPI Task per node
#SBATCH - -time-00:10:00
#SBATCH --gos=normal#SBATCH --gres=gpu:2
#use Normal Q0S
#Request 2 GPU
#say hi to your acc and print out the configuration of GPu
hostname > ./hostname nvidia-smi > ./nvidia-smi module load compiler/cuda/11.0.2 library/cuda/blas/11.0.2
#in case you need CUDA toolkit please list the environment here
#nvcc - help nvcc --help > ./nvcchelp ed / cm/shared/gpu-burn/ ./gpu_burn 3


[shchien@hpclogin01 ~]$ srun --partition-gpu_1d2g --gres=gpu:2 --account=hpc_csc --qos=debug --nodes=1 srun: job 653 queued and waiting for resources ^Csrun: Job allocation 653 has been revoked srun: Force Terminated job 653
[shchien@hpclogin01 ~]$ srun --partition=gpu_1d2g --gres=gpu:1 --account=hpc_csc --qos=debug --nodes=1 [shchien@hpc-gpu001 ~]$
```








I) Access to the System
1) User Interface
− There is no graphical user interface for Burgundy, user must logon the system with Secure Shell (SSH), and x forwarding with SSH is supported with -Y option.

− User should login to the system with CityU EID and AD password, e.g. at your SSH terminal, type,

> ssh <EID>@burgundy.hpc.cityu.edu.hk

− Use PuTTY (on Window) or Terminal (Linux or Mac) to access Burgundy at burgundy.hpc.cityu.edu.hk (IP: 144.214.138.99), e.g.

− PuTTY can be download from the Software list at CityU’s Work Desk (https://www.cityu.edu.hk/csc/deptweb/facilities/terminal-area/studentlan/StudAppWin8.asp)




II) Basic Job Submission
1) General Policy Statement
The current scheduling policy, including partition, quota, and charging schemes, is a temporary provision. The final schemes will be discussed, decided and regularly reviewed by the management committees. Users will be informed before the scheme is implemented and effective.

2) Job Partitions and Priority
i) Job Partitions
− 6 CPU/GPU partitions available for all users

Partition
Time Limit
Min/Max Nodes2,3
Node List
CPU
cpu_1d32n1
1 day
16/32
hpcnode[001-112]

cpu_3d8n
3 days
5/8


cpu_7d2n
7 days
1/2


cpu_14d1n
14 days
1/1

GPU
gpu_1d2g
1 day
2 GPU cards
hpc-gpu[001-007]

gpu_7d1g
7 days
1 GPU card

Note:
Default Partition
Example: cpu_1d32n = 16 to 32 dedicated nodes (128 cores per nodes) for 1 day. 
Node sharing (i.e. multiple jobs on the same node) is allowed for the following partitions:
gpu_1d2g  = Maximum 2 V100s GPU cards per job for 1 day
gpu_7d1g  = 1 V100s GPU cards per job for 7 day
cpu_14d1n = Minimum 64 cores within 1 node for 1 days


− Special Partitions
Please contact HPC support if you need to use these allocations
Partition
Features
Limitation
highmem
Single node with 88 cores and 4TB memory
1 single node job per user
gpu_reserv
Utilize all GPUs (8) on a node
III)  


i) Job Priority
− Instead of using FIFO scheduling scheme, the scheduling priority on the HPC depends on several factors: i.e. Job Size, Job Ages, Quality of Service (QOS), Number of submitted/running jobs (FairShare) and the Partition Properties.
(Ref: https://slurm.schedmd.com/classic_fair_share.html)
− We are working with external parties to improve the scheduling policy and implement the charging system. So, the current weightage for each factor is not finalised and will be changed in due course.
− We favor multi-node jobs by offering higher scheduling priorities for these partitions. However, intentionally requesting excessive resource so as to take advantage of this policy is strictly prohibited. Users’ actual workloads are closely monitored, and repeat offenders of this rule will lead to account suspensions and other penalties.

3) Job Scheduler and Submission
i) Simple Linux Utility for Resource Management (SLURM)
SLURM is an open source, fault-tolerant, and highly scalable cluster management and job scheduling system for large and small Linux clusters. It has been wildly used on many supercomputer systems.
(Ref. https://slurm.schedmd.com/overview.html)

ii) Job submission
− Useful SLURM Commands:
Command
Usage
sinfo
to check available partitions


squeue
to check status of your jobs


Job State Codes:
RUNNING
R
The job currently is allocated to a node and is running.
PENDING
PD
The job is waiting for resource allocation. It will eventually run.
COMPLETING
CG
The job is finishing but some processes are still active.
COMPLETED
CD
The job has completed successfully.
FAILED
F
The job terminated with a non-zero exit code and failed to execute.
PREEMPTED
PR
The job was terminated because of preemption by another job.
SUSPENDED
S
A running job has been stopped with its cores released to other jobs.
STOPPED
ST
A running job has been stopped with its cores retained.
(Ref: https://slurm.schedmd.com/squeue.html#lbAG)

Job Reason Codes:
Resource
The job is waiting for resources to become available and will eventually run.
Priority
One or more higher priority jobs is in queue for running. Your job will eventually run.
QOS(Resource)Limit
Maximum resource for your job’s QoS have been met.
Resource =

MaxJobsPerUser
The maximum number of jobs a user can have running at a given time.
MaxJobsPerAccount
The maximum number of jobs an account (or subaccount) can have running at a given time.
GrpWall
The maximum wall clock time running jobs are able to be allocated in aggregate for a QoS or an association and its children. If this limit is reached, future jobs in this QoS or association will be queued until they are able to run inside the limit.
GrpTRES
The total count of TRES able to be used at any given time from jobs running from an association and its children or QoS
GrpTRESMins
The total number of TRES minutes that can possibly be used by past, present and future jobs running
(Ref: https://slurm.schedmd.com/resource_limits.html)

sbatch <script>
to submit a batch job
scancel <job id>
to kill a waiting or running job

 


− Batch Submission:
∗ A submission script is required to submit a batch job to the system.

∗ The syntax of the SLURM script is similar to a standard shell script:

• The main portion of the script is a standard Linux bash/cash script that will be executed on the compute nodes.
• Lines beginning with #SBATCH are SLURM instructions that will only be read only the SLURM scheduler, i.e. these SLURM instruction lines will only be considered as comments by the Linux shell.

∗ Here is an example of submission script for a CPU node job.
#!/bin/bash
#SBATCH --partition=cpu_14d1n
#SBATCH --nodes=1                # 1 computer nodes
#SBATCH --ntasks-per-node=32     # 32 MPI tasks on EACH NODE
#SBATCH --cpus-per-task=4        # 4 OpenMP threads on EACH TASK, i.e. 1x32x4=128 cores
#SBATCH --mem=440GB              # 440GB mem on EACH NODE
#SBATCH --time=10:00:00          # Time limit hrs:min:sec
#SBATCH --output=C60_%j.log      # Standard output
#SBATCH --error=C60_%j.err       # Standard error log
module load  intel/2020.2.254
module load  intelmpi/2019.8.254
SIESTA=/cm/shared/apps/chemistry/siesta/4.1-266/bin/siesta
OUTPUT=/home/johndoe/scratch/C60.output

cd /home/johndoe/scratch/C60/1
mpirun -genv OMP_NUM_THREADS=4 -genv I_MPI_PIN=1 -genv OMP_PROC_BIND=true -genv OMP_PLACES=cores $SIESTA  < input.fdf > $OUTPUT

date >>$OUTPUT



 


∗ Here is another example of submission script for a 1 GPU job.
#!/bin/bash
#SBATCH --partition=gpu_7d1g
#SBATCH --nodes=1                # 1 computer nodes
#SBATCH --ntasks-per-node=1      # 1 MPI tasks on EACH NODE
#SBATCH --cpus-per-task=4        # 4 OpenMP threads on EACH MPI TASK
#SBATCH --gres=gpu:1             # Using 1 GPU card
#SBATCH --mem=55GB               # Request 50GB memory
#SBATCH --time=0-01:00:00        # Time limit day-hrs:min:sec
#SBATCH --output=gpujob_%j.log   # Standard output
#SBATCH --error=gpujob_%j.err    # Standard error log

module load gcc openmpi/4.0.5/gcc/8.3.0
module load cuda/11.0.2 cuda/blas/11.0.2 cuda/fft/11.0.2
OUTPUT=/home/johndoe/scratch/gpuburn.out
cd /home/johndoe/scratch/gpu-burn/

./gpu_burn 100  >> $OUTPUT

date        >> $OUTPUT




− Interactive Scheduling:
∗ WARNING: Users are not encouraged to use interactive scheduling for long production computation, and interactive job may be terminated due to the heavy workload on the login node. Limitations on the use of Interactive Scheduling will be implemented in the near future.

∗ For certain kinds of workloads that require manual manipulations during the computation, users may request for an interactive scheduling.


∗ Here is an example for requesting an one GPU interactive job:
srun --partition=gpu_7d1g --qos=normal  --nodes=1 --cpus-per-task=4 --ntasks-per-node=1
--gres=gpu:1  --mem=50G -t1:00:0 --pty bash -i




iii) Quality of Service (QoS)
− QoS have been implemented in SLURM; it may affect the jobs in few different aspects, e.g.
∗ Job Scheduling Priority (To be implement in future)
∗ Job Limit (To be implement in future)
∗ Charging (To be implement in future), and
∗ Access of Special Resources

− QoS will be added, deleted or modified on due course based on the need without advance notice to users
− User can use command showQos to check all QoS on the system

 

 

− There are 2 types of QoSs, i.e. User-QoS and Partition-QoSs:
∗ Partition-QoSs (i.e. gpu1 and gpu2) are used to define the partition properties, and they should not be defined inside the job script by users; they will be observed if a conflated User-QoS is defined within the job script. However, certain special QoS can override the limits defined by Partation-QoS (with OverParQOS Flag)
∗ User-QoS can be specified by users in the job script. Default QoS for most users is normal, (low for undergraduate projects and training courses users).
• normal QoS has a Priority factor=25, 8 concurrent RUNNING JOBS are allowed per users; and  60 concurrent RUNNING JOBS for each departmental account (i.e. users from the same department) are allowed.
• high, extreme are reserved for future use when the charging scheme is effective.
• highmem and gpu_vip are assigned to the users who can access the high memory node, and the whole GPU nodes, respectively, under special arrangements.
• debug  QoS is for users to test and verify their submission script before actual submission, so it has a very high priority factor and very tight resource limitations
• stingy QoS is for users who want to run jobs with the lowest priority without charging (UsageFactor=0). These jobs will be subject to be preempted (suspended, re-queued or terminated) when higher priority jobs are submitted to the system. 


iv) General Guideline for Job Submission:
− Favor Large Jobs Policy
∗ Users are encouraged to speed up the computational time by running parallel jobs across multiple nodes when it is possible, and thus we favor multi-node partitions by offering higher scheduling priorities with a shorter time limit.

∗ However, using excessive number of CPU/Nodes will slow down the computation because communication latency overtakes the computational time. (Ref https://hpc.llnl.gov/tutorials/introduction-parallel-computing/limits-and-costs-parallel-programming)

∗ User should benchmark their typical jobs with different combinations of MPI tasks and OpenMP threads on different number of nodes to obtain the best performance of the jobs.

− Use Batch Submission
∗ Long interactive scheduling is strongly discouraged, and we will implement policy to regulate the unnecessary usage of it in the near future.
• Each interactive scheduling will consume certain resource on the login node where shared amongst all login users.
• There is a risk for an abnormal job termination when the login node has encountered network or system hiccup.

∗ User should submit their job with batch script as far as it is possible. (i.e. avoid to use interactive scheduling)

∗ User should clearly specify the resource requirement, i.e. i) Number of Nodes, ii) Number of MPI Task per Node, iii) OpenMP Threads per MPI Task, iv) Memory requirement per Node in the submission script, or the default value will otherwise be applied (i.e. 1 cpu and 3.5GB memory) despite the whole node being allocated.

∗ Because of backfilling algorithm, waiting time can be significantly reduced if a smaller Time Limit has been specified in the job script.

− Use of Local Scratch
∗ Many jobs can take advantage of local scratch, and there is a 350GB local scratch at /local on each compute node.

∗ Users should remove all data on the local scratch when the computational task is completed. All data on the local scratch are not retrievable when the allocation is finished.


VI) Disk Storage and Quota
1) General Storage Policies
i) User Guideline
− It is user’s responsibility to maintain and backup their own data on the HPC system.
− Users should only store research related data on the HPC storage system, and the HPC storage should not be considered as a permanent or backup data storage. All non-researched related or unused data found on the system will be erased without advance notice.
− Any illegal data or material found on the file system will be reported to the authority; related user accounts will be frozen and the related data will be erased when the investigation is finished; the user cannot claim for any loss because of this.
ii) Data Backup Service
There is no data backup service for the HPC service currently, but we will consider to provide this servers at a cost recovery basis if there is such demand from users.

2) Disk Quota
The disk quota scheme has not been enforced currently, but it will be implemented in the near future. Following scheme has been proposed, and user may use it as a reference at this stage.

i) Home Directory: 150GB fixed
− Persistent (i.e. no time limit) home space for user login.
− Suitable to keep the following data
∗ essential files for user login
∗ user’s self-maintained libraries and applications
∗ templates for inputs and submission scripts
ii) Scratch Directory: 300GB by default
− A working space for users to carry out computation jobs
∗ Storing inputs, outputs and temporary/scratch files
− Unused file will be erased regularly.
∗ Users should backup the important data on their own local storage when the job is finished.
− Additional space can be arranged upon request with justification. Each case will be considered individually.
iii) NAS (Will be implemented in future)

VIII) Software Stacks
Lmod Environment Modules has been used to manage the software packages on the HPC system, and users can dynamically change their software environment through modulefiles.
(https://lmod.readthedocs.io/en/latest/)

There is a public modulefile set managed by CSC, the environment variable MODULEPATH has been set as follow by default.  

MODULEPATH=/cm/local/modulefiles:/etc/modulefiles:/usr/share/modulefiles:/usr/share/Modules/modulefiles:/cm/shared/modulefiles/compiler:/cm/shared/modulefiles/library:/cm/shared/modulefiles/mpi:/cm/shared/apps/mpi/hpcx/2.8.0/modulefiles




The current modulefile set is minimal, and we are preparing a more comprehensive set which covers more scientific applications and programming tools. Users will be informed when the new environment set is ready.

1) Use of Environment Modules
i) Common module commands
Command
Usage
module av
To see available modules
module list
To see currently loaded module
module load mod
To load module mod to environment
module unload mod
To unload module mod
module swap old new
To swap module old with new
module purge
To unload all loaded modules
module whatis mod
To show module mod’s information

ii) Append self-maintained module set
User can create their own modulefile set by appending the path of the directories which contain the modulefiles to the MODULEPATH variable.

The syntax of modulefile can be found in this web page:
https://lmod.readthedocs.io/en/latest/100_modulefile_examples.html

2) Singularity Containers
Users are encourage to install their own application packages as a Singularity container image (https://sylabs.io/guides/3.7/user-guide/) on their own desktop/workstation/labtop, and run the it on Burgundy’s GPU node.  This is the only method to run customized system environment (e.g. a different Linux distro such as Ubuntu 18) or libraries (e.g. python 2, unsupported libgc) or optimized AI packages prepared by Nvidia.

In general, user can build their own singularity as follow:
(Ref https://sylabs.io/guides/3.7/user-guide/quick_start.html#build-images-from-scratch)

 

i) Prepare a definition file under a X86-64 Linux environment.
- In this example, we will install the the packages, such as, gcc, and  and python with apt-get on a Ubuntu 18.04 images.
- CUDA 10.0 libraries directly downloaded from Nvidia will be installed.
- Tensorflow (with GPU supported), numpy and OpenCV will be installed with pip within the image subsequently.

 

ii) Build image with Singularity command.This example was done on a CentOS Linux VM (Virtual Box) under MacOS


iii) Upload the Singularity image to HPC Login Node 


iv) Submit the job and request the resource; in this example, an interactive schedule is used for illustration purpose only, and user should submit batch jobs if it is possible.
- Login to system, and submit an interactive job

- When the resource is allocated, the prompt will change to indicate which node has been assigned (i.e. hpc-gpu001 in this case).
For illustration purpose, we show the distro information of the Base System; it is a CentOS 8

- Execute Linux commands from the singularity image.
First, we ask to show the distro information of the client (the image), and it is a Ubuntu 18.04

Then, we call python3 from the image.  


3) Other Specific Software Issues
    i) Matlab
    A copy of Matlab has been installed, and you can find Matlab R2002b at the following locateion
    /cm/shared/apps/maths/matlab/R2020b/bin

CityU’s Matlab license servers are reachable to all nodes, and user may include this in you license file if you prefer to run your own copy of Matlab.
############################################################
SERVER berkeley101.ad.cityu.edu.hk 005056981E16 27000
SERVER berkeley102.ad.cityu.edu.hk 005056988B9D 27000
SERVER berkeley103.ad.cityu.edu.hk 005056981B97 27000
USE_SERVER
############################################################

ii) Other Commercial Software
Due to the license issue, CSC will help to install shared license to the license server, but we cannot provide support for any user-owned license packages, please contact the distributor of the software for support.



