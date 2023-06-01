import numpy as np

def winograd_3x3_conv(input_tensor, filter_weights):
    # Input tensor dimensions
    N, H, W, C = input_tensor.shape

    # Calculate output dimensions
    output_H = H - 2
    output_W = W - 2

    # Transform filter weights to Winograd domain
    G = np.array([[1, 0, 0], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5], [0, 0, 1]])
    transformed_filters = np.dot(G, np.dot(filter_weights, np.transpose(G)))

    # Initialize output tensor
    output_tensor = np.zeros((N, output_H, output_W, C))

    # Loop over each input tensor
    for n in range(N):
        # Loop over each channel
        for c in range(C):
            # Extract input tensor and transformed filter weights for the current channel
            input_channel = input_tensor[n, :, :, c]
            transformed_filter_channel = transformed_filters[:, :, c]

            # Perform Winograd convolution
            transformed_input = np.dot(np.transpose(G), np.dot(input_channel, G))
            transformed_output = np.dot(transformed_input, transformed_filter_channel)

            # Transform output back to the spatial domain
            output_channel = np.dot(np.transpose(G), np.dot(transformed_output, np.transpose(G)))
            output_tensor[n, :, :, c] = output_channel[1:-1, 1:-1]

    return output_tensor



def pool_naive(x):
    N, C, H, W = x.shape
    H1 = (H - Hp) // S + 1
    W1 = (W - Wp) // S + 1

    out = np.zeros((N, C, H1, W1))

    

if __name__ == "__main__":
    photos = np.load('dogs_vs_cats_photos.npy')
    labels = np.load('dogs_vs_cats_labels.npy')

    train_photos = photos[0:7500]
    train_labels = labels[0:7500]

    test_photos = photos[7500:10000]
    test_labels = labels[7500:10000]

    print(test_photos.shape)