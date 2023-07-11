import os

input_dir = '/Users/daiyi/work/ramp/BeamformIt/data'
beam_dir = '/Users/daiyi/work/ramp/BeamformIt/output'
os.makedirs(beam_dir, exist_ok=True)

cmd1 = '''
./BeamformIt \
    --scroll_size 250 \
    --window_size 500 \
    --nbest_amount 4 \
    --do_noise_threshold 1 \
    --noise_percent 10 \
    --trans_weight_multi 25 \
    --trans_weight_nbest 25 \
    --print_features 1 \
    --do_avoid_bad_frames 1 \
    --do_compute_reference 0 \
    --reference_channel 3 \
    --do_use_uem_file 0 \
    --do_adapt_weights 1 \
    --do_write_sph_files 1 \
    --channels_file {} \
    --show_id {} \
    --result_dir {}
'''

cmd2 = '''
cp ./output/{}/{} {}
'''

cmd3 = "rm {}"

for file in os.listdir(input_dir):
    ext = file.split(".")[-1]
    if ext != "wav":
        continue
    
    if len(file.split(".")) > 2:
        f_name = '.'.join(file.split(".")[:-1])
    else:
        f_name = file.split(".")[0]
    print(cmd1.format(input_dir + '/'+ file, f_name, beam_dir))
    os.system(cmd1.format(input_dir + '/'+ file, f_name, beam_dir))
    for i in range(8):
        extra = beam_dir + '/'+ f_name + '_f0_ch' + str(i) + '.wav' 
        os.system(cmd3.format(extra))
