from flask import Flask, jsonify, request

app = Flask(__name__)

# 假設有一個初始的使用者列表
users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Mary'}]
next_id = 3

# 查詢使用者
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# 新增使用者
@app.route('/users', methods=['POST'])
def add_user():
    global next_id
    user = request.get_json()
    user['id'] = next_id
    next_id += 1
    users.append(user)
    return jsonify(user), 201

# 修改使用者
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# 刪除使用者
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user:
        users.remove(user)
        return '', 204
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run()
