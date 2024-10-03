Triton annual conference in 2024 in Meta campus
https://tritondeveloperconference.splashthat.com/?full_url=https%3A%2F%2Ftritondeveloperconference.splashthat.com%2F

1.react is also from meta
2.3D Backend
3.TritonGPU-IR is oftern forked as a custom IR
4.Proton
5.Interpreter
6.software pipelining is becoming more complex
7.warp specialization
8.what is register spilling?
9.eba
10.vector dialect, artifact example
11.vector engine, tensor engine , scalar engine GPSIMD SBUF PSUM and HBM.
12 Triton leads to the neuron kernel interface
13.Tile semantics .torch autograd.
14.Qualcom Hexagon NPU
15.epilogue hiding, software pipelining . TMA support.
16.Triton is on the right track to be adopted by whole industry 
17.metaprogramming ,MLIR based tracing DSL.Mosiac thread.PTX into a kernel 
18.TMA, or Tensor Memory Accelerator, is a feature introduced in NVIDIA's Hopper architecture that enables asynchronous memory copying between global memory (GMEM) and shared memory (SMEM) on GPUs. This functionality is particularly beneficial for improving performance in deep learning and high-performance computing applications.
19.WGMMA, or Warp Group Matrix Multiply Accumulate, is a feature introduced in NVIDIA's Hopper GPU architecture that enables efficient matrix multiplication operations using specialized hardware called Tensor Cores. Here are the key points about WGMMA:
WGMMA Basics
Warp Group: WGMMA operates on a warp group, which consists of 128 threads. All threads in a warp group collaborate to perform a single matrix multiplication.
Supported Data Types: WGMMA supports various data types for the operands and accumulator, including FP16, TF32, BF16, and integer types like INT8 and INT4.
Tile Sizes: WGMMA computes matrix multiplications on specific tile sizes. For example, it can compute a 64x64x16 matrix multiplication for FP16 operands and accumulator.
Layouts: The input matrices must be in specific layouts that are compatible with WGMMA. These layouts include row-major (MN), column-major (KM), and specialized swizzled layouts for shared memory.
20.Compiling time is take minutes. torch inductor.
21.nccl timeout. overlap the communication and computing, tensor parallelism. 




