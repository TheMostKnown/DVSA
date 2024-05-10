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
    "xxe-task2": "sne{v3ry_v3ry_v3ry_f00l1sh_svg_sdjsjvj8372j}",
    "ssrf-task1": "sne{Th47_w4$_e@5y}",
    "ssrf-task2": "sne{b3773r_7h4n_my_Gr4ndm4}",
    "ssrf-task3": "sne{W3_r1ch}",
    "auth-task1": "cne{bru73_br0}",
    "auth-task2": "cne{1_l0v3_3471n6_c00k135}",
    "path-task1": "sne{y0u_570l3_my_53cr375}",
    "path-task2": "sne{1_l0v3_7h3_Sh1r3}",
    "path-task3": "sne{my_pr3c10u5}",
    "sqli-task1": "sne{where_was_@_simple_replacing}",
    "sqli-task2": "sne{uNiOn_request_is_@_bug}",
    "sqli-task3": "sne{buttons_@re_not_secure}",
    "access-task1": "sne{T00_e@sy_acce55_c0ntro1}",
    "access-task2": "sne{G1immer_secret}",
    "access-task3": "sne{Base64_not_4_encryption}",
    "file-task1": "sne{Too_simple_check_for_files}",
    "file-task2": "sne{This_0ne_w@s_0k}",
    "file-task3": "sne{Its_1ike_pu22le}"
    
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
