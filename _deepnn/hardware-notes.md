::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
# Hardware Ecosystem

## Nic Lane (ndl32)

## DeepNN
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Plan for the Day

-   **Introduction**
    -   **How did we get here?**
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Hardware at Deep Learning\'s birth

`<br/>`{=html}

```{=html}
<table>

<tr>
<td> <center> <h2> New York Times (1958) </h2> </center> </td>
<td> <center> <h2> Eniac, 1950s SoTA Hardware </h2> </center> </td></tr>

<tr>
<td> <img src="inputs/NYT_core.png" alt="Drawing" style="width: 800px;"/> </td>
<td> <img src="inputs/Eniac.JPG" alt="Drawing" style="width: 800px;"/> </td>
</tr>

</table>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## How did we get here? Deep Learning requires *peta* FLOPS

`<br/>`{=html} `<center>`{=html}0.01 PFLOP (left) = $10^{13}$ FLOPS
(right) `<table>`{=html}`<tr>`{=html} `<td>`{=html}
`<img src="inputs/provisional_MACs.png" alt="Drawing" style="width: 945px;"/>`{=html}
`</td>`{=html} `<td>`{=html}
`<img src="inputs/FLOPS.png" alt="Drawing" style="width: 600px;"/>`{=html}
`</td>`{=html} `</tr>`{=html}`</table>`{=html}

Credits: Our World in Data
(<https://ourworldindata.org/technological-progress>)
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Plan for the Day {#plan-for-the-day}

-   Introduction
-   **Hardware Foundation**
    -   **Internal organisation of processors**
    -   **A typical organisation of a DL system**
    -   **Two pillars: Data Movement & Parallelism**
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Internal Organisation of Processors

`<br/>`{=html} `<table>`{=html} `<tr>`{=html}
`<td>`{=html}`<center>`{=html}`<img src=inputs/AMDprocessor.jpg alt="Drawing" style="width: 800px;"/>`{=html}`</td>`{=html}
`<td>`{=html}`<center>`{=html}`<img src=inputs/GPU.jpg alt="Drawing" style="width: 1100px;"/>`{=html}`</td>`{=html}
`<td>`{=html}`<center>`{=html}`<img src=inputs/TPU_out.png alt="Drawing" style="width: 900px;"/>`{=html}`</td>`{=html}
`</tr>`{=html} `</table>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Central Processing Unit (CPU)

```{=html}
<p>
```
`<img src=inputs/provisional_CPU.png align="right" alt="Drawing" style="width: 700px;"/>`{=html}
`<ul>`{=html}

```{=html}
<li>General-purpose processor (in use since mid-1950s)</li>
```
```{=html}
<li>CPU is composed of cores, each of which consists of several threads.</li>
```
```{=html}
<li>Example high-end performance:</li>
```
    <ul><li>AMD Ryzen 9 5950X</li></ul>
    <ul><li>No. Cores:&emsp;&emsp;&emsp; <b>16</b></li></ul>
    <ul><li>No. Threads:&emsp;&emsp; <b>32</b></li></ul>
    <ul><li>Clock speed:&emsp;&emsp; <b>3.4GHz</b>, boost up to <b>4.9GHz</b></li></ul>
    <ul><li>L2 cache:&emsp;&emsp;&ensp;&emsp; <b>8 MB</b></li></ul>
    <ul><li>L3 cache:&emsp;&emsp;&ensp;&emsp; <b>64 MB</b></li></ul>

```{=html}
<p>
```
:::

::: {.cell .code scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
from custom_imports import *

our_custom_net = BasicFCModel()
our_custom_net.cpu()
# OR
device = torch.device('cpu')
our_custom_net.to(device)
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Graphics Processing Unit

```{=html}
<p>
```
`<img src=inputs/provisional_GPU.png align="right" alt="Drawing" style="width: 700px;"/>`{=html}
`<ul>`{=html}

```{=html}
<li>Parallelism-exploiting Accelerator</li>
```
```{=html}
<li>Originally used for graphics processing (in use since 1970s)</li>
```
```{=html}
<li>GPU is composed of a large number of threads organised into blocks (cores)</li>
```
```{=html}
<li>Example high-end performance:</li>
```
    <ul><li>NVIDIA GEFORCE RTX 3090</li></ul>
    <ul><li>No. Threads:&emsp;&emsp; <b>10496</b></li></ul>
    <ul><li>Clock speed:&emsp;&emsp; <b>1.4GHz</b>, boost up to <b>1.7GHz</b></li></ul>
    <ul><li>L2 cache:&emsp;&emsp;&ensp;&emsp; <b>24 GB</b></li></ul>

```{=html}
<p>
```
:::

::: {.cell .code scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
if torch.cuda.is_available():
    our_custom_net.cuda()
    # OR
    device = torch.device('cuda:0')
    our_custom_net.to(device)
# Remember to do the same for all inputs to the network
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Graphics Processing Unit {#graphics-processing-unit}

```{=html}
<p>
```
`<img src=inputs/provisional_GPU.png align="right" alt="Drawing" style="width: 700px;"/>`{=html}
`<ul>`{=html} `<li>`{=html}Register (per thread)`</li>`{=html}
`<ul>`{=html}`<li>`{=html}An automatic variable in kernel
function`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Low
latency, high bandwidth`</li>`{=html}`</ul>`{=html} `<li>`{=html}Local
Memory (per thread)`</li>`{=html} `<ul>`{=html}`<li>`{=html}Variable in
a kernel but can not be fitted in register`</li>`{=html}`</ul>`{=html}
`<li>`{=html}Shared Memory (between thread blocks)`</li>`{=html}
`<ul>`{=html}`<li>`{=html}All threads faster than local and global
memory`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Use for
inter-thread communication`</li>`{=html}`</ul>`{=html}
`<ul>`{=html}`<li>`{=html}physically shared with L1
cache`</li>`{=html}`</ul>`{=html} `<li>`{=html}Constant
memory`</li>`{=html} `<ul>`{=html}`<li>`{=html}Per Device Read-only
memory`</li>`{=html}`</ul>`{=html} `<li>`{=html}Texture
Memory`</li>`{=html} `<ul>`{=html}`<li>`{=html}Per SM, read-only cache,
optimized for 2D spatial locality`</li>`{=html}`</ul>`{=html}
`<li>`{=html}Global Memory`</li>`{=html} `<p>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## A typical organisation of a DL system

```{=html}
<p>
```
`<img src=inputs/provisional_hardwareOrg.png align="right" alt="Drawing" style="width: 1050px;"/>`{=html}
`<ul>`{=html} `<li>`{=html}Processors`</li>`{=html}
`<ul>`{=html}`<li>`{=html}CPU sits at the centre of the
system`</li>`{=html}`</ul>`{=html}
`<li>`{=html}`<u>`{=html}`<b>`{=html}Accelerators`</b>`{=html}`</u>`{=html}`</li>`{=html}\
`<ul>`{=html}`<li>`{=html}GPUs, TPUs, Eyeriss, other
specialised`</li>`{=html}`</ul>`{=html}
`<ul>`{=html}`<li>`{=html}Specialised hardware can be designed with
exploiting `<u>`{=html}`<b>`{=html}parallelism`</b>`{=html}`</u>`{=html}
in mind`</li>`{=html}`</ul>`{=html}\
`<li>`{=html}`<u>`{=html}`<b>`{=html}Memory
hierarchy`</b>`{=html}`</u>`{=html}`</li>`{=html}
`<ul>`{=html}`<li>`{=html}Caches - smallest and
fastest`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Random
Access Memory (RAM) - largest and slowest`</li>`{=html}`</ul>`{=html}
`<ul>`{=html}`<li>`{=html}Disk / SSD -
storage`</li>`{=html}`</ul>`{=html}\
`<ul>`{=html} `<ul>`{=html}`<li>`{=html}Stores the dataset; in crisis it
supplements RAM up to Swap`</li>`{=html}`</ul>`{=html} `</ul>`{=html}
`<ul>`{=html}`<li>`{=html}`<u>`{=html}`<b>`{=html}Bandwidth`</b>`{=html}`</u>`{=html}
can be serious a bottleneck`</li>`{=html}`</ul>`{=html}
`<li>`{=html}System, memory, and I/O buses`</li>`{=html}
`<ul>`{=html}`<li>`{=html}Closer to processor -
faster`</li>`{=html}`</ul>`{=html}\
`<ul>`{=html}`<li>`{=html}Designed to transport fixed-size data
chunks`</li>`{=html}`</ul>`{=html}\
`<ul>`{=html}`<li>`{=html}Word size is a key system parameter 4 bytes
(32 bit) or 8 bytes (64 bit) `</pp>`{=html}`</ul>`{=html}\
`<li>`{=html}Auxiliary hardware`</li>`{=html}
`<ul>`{=html}`<li>`{=html}Mouse, keyboard,
display`</li>`{=html}`</ul>`{=html}\
`<p>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Data Movement & Parallelism {#data-movement--parallelism}

```{=html}
<center><img src=inputs/provisional_hardwareOrg.png alt="Drawing" style="width: 1200px;"/></center>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Memory and bandwidth: memory hierarchy

`<br/>`{=html} `<br/>`{=html}

```{=html}
<center>
```
`<img src=inputs/provisional_hierarchy2.png alt="Drawing" style="width: 1400px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Memory and bandwidth: data movement

-   Energy and latency are commensurate
-   Accessing RAM is 3 to 4 `<u>`{=html}orders of magnitude`</u>`{=html}
    slower than executing MAC

`<br/>`{=html} `<br/>`{=html} `<br/>`{=html}

```{=html}
<center>
```
`<img src=inputs/latencynumbers.png alt="Drawing" style="width: 2000px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Processor comparison based on memory and bandwidth

```{=html}
<p>
```
`<img src=inputs/provisional_memoryInversion.png align="right" alt="Drawing" style="width: 900px;"/>`{=html}
`<ul>`{=html} `<li>`{=html}CPU has faster I/O bus than GPU, but it has
lower bandwidth than GPU.`</li>`{=html} `<ul>`{=html}`<pp>`{=html}CPU
can fetch small pieces of data very fast, GPU fetches them slower but in
bulk.`</pp>`{=html}`</ul>`{=html} `<li>`{=html}GPU has more lower-level
memory than CPU.`</li>`{=html} `<ul>`{=html}`<pp>`{=html}Even though
each individual thread and thread block have less memory than
the`</pp>`{=html}`</ul>`{=html} `<ul>`{=html}`<pp>`{=html}CPU threads
and cores do, there are just so much more threads in the GPU
that`</pp>`{=html}`</ul>`{=html}\
`<ul>`{=html}`<pp>`{=html}`<b>`{=html}taken as a whole`</b>`{=html} they
have much more lower-level memory.`</pp>`{=html}`</ul>`{=html}
`<ul>`{=html}`<pp>`{=html}This is memory
inversion.`</pp>`{=html}`</ul>`{=html} `<p>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## The case for parallelism - Moore\'s law is slowing down

-   *Moore\'s law fuelled the prosperity of the past 50 years.*

```{=html}
<center>
```
`<img src=inputs/Moores_Law.png alt="Drawing" style="width: 1200px;"/>`{=html}

Credits: Our World in Data
(<https://ourworldindata.org/technological-progress>)
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Plan for the Day {#plan-for-the-day}

-   Introduction
-   Hardware Foundation
-   **Parallelism Leveraging**
    -   **Parallelism in Deep Learning**
    -   **Leveraging Deep Learning parallelism**
-   Data Movement and Bandwidth Pressures
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## The case for parallelism - Moore\'s law is slowing down {#the-case-for-parallelism---moores-law-is-slowing-down}

-   *As it slows, programmers and hardware designers are searching for
    alternative drivers of performance growth.*

```{=html}
<center>
```
`<img src=inputs/Moores_Law2.png alt="Drawing" style="width: 1300px;"/>`{=html}

Credits: Karl Rupp
(<https://github.com/karlrupp/microprocessor-trend-data>)
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Processor comparison based on parallelism
:::

::: {.cell .code execution_count="3" scrolled="false"}
``` {.python}
print("CPU matrix multiplication")
a, b = [torch.rand(2**10, 2**10) for _ in range(2)]
start = time()
a * b
print(f'CPU took {time() - start} seconds')
print("GPU matrix multiplication")
start = time()
a * b
print(f'GPU took {time() - start} seconds')
```

::: {.output .stream .stdout}
    CPU matrix multiplication
    CPU took 0.0005156993865966797 seconds
    GPU matrix multiplication
    GPU took 0.0002989768981933594 seconds
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Plan for the Day {#plan-for-the-day}

-   Introduction
-   Hardware Foundation
-   **Parallelism Leveraging**
    -   **Parallelism in Deep Learning**
    -   **Leveraging Deep Learning parallelism**
-   Data Movement and Bandwidth Pressures
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Parallelism in Deep Learning training

-   Minibatch model update:

```{=html}
<center><img src=inputs/Picture1.png alt="Drawing" style="width: 1000px;"/></center>
```
-   where $\theta^{s}_{l,i}$ is an $i$\'s parameter at layer $l$ value
    at step $s$ of the training process; $r$ is the learning rate; $B$
    is the batch size; and $g^{s}_{l,i,b}$ is the $s$-th training step
    gradient coming from $b$-th training example for parameter update of
    $i$-th parameter at layer $l$.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## DL parallelism: parallelize backprop through an example

-   The matrix multiplications in the forward and backward passes can be
    parallelized:

```{=html}
<center><img src=inputs/Picture2.png alt="Drawing" style="width: 1000px;"/></center>
```
-   Fast inference is unthinkable without parallel matrix
    multiplication.
-   Frequent synchronization is needed - at each layer the parallel
    threads need to sync up.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## DL parallelism: parallelize gradient sample computation

-   Gradients for individual training examples can be computed in
    parallel:

```{=html}
<center><img src=inputs/Picture3.png alt="Drawing" style="width: 1000px;"/></center>
```
-   Synchronization is needed only at the point where we sum the
    individual gradients across the batch.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## DL parallelism: parallelize update iterations

-   Gradient updates from separate batches can be computed in parallel:

```{=html}
<center><img src=inputs/Picture4.png alt="Drawing" style="width: 1000px;"/></center>
```
-   Imagine computing $N$ batches at the same time in parallel:
    -   We can see this as using $N-1$ outdated gradient when making
        update based on the second batch.
    -   We can see this as using $N$ gradient estimates in place of the
        usual $1$ that SGD is based on.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## DL parallelism: parallelize the training of multiple models

-   In the course of solving a given DL problem one would often train
    competing models because of:
    -   The choice of hyperparameters such as architecture,
        initialization, dropout and learning rates, regularization, \...
    -   The desire to build a model ensemble.

```{=html}
<center><img src=inputs/hyperparameter.jpeg alt="Drawing" style="width: 1800px;"/></center>
```
-   The models are independent of each other and thus can be computed in
    parallel.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Leveraging Deep Learning parallelism

-   CPUs, GPUs, multi-GPU, and multi-machine each offer unique
    opportunities to leverage the four sources of parallelism.

XXXX

XXXX

XXXX

XXXX
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## CPU training

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## CPU training {#cpu-training}

Consequently:

-   Overpowered CPU threads are scrambling to juggle the many nodes /
    channels they need to compute.
-   The CPU is slowed down considerably by the fact that it needs to
    access its own L3 cache many more times than the GPU would, due to
    its lower memory access bandwidth.
:::

::: {.cell .code execution_count="7" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("CPU training code")
print("CPU training of the above-defined model short example of how long it takes")
our_custom_net.cpu()
start = time()
train(lenet, MNIST_trainloader)
print(f'CPU took {time()-start:.2f} seconds')
```

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## GPU training

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## GPU training {#gpu-training}

Consequently:

-   GPU cores are engaged at all times as they sequentially push through
    the training examples all at the same time.
-   All threads need to sync-up at the end of each layer computation so
    that their outputs can become the inputs to the next layer.
:::

::: {.cell .code execution_count="8" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("GPU training")
print("GPU training of the same example as in CPU")
lenet.cuda()

batch_size = 512
gpu_trainloader = make_MNIST_loader(batch_size=batch_size)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')
```

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## GPU parallelism: matrix multiplication example

`<br/>`{=html}

```{=html}
<table><tr>
<td> <center> <h2> GPU </h2> </center></td>
<td> <center> <h2> Naive implementation </h2> </center></td>
<td> <center> <h2> Shared memory implementation </h2> </center></td>
</tr>
    
<tr>
<td><center><img src=inputs/provisional_GPU.png alt="Drawing" style="width: 500px;"/></center></td>
<td><center><img src=inputs/provisional_matmulVOsharedMemory.png alt="Drawing" style="width: 500px;"/></center></td>
<td><center><img src=inputs/provisional_matmul.png alt="Drawing" style="width: 500px;"/></center></td>
</tr>
    
<tr>
<td>
    <center><ul><pp><h6> 12 thread blocks, each with 16 threads. </h6></ul></pp></center>
</td>
<td>
    <center><ul><pp><h6>Each <b>thread</b> reads one row of A, one <br>column of B and returns one element of C.</h6></ul></pp></center>
</td>
<td>  
    <center><ul><pp><h6>Each <b>thread <u>block</u></b> is computing <br>one square sub-matrix.</h6> </ul></pp></center>
</td>
</tr>
</table>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## GPU parallelism: matrix multiplication example {#gpu-parallelism-matrix-multiplication-example}

`<br/>`{=html} `<br/>`{=html}

```{=html}
<center><img src=inputs/fig7.png alt="Drawing" style="width: 2000px;"/></center>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Multi-GPU training

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Multi-GPU training {#multi-gpu-training}
:::

::: {.cell .code execution_count="9" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("multi-GPU training")
print("GPU training of the same example as in single GPU but with two GPUs")
our_custom_net_dp = lenet
our_custom_net_dp.cuda()
our_custom_net_dp = nn.DataParallel(our_custom_net_dp, device_ids=[0, 1])
batch_size = 1024
multigpu_trainloader = make_MNIST_loader(batch_size=batch_size)
start = time()
gpu_train(our_custom_net_dp, multigpu_trainloader)
print(f'2 GPUs took {time()-start:.2f} seconds')
```

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Multi-Machine training

In principle the same options as in multi-GPU:

-   *Distribute* the training examples of a batch between GPUs
    -   This is rarely if ever needed on the scale of multi-Machine
-   *Parallelize* the model computation
    -   Same principles as in multi-GPU.
-   *Parallelize* the gradient computation
    -   Same principles as in multi-GPU.

In practice we would either take advantage of the latter two. In extreme
examples one might do a combination of multiple options.
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Parallelism summary: model and data parallelism

`<br/>`{=html}

```{=html}
<table><tr>
<td> <img src="inputs/dataParallelism.png" alt="Drawing" style="width: 700px;"/> </td>
<td> <img src="inputs/modelParallelism.png" alt="Drawing" style="width: 740px;"/> </td>
</tr></table>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Parallelism bottlenecks: Synchronization & Communication {#parallelism-bottlenecks-synchronization--communication}

```{=html}
<p>
```
`<img src=inputs/distributed_bottlenecks4.png align="right" alt="Drawing" style="width: 1100px;"/>`{=html}
`<ul>`{=html} `<li>`{=html}DL-training hardware needs to synchronize and
communicate very frequently`</li>`{=html}
`<ul>`{=html}`<li>`{=html}Model nodes are heavily interconnected at each
model layer.`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Data
nodes are interconnected by batch-norm-style
layers`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Data nodes
are interconnected at gradient computation`</li>`{=html}`</ul>`{=html}
`<li>`{=html}This communication occurs between`</li>`{=html}
`<ul>`{=html}`<li>`{=html}Threads in a core (CPU and
GPU)`</li>`{=html}`</ul>`{=html} `<ul>`{=html}`<li>`{=html}Cores within
a chip`</li>`{=html}`</ul>`{=html}\
`<ul>`{=html}`<li>`{=html}Pieces of hardware
`</li>`{=html}`</ul>`{=html}
`<ul>`{=html}`<pp>`{=html}`<i>`{=html}example: SLI bridge is a connector
and a protocol for such a
communication`</i>`{=html}`</pp>`{=html}`</ul>`{=html} `<p>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Bottlenecks beyond parallelism

-   DL training and inference do not take place solely on the
    accelerator.
    -   The accelerator accelerates the gradient computations and
        updates.
    -   The CPU will still need to be loading the data (model, train
        set) and saving the model (checkpointing).
-   The accelerator starves if it waits idly for its inputs due for
    example to slow CPU, I/O buses, or storage interface (SATA, SSD,
    NVMe).
:::

::: {.cell .code execution_count="11" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("starving GPUs")
print("show in-code what starving GPU looks like")
# Deliberately slow down data flow into the gpu 
# Do you have any suggestions how to do this in a more realistic way than just to force waiting?
print('Using only 1 worker for the dataloader, the time the GPU takes increases.')
lenet.cuda()
batch_size = 64
gpu_trainloader = make_MNIST_loader(batch_size=batch_size, num_workers=1)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')
```

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

::: {.output .stream .stderr}
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Plan for the Day {#plan-for-the-day}

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   **Data Movement and Bandwidth Pressures**
    -   **Deep Learning working set**
    -   **Mapping Deep Learning onto hardware**
    -   **Addressing memory pressure**
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Deep Learning resource characterisation
:::

::: {.cell .code execution_count="12"}
``` {.python}
print("profiling demo")
print("in-house DL training resource profiling code & output - based on the above model and training loop")
#for both of the below produce one figure for inference and one for training
#MACs profiling - first slide; show as piechard

lenet.cpu()
profile_ops(lenet, shape=(1,1,28,28))
```

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

::: {.output .display_data}
![](fa2e484acf0b3be23b09b17472a1346d6489ca12.png)
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Deep Learning working set

-   Working set - a collection of all elements needed for executing a
    given DL layer
    -   Input and output activations
    -   Parameters (weights & biases)
:::

::: {.cell .code execution_count="14" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("working set profiling")
# compute the per-layer required memory:
# memory to load weights, to load inputs, to save oputputs
# visualze as a per-layer bar chart, each bar consists of three sections - the inputs, outputs, weights

profile_layer_mem(lenet)
```

::: {.output .stream .stdout}
    working set profiling
:::

::: {.output .display_data}
![](af6e0bd6b0755f5ccb33f3a4845521ef02a83120.png)
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Working Set requirement exceeding RAM
:::

::: {.cell .code execution_count="15" scrolled="false" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("exceeding RAM+Swap demo")
print("exceeding working set experiment - see the latency spike over a couple of bytes of working set")
# sample* a training speed of a model whose layer working sets just first in the memory
# bump up layer dimensions which are far from reaching the RAM limit - see that the effect on latency is limited
# bump up the layer(s) that are at the RAM limit - observe the latency spike rapidly
# add profiling graphs for each of the cases, print out latency numbers.

# *train for an epoch or two, give the latency & give a reasonable estimate of how long would the full training take (assuming X epochs)
estimate_training_for(LeNet, 1000)
```

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

::: {.output .display_data}
![](7e50f30ae5d9101c770d18fd37f3f335e9107616.png)
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Working Set requirement exceeding RAM + Swap {#working-set-requirement-exceeding-ram--swap}
:::

::: {.cell .code execution_count="16" scrolled="true" slideshow="{\"slide_type\":\"-\"}"}
``` {.python}
print("OOM - massive images")
print("show in-code how this can hapen - say massive images; maybe show error message")
# How could we do this without affecting the recording process?
print('Loading too many images at once causes errors.')
lenet.cuda()
batch_size = 6000
gpu_trainloader = make_MNIST_loader(batch_size=batch_size, num_workers=1)
start = time()
gpu_train(lenet, gpu_trainloader)
print(f'GPU took {time()-start:.2f} seconds')
```

::: {.output .stream .stdout}
    OOM - massive images
    show in-code how this can hapen - say massive images; maybe show error message
    Loading too many images at once causes errors.
:::

::: {.output .stream .stderr}
    Epoch 1, iter 10, iter loss 0.596: : 10it [00:03,  2.78it/s]
    Epoch 2, iter 2, iter loss 0.592: : 2it [00:01,  1.69it/s]
:::

::: {.output .error ename="RuntimeError" evalue="DataLoader worker (pid(s) 7512) exited unexpectedly"}
    ---------------------------------------------------------------------------
    RuntimeError                              Traceback (most recent call last)
    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/dataloader.py in _try_get_data(self, timeout)
        871         try:
    --> 872             data = self._data_queue.get(timeout=timeout)
        873             return (True, data)

    ~/miniconda3/lib/python3.8/multiprocessing/queues.py in get(self, block, timeout)
        106                     timeout = deadline - time.monotonic()
    --> 107                     if not self._poll(timeout):
        108                         raise Empty

    ~/miniconda3/lib/python3.8/multiprocessing/connection.py in poll(self, timeout)
        256         self._check_readable()
    --> 257         return self._poll(timeout)
        258 

    ~/miniconda3/lib/python3.8/multiprocessing/connection.py in _poll(self, timeout)
        423     def _poll(self, timeout):
    --> 424         r = wait([self], timeout)
        425         return bool(r)

    ~/miniconda3/lib/python3.8/multiprocessing/connection.py in wait(object_list, timeout)
        929             while True:
    --> 930                 ready = selector.select(timeout)
        931                 if ready:

    ~/miniconda3/lib/python3.8/selectors.py in select(self, timeout)
        414         try:
    --> 415             fd_event_list = self._selector.poll(timeout)
        416         except InterruptedError:

    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/_utils/signal_handling.py in handler(signum, frame)
         65         # Python can still get and update the process status successfully.
    ---> 66         _error_if_any_worker_fails()
         67         if previous_handler is not None:

    RuntimeError: DataLoader worker (pid 7512) is killed by signal: Bus error. It is possible that dataloader's workers are out of shared memory. Please try to raise your shared memory limit.

    The above exception was the direct cause of the following exception:

    RuntimeError                              Traceback (most recent call last)
    <ipython-input-16-f2168c022c8c> in <module>
          7 gpu_trainloader = make_MNIST_loader(batch_size=batch_size, num_workers=1)
          8 start = time()
    ----> 9 gpu_train(lenet, gpu_trainloader)
         10 print(f'GPU took {time()-start:.2f} seconds')

    /home/niclane/custom_imports.py in gpu_train(net, trainloader, num_epochs)
         67 
         68         data_tqdm = tqdm.tqdm(enumerate(trainloader))
    ---> 69         for i, (inputs, labels) in data_tqdm:
         70             # zero the parameter gradients
         71             inputs = inputs.cuda()

    ~/miniconda3/lib/python3.8/site-packages/tqdm/std.py in __iter__(self)
       1165 
       1166         try:
    -> 1167             for obj in iterable:
       1168                 yield obj
       1169                 # Update and possibly print the progressbar.

    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/dataloader.py in __next__(self)
        433         if self._sampler_iter is None:
        434             self._reset()
    --> 435         data = self._next_data()
        436         self._num_yielded += 1
        437         if self._dataset_kind == _DatasetKind.Iterable and \

    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/dataloader.py in _next_data(self)
       1066 
       1067             assert not self._shutdown and self._tasks_outstanding > 0
    -> 1068             idx, data = self._get_data()
       1069             self._tasks_outstanding -= 1
       1070             if self._dataset_kind == _DatasetKind.Iterable:

    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/dataloader.py in _get_data(self)
       1032         else:
       1033             while True:
    -> 1034                 success, data = self._try_get_data()
       1035                 if success:
       1036                     return data

    ~/miniconda3/lib/python3.8/site-packages/torch/utils/data/dataloader.py in _try_get_data(self, timeout)
        883             if len(failed_workers) > 0:
        884                 pids_str = ', '.join(str(w.pid) for w in failed_workers)
    --> 885                 raise RuntimeError('DataLoader worker (pid(s) {}) exited unexpectedly'.format(pids_str)) from e
        886             if isinstance(e, queue.Empty):
        887                 return (False, None)

    RuntimeError: DataLoader worker (pid(s) 7512) exited unexpectedly
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Mapping Deep Models to hardware: Systolic Arrays

`<br/>`{=html}

```{=html}
<table><tr>
<td> <center> <h2> Core principle </h2> </center></td>
<td> <center> <h2> Systolic system matrix multiplication </h2> </center></td>
</tr>
<tr>
<td><center><img src=inputs/basic_systolic_system.png alt="Drawing" style="width: 900px;"/></center></td>
<td><center><video controls src="inputs/systolic_array.mp4" width="900"/></center></td>
</tr>
</table>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Mapping Deep Models to hardware: weight, input, and output stationarity

#### Weight stationary design

```{=html}
<center><img src=inputs/weight_stationary.png style="width: 900px;"/></center>
```
#### Input stationary design

```{=html}
<center><img src=inputs/input_stationary.png style="width: 900px;"/></center>
```
#### Output stationary design

```{=html}
<center><img src=inputs/output_stationary.png style="width: 900px;"/></center>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## Systolic array example: weight stationary Google Tensor Processing Unit (TPU)

`<br/>`{=html}

```{=html}
<center>
```
`<img src=inputs/provisional_TPU3.png alt="Drawing" style="width: 1200px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Plan for the Day {#plan-for-the-day}

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   **Closing messages**
    -   **Deep Learning stack**
    -   **Deep Learning and accelerator co-design**
    -   **The Hardware and the Software Lottery**
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Deep Learning stack

`<br/>`{=html}

```{=html}
<center>
```
`<img src=inputs/TVM_stack2.png alt="Drawing" style="width: 1700px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Beyond hardware methods

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Deep Learning and accelerator co-design

`<br/>`{=html} `<br/>`{=html}

```{=html}
<center>
```
`<img src=inputs/codesign.png alt="Drawing" style="width: 800px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## AlexNet: how GPU memory defined its architecture

-   Alex Krizhevsky used two GTX 580 GPUs, each with 3GB of memory.
-   Theoretical AlexNet (without mid-way split) working set profiling:
:::

::: {.cell .code execution_count="17" scrolled="false"}
``` {.python}
print("profile AlexNet layers - show memory requirements")
print("per-layer profiling of AlexNet - connects to the preceding slide")
from torchvision.models import alexnet as net
anet = net()
profile_layer_alexnet(anet)
```

::: {.output .stream .stdout}
    profile AlexNet layers - show memory requirements
    per-layer profiling of AlexNet - connects to the preceding slide
:::

::: {.output .display_data}
![](2371c2a192ef69113ac6e04527cd20ce276e13af.png)
:::
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"subslide\"}"}
## The actual AlexNet architecture

AlexNet\'s architecture had to be split down the middle to accommodate
the 3GB limit per unit in its two GPUs.

```{=html}
<center>
```
`<img src=inputs/AlexNet.png alt="Drawing" style="width: 1400px;"/>`{=html}
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Beyond hardware methods {#beyond-hardware-methods}

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
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## The Hardware and the Software Lotteries

`<br/>`{=html}

```{=html}
<center><b><i>The software and hardware lottery describes the success of a software or a piece of hardware <br/> resulting not from its universal superiority, but, rather, from its fit to the broader hardware and software ecosystem.</i></b></center>
```
`<br/>`{=html}

```{=html}
<table>

<tr>
<td> <center> <h2> Eniac (1950s) </h2> </center> </td>
<td> <center> <h2> All-optical NN (2019) </h2> </center> </td></tr>

<tr>
<td> <img src="inputs/Eniac.JPG" alt="Drawing" style="width: 800px;"/> </td>
<td> <img src="inputs/futureDL.png" alt="Drawing" style="width: 800px;"/> </td>
</tr>

</table>
```
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"slide\"}"}
## Summary of the Day

-   Introduction
-   Hardware Foundation
-   Parallelism Leveraging
-   Data Movement and Bandwidth Pressures
-   Closing messages
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
# Thank you for your attention!
:::

::: {.cell .markdown slideshow="{\"slide_type\":\"skip\"}"}
## Deep Learning resource characterisation {#deep-learning-resource-characterisation}
:::

::: {.cell .code execution_count="13" slideshow="{\"slide_type\":\"skip\"}"}
``` {.python}
#memory requirements profiling - second slide; show as piechard
# Show proportion of data required for input, parameters and outputs

profile_mem(lenet)
```

::: {.output .display_data}
![](11d23715eb81c04c09c465d3757cb818e4d44bfd.png)
:::
:::
