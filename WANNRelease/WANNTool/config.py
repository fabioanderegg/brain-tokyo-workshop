from collections import namedtuple

Game = namedtuple('Game', ['env_name', 'input_size', 'output_size', 'wann_file', 'action_select', 'weight_bias'])

games = {}

cartpole_swingup = Game(env_name='CartPoleSwingUp',
  input_size=5,
  output_size=1,
  wann_file='swing.out',
  action_select='all', # all, soft, hard
  weight_bias=-1.5,
)
games['cartpole_swingup'] = cartpole_swingup

biped = Game(env_name='BipedalWalker-v2',
  input_size=24,
  output_size=4,
  wann_file='biped.out',
  action_select='all', # all, soft, hard
  weight_bias=-1.87,
)
games['biped'] = biped

bipedhard = Game(env_name='BipedalWalkerHardcore-v2',
  input_size=24,
  output_size=4,
  wann_file='biped.out',
  action_select='all', # all, soft, hard
  weight_bias=-1.87,
)
games['bipedhard'] = bipedhard

vae_racing = Game(env_name='VAERacing-v0',
  input_size=16,
  output_size=3,
  wann_file='racer.out',
  action_select='all', # all, soft, hard
  weight_bias=-0.7,
)
games['vae_racing'] = vae_racing

mnist256 = Game(env_name='MNIST256-v0',
  input_size=256,
  output_size=10,
  wann_file='mnist.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnist256'] = mnist256

# evaluate on the test set
mnist256test = Game(env_name='MNISTTEST256-v0',
  input_size=256,
  output_size=10,
  wann_file='mnist.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnist256test'] = mnist256test

# evaluate on the training set
mnist256train = Game(env_name='MNISTTRAIN256-v0',
  input_size=256,
  output_size=10,
  wann_file='mnist.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnist256train'] = mnist256train


# evaluate on the test set
mnist784test = Game(env_name='MNISTTEST784-v0',
  input_size=784,
  output_size=10,
  wann_file='mnist784_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnist784test'] = mnist784test

# evaluate on the training set
mnist784train = Game(env_name='MNISTTRAIN784-v0',
  input_size=784,
  output_size=10,
  wann_file='mnist784_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnist784train'] = mnist784train

# evaluate on the test set
mnistfeaturestest = Game(env_name='MNISTTESTFEATURES-v0',
  input_size=20,
  output_size=10,
  wann_file='mnist_features_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnistfeaturestest'] = mnistfeaturestest

# evaluate on the training set
mnistfeaturestrain = Game(env_name='MNISTTRAINFEATURES-v0',
  input_size=20,
  output_size=10,
  wann_file='mnist_features_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnistfeaturestrain'] = mnistfeaturestrain

# evaluate on the test set
mnistautoencodertest = Game(env_name='MNISTTESTAUTOENCODER-v0',
  input_size=32,
  output_size=10,
  wann_file='mnist_autoencoder_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnistautoencodertest'] = mnistautoencodertest

# evaluate on the training set
mnistautoencodertrain = Game(env_name='MNISTTRAINAUTOENCODER-v0',
  input_size=32,
  output_size=10,
  wann_file='mnist_autoencoder_best.out',
  action_select='softmax', # all, soft, hard
  weight_bias=0.0,
)
games['mnistautoencodertrain'] = mnistautoencodertrain
