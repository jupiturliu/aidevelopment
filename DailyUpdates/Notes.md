# 10/3/2024

* Triton Study
* FineTune llama3.2 model with different techniques
  * Unsloth designed to optimize the training and fine-tuning of LLMs
* Exercise for an hour

## Key Features of OpenMP:

Parallelism: Allows you to parallelize code by using compiler directives, library routines, and environment variables.
Shared Memory Model: Uses a shared memory model where multiple threads can access shared data.
Scalability: Scales from a few threads on a single processor to thousands of threads on a multi-processor system.
Ease of Use: Simplifies the process of parallel programming by allowing incremental parallelization of existing code.

OpenMP is widely used in scientific computing, engineering simulations, data analysis, and any application that can benefit from parallel processing.

## What is PrimTorch?

PrimTorch is a project within the PyTorch ecosystem that focuses on providing a set of primitive operations for deep learning. These primitives are low-level operations
that serve as building blocks for more complex neural network operations. The goal of PrimTorch is to offer a minimal and efficient set of operations that can be used
to implement higher-level functionalities in a flexible and optimized manner.

Key Features of PrimTorch:
Low-Level Primitives: Provides a set of basic operations that can be combined to create more complex neural network layers and functions.
Optimization: Designed to be highly efficient, making it suitable for performance-critical applications.
Flexibility: Allows developers to build custom operations and layers by combining these primitives.
Integration: Seamlessly integrates with the broader PyTorch framework, enabling easy use alongside other PyTorch components.
Example Usage:
While specific examples of PrimTorch usage might vary, the general idea is to use these primitives to construct custom neural network components. Here is a conceptual example:

Applications:
PrimTorch is particularly useful for:

Custom Layer Development: Creating custom neural network layers that require specific low-level operations.
Optimization: Fine-tuning performance-critical parts of a neural network.
Research: Experimenting with new neural network architectures and operations.

**dynamic ** specifies whether to enable the code path for Dynamic Shapes. Certain compiler optimizations cannot be applied to dynamic shaped programs

Compile Mode vs Eager Mode

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

# 10/4/2024

# 10/8/2024

* cache-line aware work assignment. bam_ptr
* page cache not only in GPU but CPU.
* GMCT is GPU multiple cache tier
  ![](assets/20241008_150016_image.png)
* TTPoE is a lossy transport protocol
* 突出两部分，一部分是芯片，一部分是路标

# 10/9/2024
fabricmanager:responsible for configuring the intra-node NV link fabric
![alt text](image.png)

UFM(Unified Fabric Manager) is a software package offered by Nvidia that handles network management , performance optimization and monitoring. The CS9500's liquid cool
Weights & Biases(W&B) is a popular tool used for tracking and managing machine learning experiments. It provides a comprehensive paltform for developers and researchers
to visualize ,optimize and collaborate on their machine learning workflows.

# 10/10/2024
AMD advancing AI 
computing engine , open software solution .DPU->UAlink->UEC,Data for CPU processing, GPU for traning and inference.AMD is taking 34% market share.Microsoft, OpenAI Meta is using AMD instinct MI300 series.

AMD end to end AI infrastructure leader.SILO AI is especially focusing on inference and training.push the limits on performance.leveraging OCP platform .

AMD GPU ,Naveen Rao.Databricks is also using MI300X.they are using ROCm. No modification. Very fast and iterate very fast.

We are just at beginning of the AI.performance/dollar/watt.1.5 millions EPIC CPU.MI300X is very instrumental in production.1M models in HuggingFace can run in AMD. 

REka vs Fireworks vs essential AI vs LUMA AI

Why Triton,Optimizing Matrix multiplication.
Graph compilers, is always about the performance and complexity. Triton development timeline.
Users defined tensors in SRAM, and modify them using torch-like operators.

Reducting technical debts.Triton is a mid-level kernel programming language. Triton trades off performance for productivity.Triton allowed OpenAI to scale kernel development.Triton allowed OpenAI to increase research productivity. Triton is portable across different GPU architectures.

Evolution of LLama. Herd to stack. Llama3.x 128K can run GPUs and on-devices,it can support text and image, with Llama Stack.

Distilled and pruned from 8B and 70B. Rewriting and summarization.Next Multimodal models will be 90B and 11B on Llama 3.2. It is adapter architecture and visual recognition. base and isntruct open source model.

Constraint decoding:JSON schema->Regular expression.CPU was used to schedule data. Vectorize CPU operations/Overlap CPU scheduling.

Reka is very likely not exist any more.
# 10/14/2024
How GPU works with CPU
1. Copy the input data from host memory to device memory, also known as host-to-device transfer.
2. Load the GPU program and execute, caching data on-chip for performance.
3. Copy the results from device memory to host memory, also called device-to-host transfer.

A function that is called by the host to execute on GPU is called a kernel.A kernel is executed as a grid of thread blocks.
[Image]
A kernel is executed as a grid of thread blocks, the entirety of blocks is called the grid of that application. Threads in an application are grouped into blocks, A CUDA application is composed of multiple blocks of threads with each thread calls a kernel once.

Cuda introduced a software mechanism called CUDA streams, a workload queue for the device
![alt text](image-1.png)
In CUDA programming, there are two major concepts , one is host ,another one is device.The host is the CPU available in the system, Every CUDA kernel starts with a __global__ declaration specifier, Programmers provide a unique global ID to each thread by using build-in variables.

<<<…>>> these triple angle brackets mark a call from host code to device code,  It is also called a kernel launch.
 The following memories are exposed by the GPU architecture: Registers,these are private to each thread.The compiler makes decision about register utilization.L1/Shared memory(SMEM).L2 cache is shared across all SMs. so every thread in every CUDA block can access this memory.Global memory is the framebuffer size of the GPU and DRAM sitting in the GPU.The CUDA programming model also assumes that both the host and device maintain their own separate memory spaces, referred to as host memory and device memory, respectively.Cuda code also provides for data transfer between host and device memory over the PCIe bus

In H100, there is a new concept called thread block clusters .A cluster is a group of thread blocks that are guaranteed to be concurrently scheduled onto a group of SMs, where the goal is to enable efficient cooperation of threads across multiple SMs.

Nvidia Multi-Instance GPU(MIG) technology was introduced in the NVidia Ampere achitecture-based A100 Tensor Core GPU.

![alt text](image-2.png)

H100 includes a new transformer engine that is a custom hopper tensor core technology to dramatically accelerate the AI calculations for Transformers.At each layer of a Transformer model, the Transformer Engine analyzes the statistics of the putput values produced by the Tensor Core

H100 also introduces the new NVLink network interconnect , a scalable version of NVLink that enables GPU-to-GPU communication among up to 256GPUs across multiple compute nodes。NVSwitch also provides hardware acceleration of collective operations with multicase and NVidia sharp in-netowrk reductions.Accekerated collectives include write broadcast(all_gather),reduce_scatter and broadcast atomics,NDR(Next Data Rate)400Gb/s InfiniBand networking acceleration for secure HPC and AI workloads.Nvidia is a member of the Confidential computing consortium .Data confidentiality, data integrity and code integrity.

federated learning enable multiple organizations to work together to train or evaluate AI models without having to share each group's proprietary datasets

DGX H100 is an AI powerhouse that features the groundbreaking Nvidia H100 Tensor Core GPU.

DGX SuperPODS starts with 32 DGX H100 system, referred to as a "scalable unit"

# 10/16/2024
Only a small number of CUDA threads are now required to manage the full memory bandwidth of H100 using the new Tensor Memory Accelerator.while most other CUDA threads can be focused on general-purpose computations, such as pre-procssing and post-processing data for the new generation of Tensor Cores. Orchestrating the growing number of on-chip accelerators and diverse groups of general purpose threads requires synchronization.Tensor cores arfe specialized processing units designed to acceleratate deep learning and AI workloads.
RAM is the 4th most expensive part of the compute chassis BOM, we recommend downgrading from the standard 2 TBytes to only 1TByte of RAM.
8-Rail optimized networking 

FenFETS cannot scale further and SRAM shrink has beed dead for a few nodes. GAA and backside power delivery .Rapidus .Most EUV lithography is actually used on interconnects(contacts, vias, ane metal layers),not the transistor layer itself.

Deep learning is a specialized subset of machine learning that employs artificial neural networks to analze and interpret complext data.Techniques such as backpropagation are used to adjust the weights of connections between neurons ,minmizing errors and improving accuracy over time.

Reinforcement learning(RL) is a branch of machine learning focused on how agents learn to make decisions by interacting with their environment.RL is a machine learning rechnique where an agent learns to perform tasks by taking actions in an environment and receiving feedback in the form of rewards or penalities.The goal is to maximize cumulative rewards over time through trail and error. Markov decison process(MDP).Reinforcement learning empowers agents to learn optimal behaviors in uncertain environments through feedback mechanisms, making it a pwoerful tool for developing intelligent systems capable of complex decision-making tasks.

# 10/17/2024
# 10/21/2024
Time-sharing and space-sharing are two paradigms for GPU sharing, the primary goal for production clusters is to guarentee the performance of online workloads, xCUDA monitors the GPU memory allocation to limit the memory usage of offline workloads, DL workloads are usually classfied into two categories, online workload and offline workloads, according to the latency demand, online workload refers to latency critical inference, 

# 11/12/2024
1.人类所独有的高阶智慧能力只需要非常少的计算能力,但是无意识的技能和直觉却需要极大的运算能力,"要让电脑如成人般地下棋是相对容易的，但是要让电脑有如一岁小孩般的感知和行动能力却是相当困难甚至是不可能的"
"


# 11/19/2024
right now , you are only foucs on data movement, not computing