# PyTorch 2024 Conference

Welcome to the PyTorch 2024 Conference! This event brings together researchers, developers, and enthusiasts from around the world to explore the latest advancements in PyTorch, an open-source machine learning library. Join us for insightful talks, hands-on workshops, and networking opportunities with industry leaders and fellow practitioners. Whether you're a seasoned expert or just starting your journey with PyTorch, this conference offers something for everyone. Let's push the boundaries of machine learning together!

Meta Llama 3 and the Future of Responsible AI Development - Spencer Whitman & Vincent Gonguet, Meta
As AI models become increasingly powerful and pervasive, trust and safety have become top priorities. Join us for a timely talk on Llama 3, our latest foundation model, and the cutting-edge trust and safety models and tools we've developed to ensure responsible AI development. In this talk, we'll dive into: •The advancements of Llama 3 and its applications •Our innovative trust and safety approaches, including toxicity detection and mitigation •The open-source tools and resources we're sharing to empower the community Discover how Meta is pushing the boundaries of trust and safety and learn how you can integrate these solutions into your own projects. Let's build a safer, more responsible AI future together!

1.Open Source is the Path Forward
2.Enable safety research&transparency, release safety-tested foundation models, reduce barriers to safe deployment 
3.system fine-tuning , cubersecurity uplift
4.Cybersec Eval 3,Model &inference guardrails 
5.LLama Guard
6.DeepChem ,graph convolutions ,scikit learn .Deep forest science.
7.Porting from di.
8.Equation solving , Linear equations, differential equations, non-linear equations.

9.GPU vs memory and communications . weights .Torch.compile with FSDP.
10.torch.compile->computation graph and memory allocations.->graph breaks->unsupported operations or data-dependent flow.
11.RopE ,RoPE with NTK.FSDP
12.Activation Checkpointing plays an important role to trades computation and memory.
21.FSDP sharded data including weights 
22.Larger vocab size harms compute-comms overlapping ,torchao .FSDP2 resharding policy.
23. https://github.com/pytorch/xla
24.Increase GPU utilization will create another dileman is to increase power consumption.


Since the boom of generative AI, the industry is now moving towards on-device AI inferencing, as it is not only a trend but a necessity now in order to save costs, achieve the best inference performance, ultra-low latency at the lowest power possible. In this session we go over the new features added on the Qualcomm AI Stack and how it works with the public release of ExecuTorch 1.0. We will discuss how to run traditional workloads as well as GenAI use cases including the latest version of Llama on the Mobile device while using Qualcomm Hexagon NPU.
1.Simple CNN, LSTM, RNN, CNN, AI self is not use case, AI is a tool to accelerate other applications.
2.ExecuTorch,quanizaion schema is only way to run small modules .utilize model sharding algorithm .node fusion/expansion .
https://pytorch.org/executorch-overview
3.AI stack with LoRA.Block Quantization , Optimize the ExecuTorch backend. Weight sharing for prefill and KV cache models.

TorchInductor CPU Backedn Advancement
1.OpemMP, Halide CPU Codegen, Triton CPU Codegen.
2.ATen Vectorzied abstraction. 
3.