import gpt_2_simple as gpt2

model_name = "124M"
# gpt2.download_gpt2(model_name=model_name)

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

gpt2.generate(sess,
              length=100,
              temperature=1.5,
              nsamples=10,
              batch_size=10,
              )
