import bcrypt

# bcrypt 工作因子，决定哈希的复杂度，越高越安全但越慢
BCRYPT_ROUNDS = 12


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """验证密码是否匹配哈希值"""
    try:
        # bcrypt 需要字节类型输入
        plain_password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')

        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
    except Exception:
        # 如果发生任何异常（如格式错误），返回 False
        return False


def get_password_hash(password: str) -> str:
    """生成密码的哈希值"""
    # bcrypt 需要字节类型输入
    password_bytes = password.encode('utf-8')

    # 生成盐值并哈希密码
    salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    hashed = bcrypt.hashpw(password_bytes, salt)

    # 将结果转换回字符串
    return hashed.decode('utf-8')
