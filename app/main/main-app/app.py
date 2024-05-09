from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main_app():
    return (render_template('index.html'))
    
    
# Dictionary to store correct flags for each task
correct_flags = {
    "bl-task1": "sne{y0u_4r3_d1sc0unt_4bus3r_u72hd9ao0}",
    "bl-task2": "sne{0h_n0_y0u_h4v3_0v3rfl0w3d_my_c4rt_os8sdfy40df9}",
    "bl-task3": "sne{0h_l00k_h3r3_1s_4_g1ft_c0d3_3nj03r_sdas89s8df7}",
    "id-task1": "sne{g0thc4_th3_fl4g_1s_y0urs_ac4e0693bb}",
    "id-task2": "sne{0k_1_b3l31ve_th4t_y0u_4r3_4dmin_201dc6546c}",
    "id-task3": "sne{g00d_yuv3_r34ch3d_rc3_asd8f79asdf87}",
    "xxe-task1": "sne{p0k3m0ns_4r3_gr34t_asjdlxcovs8dfs7dfhvc}",
    "xxe-task2": "sne{v3ry_v3ry_v3ry_f00l1sh_svg_sdjsjvj8372j}"
}

@app.route('/check_flag', methods=['POST'])
def check_flag():
    data = request.json
    task_id = data.get('task_id', '')
    flag = data.get('flag', '')

    # Validate the flag for the corresponding task
    correct_flag = correct_flags.get(task_id)
    is_correct = flag == correct_flag

    return jsonify({'is_correct': is_correct})

if __name__ == 'main':
  app.run(debug=True, host='0.0.0.0', port=80)
