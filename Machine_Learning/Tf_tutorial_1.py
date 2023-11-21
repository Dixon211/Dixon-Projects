import tensorflow as tf
import numpy as np

# creates a zero dimension tensor, a tensor of just 1 number, the number is 4
tensor_zero_d = tf.constant(4)

#creates a tensor with no shape, with the data type: integer, the int is 4
tf.Tensor(4, shape=(), dtype=int)

#creates a one-dimension tensor, a list
tensor_one_d=tf.constant([2, 0, -3])

# a 2-dimension tensor, a matrix
tensor_two_d = tf.constant([
    [1, 2, 0],
    [3, 5, -1],
    [1, 5, 6],
    [2, 3, 8],
    ])

# a 3-d tensor, print allows you to see dimensions
tensor_three_d =tf.constant([
    [[1, 2, 0],
     [3, 5, -1]],

     [[10, 2, 0],
     [1, 0, 2]],

     [[5, 8, 0],
      [2, 7, 0]],

    [[2, 1, 9],
     [4, -3, 32]]

    ])

tensor_four_d = tf.constant([
    [[[1, 2, 0],
    [3, 5, -1]],

    [[10, 2, 0],
    [1, 0, 2]],

    [[5, 8, 0],
    [2, 7, 0]],

    [[2, 1, 9],
    [4, -3, 32]]],

    [[[4, 5, 4],
    [3, 1, 1]],

    [[0,2,5],
    [0,4,3]],

    [[3,2,4],
     [5,8,3]],

     [[8, 2, 5],
      [2,3,3]]],
      [[[0,2,5],
        [5,3,1]],
        
    [[0,2,0],
    [-1, 10, 0]],
         
    [[0, 5, 1],
     [1,7,0]],

     [[3, 8, 7],
      [2, 3, 2]]]
])

#how to convert numpy array to tensor
np_array = np.array([1, 2, 4])
np_converted_to_tensor = tf.convert_to_tensor(np_array)

# eye tensor, creates diagonal tensor
eye_tensor = tf.eye(
    num_rows=3,
    num_columns=None,
    batch_shape=None,
    dtype=tf.dtypes.float32,
    name=None
)

#print(3*eye_tensor)

# fill tensor, creates a tensor with a single scalar in all positions
fill_tensor = tf.fill(
    [3, 4], 5, name = None
)

#print(fill_tensor)