---
layout: lecture
title: Hardware Ecosystem
week: 3
session: 1
date: 2022-02-03
start: "14:00"
end: "15:00"
author:
- given: Nic
  family: Lane
  institution: 
  url: http://niclane.org/
abstract: >
  This lecture will look at the changes in hardware that enabled neural networks to be efficient and how neural network models are deployed on hardware.
talkscam:
reveal: true
ipynb: true
youtube: -IXnGgDbE-M
talktheme: white
talkcss: https://inverseprobability.com/assets/css/talks-small.css
time: "14:00"
start: "14:00"
end: "15:00"
---

\subsection{DeepNN}

\subsection{Plan for the Day}

-   **Introduction**
    -   **How did we get here?**
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages

\subsection{Hardware at Deep Learning\'s birth}

<table>

<tr>
<td> \aligncenter{ <h2> New York Times (1958) </h2> } </td>
<td> \aligncenter{ <h2> Eniac, 1950s SoTA Hardware </h2> } </td>
</tr>

<tr>
<td> \includepng{\diagramsDir/hardware/NYT_core}{40%}</td>
<td> \includejpg{\diagramsDir/hardware/Eniac}{40%} </td>
</tr>

</table>

\subsection{How did we get here? Deep Learning requires *peta* FLOPS}

\aligncenter{0.01 PFLOP (left) = $10^{13}$ FLOPS (right)}
\columns{\includepng{\diagramsDir/hardware/provisional_MACs}{100%}}{
\includepng{\diagramsDir/hardware/FLOPS}{100%}}{45%}{45%}


\credit{Our World in Data}{https://ourworldindata.org/technological-progress}


\subsection{Plan for the Day}

-   Introduction
-   **Hardware Foundation**
    -   **Internal organisation of processors**
    -   **A typical organisation of a DL system**
    -   **Two pillars: Data Movement & Parallelism**
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages


\subsection{Internal Organisation of Processors}

\threeColumns{\aligncenter{\includejpg{\diagramsDir/hardware/AMDprocessor}{100%}}}{\aligncenter{\includejpg{\diagramsDir/hardware/GPU}{100%}}}{\aligncenter{\includepng{\diagramsDir/hardware/TPU_out}{100%}}}{30%}{40%}{30%}

\subsection{Central Processing Unit (CPU)}

\columns{* General-purpose processor (in use since mid-1950s)
* CPU is composed of cores, each of which consists of several threads.
* Example high-end performance:
    * AMD Ryzen 9 5950X
    * No. Cores:&emsp;&emsp;&emsp; **16**
    * No. Threads:&emsp;&emsp; **32**
    * Clock speed:&emsp;&emsp; **3.4GHz**, boost up to **4.9GHz**
    * L2 cache:&emsp;&emsp;&ensp;&emsp; **8 MB**
    * L3 cache:&emsp;&emsp;&ensp;&emsp; **64 MB**
}{\includepng{\diagramsDir/hardware/provisional_CPU}{100%}}{60%}{40%}


\showcode{from custom_imports import *

our_custom_net = BasicFCModel()
our_custom_net.cpu()
# OR
device = torch.device('cpu')
our_custom_net.to(device)}


\subsection{Graphics Processing Unit}

\columns{* Parallelism-exploiting Accelerator
* Originally used for graphics processing (in use since 1970s)
* GPU is composed of a large number of threads organised into blocks (cores)
* Example high-end performance:
    * NVIDIA GEFORCE RTX 3090
    * No. Threads:&emsp;&emsp; **10496**
    * Clock speed:&emsp;&emsp; **1.4GHz**, boost up to **1.7GHz**
    * L2 cache:&emsp;&emsp;&ensp;&emsp; **24 GB**}{\includepng{\diagramsDir/hardware/provisional_GPU}{100%}}{60%}{40%}

\showcode{if torch.cuda.is_available():
    our_custom_net.cuda()
    # OR
    device = torch.device('cuda:0')
    our_custom_net.to(device)
# Remember to do the same for all inputs to the network}


\subsection{Graphics Processing Unit}


\columns{* Register (per thread)
  * An automatic variable in kernel
function
  * Low latency, high bandwidth

* Local Memory (per thread)
  * Variable in a kernel but can not be fitted in register
* Shared Memory (between thread blocks)
  * All threads faster than local and global memory
  * Use for inter-thread communication
  * physically shared with L1 cache
* Constant memory
  * Per Device Read-only memory
* Texture Memory
  * Per SM, read-only cache, optimized for 2D spatial locality
* Global Memory}{\includepng{\diagramsDir/hardware/provisional_GPU}{100%}}{60%}{40%}


\subsection{A typical organisation of a DL system}

\columns{* Processors
  * CPU sits at the centre of the system
* <u>**Accelerators**</u>
  * GPUs, TPUs, Eyeriss, other specialised
  * Specialised hardware can be designed with exploiting <u>**parallelism**</u> in mind
* <u>**Memory hierarchy**</u>
  * Caches - smallest and fastest
  * Random Access Memory (RAM) - largest and slowest
  * Disk / SSD - storage
    * Stores the dataset; in crisis it supplements RAM up to Swap 
    * <u>**Bandwidth**</u> can be serious a bottleneck
  * System, memory, and I/O buses
    * Closer to processor - faster
    * Designed to transport fixed-size data chunks
    * Word size is a key system parameter 4 bytes (32 bit) or 8 bytes (64 bit) </pp>
  * Auxiliary hardware
    * Mouse, keyboard, display
}{\includepng{\diagramsDir/hardware/provisional_hardwareOrg}{100%}}{60%}{40%}



\subsection{Data Movement & Parallelism}

\aligncenter{\includepng{\diagramsDir/hardware/provisional_hardwareOrg}{60%}}


\subsection{Memory and bandwidth: memory hierarchy}


\aligncenter{\includepng{\diagramsDir/hardware/provisional_hierarchy2}{70%}}

\subsection{Memory and bandwidth: data movement}

-   Energy and latency are commensurate
-   Accessing RAM is 3 to 4 <u>orders of magnitude</u>
    slower than executing MAC

  

\aligncenter{\includepng{\diagramsDir/hardware/latencynumbers}{100%}}

\subsection{Processor comparison based on memory and bandwidth}



\includepng{\diagramsDir/hardware/provisional_memoryInversion}{45%}

* CPU has faster I/O bus than GPU, but it has
lower bandwidth than GPU.
  <pp>CPU can fetch small pieces of data very fast, GPU fetches them slower but in bulk.</pp>
* GPU has more lower-level memory than CPU.
  <pp>Even though each individual thread and thread block have less memory than
the</pp>
  <pp>CPU threads and cores do, there are just so much more threads in the GPU
that</pp>
  <pp></pp>
  <pp>**taken as a whole** they have much more lower-level memory.</pp>
  <pp>This is memory inversion.</pp> 


\subsection{The case for parallelism - Moore\'s law is slowing down}

-   *Moore\'s law fuelled the prosperity of the past 50 years.*

\aligncenter{\includepng{\diagramsDir/hardware/Moores_Law}{60%}}

\credit{Our World in Data}{https://ourworldindata.org/technological-progress}


\subsection{Plan for the Day}

-   Introduction
-   Hardware Foundation
-   **Parallelism Leveraging**
    -   **Parallelism in Deep Learning**
    -   **Leveraging Deep Learning parallelism**
-   Data Movement and Bandwidth Pressures
-   Closing messages

\subsection{The case for parallelism - Moore's law is slowing down}

-   *As it slows, programmers and hardware designers are searching for
    alternative drivers of performance growth.*

\aligncenter{\includepng{\diagramsDir/hardware/Moores_Law2}{65%}}

\credit{Karl Rupp}{https://github.com/karlrupp/microprocessor-trend-data}

\subsection{Processor comparison based on parallelism}

\showcode{print("CPU matrix multiplication")
a, b = [torch.rand(2**10, 2**10) for _ in range(2)]
start = time()
a * b
print(f'CPU took {time() - start} seconds')
print("GPU matrix multiplication")
start = time()
a * b
print(f'GPU took {time() - start} seconds')}

::: {.output .stream .stdout}
    CPU matrix multiplication
    CPU took 0.0005156993865966797 seconds
    GPU matrix multiplication
    GPU took 0.0002989768981933594 seconds
:::


\subsection{Plan for the Day}

-   Introduction
-   Hardware Foundation
-   **Parallelism Leveraging**
    -   **Parallelism in Deep Learning**
    -   **Leveraging Deep Learning parallelism**
-   Data Movement and Bandwidth Pressures
-   Closing messages

\subsection{Parallelism in Deep Learning training}

-   Minibatch model update:

\aligncenter{\includepng{\diagramsDir/hardware/Picture1}{50%}}

-   where $\theta^{s}_{l,i}$ is an $i$\'s parameter at layer $l$ value
    at step $s$ of the training process; $r$ is the learning rate; $B$
    is the batch size; and $g^{s}_{l,i,b}$ is the $s$-th training step
    gradient coming from $b$-th training example for parameter update of
    $i$-th parameter at layer $l$.

\subsection{DL parallelism: parallelize backprop through an example}

-   The matrix multiplications in the forward and backward passes can be
    parallelized:

\aligncenter{\includepng{\diagramsDir/hardware/Picture2}{50%}}

-   Fast inference is unthinkable without parallel matrix
    multiplication.
-   Frequent synchronization is needed - at each layer the parallel
    threads need to sync up.

\subsection{DL parallelism: parallelize gradient sample computation}

-   Gradients for individual training examples can be computed in
    parallel:

\aligncenter{\includepng{\diagramsDir/hardware/Picture3}{50%}}

-   Synchronization is needed only at the point where we sum the
    individual gradients across the batch.

\subsection{DL parallelism: parallelize update iterations}

-   Gradient updates from separate batches can be computed in parallel:

\aligncenter{\includepng{\diagramsDir/hardware/Picture4}{50%}}

-   Imagine computing $N$ batches at the same time in parallel:
    -   We can see this as using $N-1$ outdated gradient when making
        update based on the second batch.
    -   We can see this as using $N$ gradient estimates in place of the
        usual $1$ that SGD is based on.

\subsection{DL parallelism: parallelize the training of multiple models}

-   In the course of solving a given DL problem one would often train
    competing models because of:
    -   The choice of hyperparameters such as architecture,
        initialization, dropout and learning rates, regularization, \...
    -   The desire to build a model ensemble.

\aligncenter{\includejpg{\diagramsDir/hardware/hyperparameter}{90%}}
-   The models are independent of each other and thus can be computed in
    parallel.


\subsection{Leveraging Deep Learning parallelism}

-   CPUs, GPUs, multi-GPU, and multi-machine each offer unique
    opportunities to leverage the four sources of parallelism.

XXXX

XXXX

XXXX

XXXX

\subsection{CPU training}

The most a CPU can do for this setup is to:

-   Run through the batches *sequentially*
-   Run through the model *sequentially*
-   Run through the batch *sequentially*
-   Potentially, *parallelize* each layer computation between its cores
    -   Best case scenario: individual cores can tackle separate nodes /
        channels as these are independent of each other
-   *Parallelize* matrix multiplication
    -   Best case scenario: Matrix multiplication is split between
        separate cores and threads. The degree of parallelism is,
        however, negligent.

\subsection{CPU training}

Consequently:

-   Overpowered CPU threads are scrambling to juggle the many nodes /
    channels they need to compute.
-   The CPU is slowed down considerably by the fact that it needs to
    access its own L3 cache many more times than the GPU would, due to
    its lower memory access bandwidth.

\showcode{print("CPU training code")
print("CPU training of the above-defined model short example of how long it takes")
our_custom_net.cpu()
start = time()
train(lenet, MNIST_trainloader)
print(f'CPU took {time()-start:.2f} seconds')}

::: {.output .stream .stdout}
    CPU training code
    CPU training of the above-defined model short example of how long it takes
:::

::: {.output .stream .stderr}
    Epoch 1, iter 469, loss 1.980: : 469it [00:02, 181.77it/s]
    Epoch 2, iter 469, loss 0.932: : 469it [00:02, 182.58it/s]
:::

::: {.output .stream .stdout}
    CPU took 5.22 seconds
:::

::: {.output .stream .stderr}
:::

\subsection{GPU training}

The GPU, on the other hand, can:

-   Run through the batches *sequentially*
-   Run through the model *sequentially*
    -   The model and the batch size just fit once in the memory of the
        GPU we chose.
-   In the best case scenario run through the training examples in a
    batch in *parallel*
    -   For most GPUs the computation is, however, *sequential* if their
        memory is not big enough to hold the entire batch of training
        examples.
-   *Parallelize* each layer computation between its cores
    -   Groups of several cores are assigned to separate network layers
        / channels. Cores in the group need not be physically close to
        each other.
-   *Parallelize* matrix multiplication
    -   The matrix multiplication needed to compute a given node /
        channel is split between the threads in the group that was
        assigned to it. Each thread computes separate sector of the
        input.

\subsection{GPU training}

Consequently:

-   GPU cores are engaged at all times as they sequentially push through
    the training examples all at the same time.
-   All threads need to sync-up at the end of each layer computation so
    that their outputs can become the inputs to the next layer.

\showcode{print("GPU training")
print("GPU training of the same example as in CPU")
lenet.cuda()

batch_size = 512
gpu_trainloader = make_MNIST_loader(batch_size=batch_size)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')}

::: {.output .stream .stdout}
    GPU training
    GPU training of the same example as in CPU
:::

::: {.output .stream .stderr}
    Epoch 1, iter 118, iter loss 0.786: : 118it [00:02, 52.62it/s]
    Epoch 2, iter 118, iter loss 0.760: : 118it [00:02, 57.48it/s]
:::

::: {.output .stream .stdout}
    GPU took 4.37 seconds
:::

::: {.output .stream .stderr}
:::

\subsection{GPU parallelism: matrix multiplication example}

\threeColumns{\aligncenter{GPU}\aligncenter{\includepng{\diagramsDir/hardware/provisional_GPU}{100%}}\aligncenter{*12 thread blocks, each with 16 threads.*}}{\aligncenter{Naive implementation}\aligncenter{\includepng{\diagramsDir/hardware/provisional_matmulVOsharedMemory}{100%}}\aligncenter{*Each **thread** reads one row of A, one <br>column of B and returns one element of C.*}}{\aligncenter{Shared memory implementation}\aligncenter{\includepng{\diagramsDir/hardware/provisional_matmul}{100%}}\aligncenter{*Each **thread <u>block</u>** is computing <br>one square sub-matrix.*}}

\subsection{GPU parallelism: matrix multiplication example}

\aligncenter{\includepng{\diagramsDir/hardware/fig7}{100%}}

\subsection{Multi-GPU training}

With multiple GPUs we can choose one of the following:

-   *Distribute* the training examples of a batch between GPUs
    -   When individual GPUs can not hold the whole batch in the memory,
        this can be distributed between multiple cards.
    -   The computation has to sync-up for each Batch-Norm.
-   *Parallelize* the model computation
    -   Separate layers or groups of layers are handled by separate
        GPUs.
    -   Computation syncs between pairs of GPU cards - as the one\'s
        outputs are the other\'s inputs.
    -   This creates a flow-through system that will keep all GPUs busy
        at all times during the training.
    -   Batch is processed sequentially, all GPUs sync up after each
        batch - either dead time or outdated gradients.
-   *Parallelize* the gradient computation
    -   Each GPU can be given its own batch if we accept outdated model
        in gradient computations.

\subsection{Multi-GPU training}

\showcode{print("multi-GPU training")
print("GPU training of the same example as in single GPU but with two GPUs")
our_custom_net_dp = lenet
our_custom_net_dp.cuda()
our_custom_net_dp = nn.DataParallel(our_custom_net_dp, device_ids=[0, 1])
batch_size = 1024
multigpu_trainloader = make_MNIST_loader(batch_size=batch_size)
start = time()
gpu_train(our_custom_net_dp, multigpu_trainloader)
print(f'2 GPUs took {time()-start:.2f} seconds')}

::: {.output .stream .stdout}
    multi-GPU training
    GPU training of the same example as in single GPU but with two GPUs
:::

::: {.output .stream .stderr}
    Epoch 1, iter 59, iter loss 0.745: : 59it [00:02, 21.24it/s]
    Epoch 2, iter 59, iter loss 0.736: : 59it [00:01, 31.70it/s]
:::

::: {.output .stream .stdout}
    2 GPUs took 4.72 seconds
:::

::: {.output .stream .stderr}
:::

\subsection{Multi-Machine training}

In principle the same options as in multi-GPU:

-   *Distribute* the training examples of a batch between GPUs
    -   This is rarely if ever needed on the scale of multi-Machine
-   *Parallelize* the model computation
    -   Same principles as in multi-GPU.
-   *Parallelize* the gradient computation
    -   Same principles as in multi-GPU.

In practice we would either take advantage of the latter two. In extreme
examples one might do a combination of multiple options.

\subsection{Parallelism summary: model and data parallelism}

\columns{\includepng{\diagramsDir/hardware/dataParallelism}{100%}}{\includepng{\diagramsDir/hardware/modelParallelism}{100%}}{49%}{49%}

\subsection{Parallelism bottlenecks: Synchronization & Communication}

\includepng{\diagramsDir/hardware/distributed_bottlenecks4}{80%}

* DL-training hardware needs to synchronize and
communicate very frequently
  * Model nodes are heavily interconnected at each model layer.
  * Data nodes are interconnected by batch-norm-style layers
  * Data nodes are interconnected at gradient computation
* This communication occurs between
  * Threads in a core (CPU and GPU)
  * Cores within a chip
  * Pieces of hardware
    *example: SLI bridge is a connector and a protocol for such a communication*

\subsection{Bottlenecks beyond parallelism}

-   DL training and inference do not take place solely on the
    accelerator.
    -   The accelerator accelerates the gradient computations and
        updates.
    -   The CPU will still need to be loading the data (model, train
        set) and saving the model (checkpointing).
-   The accelerator starves if it waits idly for its inputs due for
    example to slow CPU, I/O buses, or storage interface (SATA, SSD,
    NVMe).

\showcode{print("starving GPUs")
print("show in-code what starving GPU looks like")
# Deliberately slow down data flow into the gpu 
# Do you have any suggestions how to do this in a more realistic way than just to force waiting?
print('Using only 1 worker for the dataloader, the time the GPU takes increases.')
lenet.cuda()
batch_size = 64
gpu_trainloader = make_MNIST_loader(batch_size=batch_size, num_workers=1)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')}

::: {.output .stream .stdout}
    starving GPUs
    show in-code what starving GPU looks like
    Using only 1 worker for the dataloader, the time the GPU takes increases.
:::

::: {.output .stream .stderr}
    Epoch 1, iter 938, iter loss 0.699: : 938it [00:04, 214.02it/s]
    Epoch 2, iter 938, iter loss 0.619: : 938it [00:04, 208.96it/s]
:::

::: {.output .stream .stdout}
    GPU took 8.92 seconds
:::



\subsection{Plan for the Day}

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   **Data Movement and Bandwidth Pressures**
    -   **Deep Learning working set**
    -   **Mapping Deep Learning onto hardware**
    -   **Addressing memory pressure**
-   Closing messages


\subsection{Deep Learning resource characterisation}

\showcode{print("profiling demo")
print("in-house DL training resource profiling code & output - based on the above model and training loop")
#for both of the below produce one figure for inference and one for training
#MACs profiling - first slide; show as piechard

lenet.cpu()
profile_ops(lenet, shape=(1,1,28,28))}

::: {.output .stream .stdout}
    profiling demo
    in-house DL training resource profiling code & output - based on the above model and training loop
    Operation                              OPS      
    -------------------------------------  -------  
    LeNet/Conv2d[conv1]/onnx::Conv         89856    
    LeNet/ReLU[relu1]/onnx::Relu           6912     
    LeNet/MaxPool2d[pool1]/onnx::MaxPool   2592     
    LeNet/Conv2d[conv2]/onnx::Conv         154624   
    LeNet/ReLU[relu2]/onnx::Relu           2048     
    LeNet/MaxPool2d[pool2]/onnx::MaxPool   768      
    LeNet/Linear[fc1]/onnx::Gemm           30720    
    LeNet/ReLU[relu3]/onnx::Relu           240      
    LeNet/Linear[fc2]/onnx::Gemm           7200     
    LeNet/ReLU[relu4]/onnx::Relu           120      
    LeNet/Linear[fc3]/onnx::Gemm           600      
    LeNet/ReLU[relu5]/onnx::Relu           20       
    ------------------------------------   ------   
    Input size: (1, 1, 28, 28)
    295,700 FLOPs or approx. 0.00 GFLOPs
:::


\subsection{Deep Learning working set}

-   Working set - a collection of all elements needed for executing a
    given DL layer
    -   Input and output activations
    -   Parameters (weights & biases)

\showcode{print("working set profiling")
# compute the per-layer required memory:
# memory to load weights, to load inputs, to save oputputs
# visualize as a per-layer bar chart, each bar consists of three sections - the inputs, outputs, weights

profile_layer_mem(lenet)}

::: {.output .stream .stdout}
    working set profiling
:::


\subsection{Working Set requirement exceeding RAM}

\showcode{print("exceeding RAM+Swap demo")
print("exceeding working set experiment - see the latency spike over a couple of bytes of working set")
# sample* a training speed of a model whose layer working sets just first in the memory
# bump up layer dimensions which are far from reaching the RAM limit - see that the effect on latency is limited
# bump up the layer(s) that are at the RAM limit - observe the latency spike rapidly
# add profiling graphs for each of the cases, print out latency numbers.

# *train for an epoch or two, give the latency & give a reasonable estimate of how long would the full training take (assuming X epochs)
estimate_training_for(LeNet, 1000)}

::: {.output .stream .stdout}
    exceeding RAM+Swap demo
    exceeding working set experiment - see the latency spike over a couple of bytes of working set
    Using 128 hidden nodes took 2.42 seconds,        training for 1000 epochs would take ~2423.7449169158936s
    Using 256 hidden nodes took 2.31 seconds,        training for 1000 epochs would take ~2311.570882797241s
    Using 512 hidden nodes took 2.38 seconds,        training for 1000 epochs would take ~2383.8846683502197s
    Using 1024 hidden nodes took 2.56 seconds,        training for 1000 epochs would take ~2559.4213008880615s
    Using 2048 hidden nodes took 3.10 seconds,        training for 1000 epochs would take ~3098.113536834717s
    Using 4096 hidden nodes took 7.20 seconds,        training for 1000 epochs would take ~7196.521997451782s
    Using 6144 hidden nodes took 13.21 seconds,        training for 1000 epochs would take ~13207.558155059814s
:::


\subsection{Working Set requirement exceeding RAM + Swap}

\showcode{print("OOM - massive images")
print("show in-code how this can hapen - say massive images; maybe show error message")
# How could we do this without affecting the recording process?
print('Loading too many images at once causes errors.')
lenet.cuda()
batch_size = 6000
gpu_trainloader = make_MNIST_loader(batch_size=batch_size, num_workers=1)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')}

::: {.output .stream .stdout}
    OOM - massive images
    show in-code how this can hapen - say massive images; maybe show error message
    Loading too many images at once causes errors.
:::

::: {.output .stream .stderr}
    Epoch 1, iter 10, iter loss 0.596: : 10it [00:03,  2.78it/s]
    Epoch 2, iter 2, iter loss 0.592: : 2it [00:01,  1.69it/s]
:::



\subsection{Mapping Deep Models to hardware: Systolic Arrays}

\columns{\aligncenter{**Core principle**}
\aligncenter{\includepng{\diagramsDir/hardware/basic_systolic_system}{100%}}}{
\aligncenter{**Systolic system matrix multiplication**}\aligncenter{\includempfour{\diagramsDir/hardware/systolic_array.mp4}{100%}}}{49%}{49%}

\subsection{Mapping Deep Models to hardware: weight, input, and output stationarity}

**Weight stationary design**

\aligncenter{\includepng{\diagramsDir/hardware/weight_stationary}{70%}}

**Input stationary design**

\aligncenter{\includepng{\diagramsDir/hardware/input_stationary}{70%}}

**Output stationary design**

\aligncenter{\includepng{\diagramsDir/hardware/output_stationary}{70%}}

\subsection{Systolic array example: weight stationary Google Tensor Processing Unit (TPU)}

\aligncenter{\includepng{\diagramsDir/hardware/provisional_TPU3}{60%}}


\subsection{Plan for the Day}

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   **Closing messages**
    -   **Deep Learning stack**
    -   **Deep Learning and accelerator co-design**
    -   **The Hardware and the Software Lottery**


\subsection{Deep Learning stack}

\includepng{\diagramsDir/hardware/TVM_stack2}{80%} 


\subsection{Beyond hardware methods}

-   Sparsity leveraging
    -   Sparsity-inducing compression
    -   Sparsity leveraging hardware
-   Numerical representation
    -   Low precision
    -   bfloat16
    -   Quantization
-   Low-level implementations
    -   GEMM
    -   cuDNN


\subsection{Deep Learning and accelerator co-design}

\aligncenter{\includepng{\diagramsDir/hardware/codesign}{40%}}

\subsection{AlexNet: how GPU memory defined its architecture}

-   Alex Krizhevsky used two GTX 580 GPUs, each with 3GB of memory.
-   Theoretical AlexNet (without mid-way split) working set profiling:

\showcode{print("profile AlexNet layers - show memory requirements")
print("per-layer profiling of AlexNet - connects to the preceding slide")
from torchvision.models import alexnet as net
anet = net()
profile_layer_alexnet(anet)}

::: {.output .stream .stdout}
    profile AlexNet layers - show memory requirements
    per-layer profiling of AlexNet - connects to the preceding slide
:::


\subsection{The actual AlexNet architecture}

AlexNet\'s architecture had to be split down the middle to accommodate
the 3GB limit per unit in its two GPUs.

\aligncenter{\includepng{\diagramsDir/hardware/AlexNet}{70%}}

\subsection{Beyond hardware methods}

-   Sparsity leveraging
    -   Sparsity-inducing compression
    -   Sparsity leveraging hardware
-   Numerical representation
    -   Low precision
    -   bfloat16
    -   Quantization
-   Low-level implementations
    -   GEMM
    -   cuDNN


\subsection{The Hardware and the Software Lotteries}



  
\aligncenter{**The software and hardware lottery describes the success of a software or a piece of hardware  resulting not from its universal superiority, but, rather, from its fit to the broader hardware and software ecosystem.**}

\columns{\aligncenter{Eniac (1950s)}\aligncenter{\includejpg{\diagramsDir/hardware/Eniac}{100%}}}{\aligncenter{All-optical NN (2019)}\aligncenter{\includepng{\diagramsDir/hardware/futureDL}{100%}}}{49%}{49%}


\subsection{Summary of the Day}

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages


# Thank you for your attention!

\subsection{Deep Learning resource characterisation}

\showcode{# memory requirements profiling - second slide; show as piechard
# Show proportion of data required for input, parameters and outputs

profile_mem(lenet)}

