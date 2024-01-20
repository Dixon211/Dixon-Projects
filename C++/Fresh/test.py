
def decode(message_file):
        text = open(message_file, "r", encoding="utf-8").read().split("/n")
        decoder_dictionary = {}
        for i in text:
                i = i.split()
                decoder_dictionary[int(i[0])].append(i[1])
        

        pyramid_nums = []
        for key in decoder_dictionary.keys():
                pyramid_nums.append(key)


        pyramid_nums = sorted(pyramid_nums)
        steps = 1
        layers = []
        while len(pyramid_nums) != 0:
                if len(pyramid_nums) >= steps:
                    layers.append(pyramid_nums[0:steps])
                    pyramid_nums = pyramid_nums[steps:]
                    steps += 1
                else:
                       break
        
        message = ""
        for layer in layers:
               x = layer[-1]
               message = message + decoder_dictionary[x] + " "
        
        return message
                    
                
                



        
                
        return True