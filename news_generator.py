# -*- coding: utf-8 -*-
"""News_Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/102XLAFd34V76B6i1nZMZgPOVYdtEiXXw

Run this to install the neccasary depenedices and packages.
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 1.x
!pip install -q gpt-2-simple
import gpt_2_simple as gpt2
from datetime import datetime
from google.colab import files

"""Connect your Google Drive"""

from google.colab import drive
drive.mount('/content/drive')

"""Download the 355 million parameter version of GPT2. (The best you can use on Colaboratory) Then mount the Google drive"""

gpt2.download_gpt2(model_name="355M")
gpt2.mount_gdrive()

"""You must have a filename in your drive called output.txt (You can find mine in the GitHub repo). This grabs the content from it"""

file_name = "output.txt"
gpt2.copy_file_from_gdrive(file_name)
sess = gpt2.start_tf_sess()

"""Here the nueral network is being trained"""

gpt2.finetune(sess,
              dataset=file_name,
              model_name='355M',
              steps=2000,
              restore_from='fresh',
              run_name='run1',
              print_every=25,
              sample_every=35,
              save_every=100
              )

"""Save the trained weights and biases"""

gpt2.copy_checkpoint_to_gdrive(run_name='run1')

"""Generate an entry"""

gpt2.generate(sess,
              length=250,
              temperature=1,
              prefix="<|startoftext|>",
              nsamples=5,
              batch_size=5, 
              )