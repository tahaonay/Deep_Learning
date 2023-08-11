import torch
import numpy as np


#%% scalar->vector->matrix->tensor

scalar = torch.tensor(7)
print(scalar)
print(scalar.ndim)

vector = torch.tensor([7,7])
print(vector)
print(vector.ndim)

matrix = torch.tensor([[1,2],[3,4]])
print(matrix)
print(matrix.ndim)
print(matrix.shape)

tensor = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]]])
print(tensor)
print(tensor.ndim)
print(tensor.shape)

#%% Random zeros-ones range 
random_tensor = torch.rand(3,4)    # create random tensor (2 dimension)
print(random_tensor)

random_image_size_tensor = torch.rand(size=(224,224,3)) # heigt,width,color channels
print(random_image_size_tensor.shape)     # gives tensor shape    like [224,223,3]
print(random_image_size_tensor.ndim)      # gives tensor dimesion  2,3 etc

print(random_tensor.dtype)                # gives data type (tensor default float32)

# Zeros and Ones
zero = torch.zeros(3,4)
print(zero)

one = torch.ones(4,4)
print(one)

# Range - arange
zero_to_ten = torch.range(0,10)
print(zero_to_ten)

step_range = torch.arange(start=0, end=100, step=5)
print(step_range)

# like
zero_ten = torch.zeros_like(input=zero_to_ten) 
print(zero_ten)

#%% Data Types      tensor.dtype, tensor.shape,  tensor.device
# float32
float_32 = torch.tensor([3.0, 6.0, 9.0], dtype=None)
print(float_32)

float_16_tensor = float_32.type(torch.float16)
print(float_16_tensor)


multi= float_16_tensor*float_32   # float16 * float32 
print(multi)

int_32 = torch.tensor([3, 6, 9],dtype=torch.int32)
print(int_32)

multi2= int_32*float_32           # int32 * float32
print(multi2)
print(float_32.device)
#%% Tensor Operations
tensor = torch.tensor([1,2,3])

# addition
tensor_add= tensor+10
print(tensor_add)

# substraction
tensor_sub= tensor -5
print(tensor_sub)

# Multiplication
tensor_mul= tensor*2
print(tensor_mul)

# Division
tensor_div= tensor /3
print(tensor_div)

# matrix multiplication
element_wise = tensor*tensor                 # (1*1, 2*2, 3*3)
print(element_wise)

matrix_mul = torch.matmul(tensor, tensor)    # (1*1 + 2*2 + 3*3)
print(matrix_mul)

# Transpose    tensor.T
tensor2 = torch.tensor([[7,8,9],[10,11,12]])
print(tensor2)
tensor_transpose = tensor2.T 
print(tensor_transpose)

#%% min, max, mean, sum,vs
tensor = torch.arange(1,100,10)
print(tensor)

x_min = tensor.min()    # torch.min(tensor)
x_max = tensor.max()    # torch.max(tensor)
x_mean = tensor.type(torch.float32).mean()  # torch.mean(tensor.type(torch.float32))
x_sum = tensor.sum()    # torch.sum(tensor)
 
print(f"min: {x_min} , max: {x_max} , mean: {x_mean} , sum: {x_sum}")

# positional min, max

min_pos = tensor.argmin()
max_pos = tensor.argmax()

print(f"min pos: {min_pos}, max pos: {max_pos}")

#%% Reshaping, stacking, squeezing, unsqueezing
x = torch.arange(1.,10.)
print(x.shape)

# add an extra dimesinon   [1x9] --> [[1x9]]
x_reshaped = x.reshape(1,9)
x_reshaped2 = x.reshape(9,1)
print(x_reshaped)
print(x_reshaped2)

#  1x12 --> 4x3
x = torch.arange(1.,13.)
x_reshaped3 = x.reshape(4,3)
print(x_reshaped3)

# change the view
x = torch.arange(1.,10.)
z = x.view(1,9)
z.shape

z[:,0] = 4   # z and x shares same memory so changes together
print(z,x)


# stack tensors on top of each other
x_stacked = torch.stack([x,x,x,x],dim=0)   # dim,  0 = horizontal, 1=vertical
print(x_stacked)

# squeeze  removes all single dimension
x_squeezed= x_reshaped.squeeze()
print(f"Previous tensor:\n{x_reshaped}")
print(f"New tensor: \n{x_squeezed}")
print(f"\nPrevious size: {x_reshaped.size()} \n\t New size: {x_squeezed.size()}")

# unsqueeze  add a single dimension
x_unsqueezed = x_squeezed.unsqueeze(dim=0)  # dim=0  (9) --> (1,9)  add 0.index
print(f"Previous tensor:\n{x_squeezed}")
print(f"New tensor: \n{x_unsqueezed}")
print(f"\nPrevious size: {x_squeezed.size()} \n\t New size: {x_unsqueezed.size()}")

x_unsqueezed = x_squeezed.unsqueeze(dim=1)  # dim=1  (9) -->  (9,1)  add 1.index
print(f"Previous tensor:\n{x_squeezed}")
print(f"New tensor: \n{x_unsqueezed}")
print(f"\nPrevious size: {x_squeezed.size()} \n\t New size: {x_unsqueezed.size()}")


# permute   changes dimension index

x_original = torch.rand(size=(224,224,3)) # height, width, color_channel
x_permuted = x_original.permute(2,0,1)  # shift axis 2->0, 0->1, 1->2
print(x_original.shape)
print(x_permuted.shape)

#%% indexing      ":" = select all of a target dimension
x = torch.arange(1,10).reshape(1,3,3)     # x[][][]   
first_dimension = x[0]
first_raw = x[0][0]   # x[0,0]
first_item = x[0][0][0]
print(first_item)

second_raw = x[:,1]
print(second_raw)

firts_column = x[:,:,0]
print(firts_column)

last_column = x[:,:,2]
print(last_column)

item = x[:,1,1]     # with []   
item2 = x[0][1][1]  # without []



print(item,item2)

#%% Numpy
 # numpy--> tensor
array = np.arange(1.0,8.0)  # default "float64"
tensor = torch.from_numpy(array).type(torch.float32)
print(array, array.dtype)
print(tensor, tensor.dtype)

array = array + 1

print(array)
print(tensor)

 # tensor --> numpy
tensor= torch.ones(7)
numpy_tensor = tensor.numpy()
print(tensor, tensor.dtype)
print(numpy_tensor, numpy_tensor.dtype)

#%%  random   reproducibility
random_seed = 42  # set random seed
torch.manual_seed(random_seed)    # everythime you use, you must called one time
random_tensor_c = torch.rand(3,4)
torch.manual_seed(random_seed)    # everythime you use, you must called one time
random_tensor_d = torch.rand(3,4)
print(random_tensor_c)
print(random_tensor_d)
print(random_tensor_c == random_tensor_d)

#%% using GPU
# information
version = torch.version.cuda
access = torch.cuda.is_available()

print(f"Version : {version}")
print(f"Access : {access} ")

# cuda or cpu
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

# device count 
count = torch.cuda.device_count()

# Create a tensor (default on the CPU)
tensor = torch.tensor([1,2,3])
print(tensor, tensor.device)

# move to GPU
tensor_GPU = tensor.to(device)
print(tensor_GPU)

# move to CPU
tensor_CPU = tensor.cpu()
print(tensor_CPU, tensor_CPU.device)
