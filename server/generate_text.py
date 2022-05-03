import gpt_2_simple as gpt2


class Generator:
    def __init__(self):
        self.model_name = "124M"
        # gpt2.download_gpt2(model_name=model_name)

        self.sess = gpt2.start_tf_sess(threads=1)
        gpt2.load_gpt2(self.sess, run_name="run1")

    def generate(self, length, temprature, prefix):
        return gpt2.generate(self.sess,
                             length=length,
                             temperature=temprature,
                             nsamples=1,
                             batch_size=1,
                             return_as_list=True,
                             prefix=prefix
                             )[0]


# sess = setup()
# for i in range(10):
#     print(generate(sess))
#     print("=================")
# print("======== Other Generation ==========")

# gpt2.generate(sess,
#               length=50,
#               temperature=1,
#               nsamples=10,
#               batch_size=10,
#               prefix="<|startoftext|>",
#               truncate="<|endoftext|>",
#               include_prefix=False,
#               )
