#!/bin/python3

# -*- coding: utf-8 -*-

if __import__('sys').version_info < (3, 9):raise MemoryError

try:

    import ast, random, base64, zlib, lzma, marshal, struct, time, sys, secrets, textwrap, os, uuid, unicodedata, hashlib

    from ast import *

    from getpass import getpass

except:pass



text = """ ▄▄▄·▄▄▄         ▐▄▄▄▄▄▄ . ▄▄· ▄▄▄▄▄
▐█ ▄█▀▄ █·▪       ·██▀▄.▀·▐█ ▌▪•██
 ██▀·▐▀▀▄  ▄█▀▄ ▪▄ ██▐▀▀▪▄██ ▄▄ ▐█.▪  __OBF__: ProJect
▐█▪·•▐█•█▌▐█▌.▐▌▐▌▐█▌▐█▄▄▌▐███▌ ▐█▌·  __Author__: khangcoder X thảo my coder
.▀   .▀  ▀ ▀█▄▀▪ ▀▀▀• ▀▀▀ ·▀▀▀  ▀▀▀   __In4__: (https://www.facebook.com/profile.php?id=61593602324700)
"""


sys.setrecursionlimit(99999999)

ver = f"{sys.version_info.major}.{sys.version_info.minor}"



try:

    import textwrap

    from getpass import getpass

    from pystyle import *

except ModuleNotFoundError:

    print('>> Installing Module')

    __import__('os').system(f'{__import__("sys").executable} -m pip install pystyle --quiet')

    from pystyle import *



System.Clear()



try:

    if hasattr(sys.stdout, 'reconfigure'):

        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    if hasattr(sys.stderr, 'reconfigure'):

        sys.stderr.reconfigure(encoding='utf-8', errors='replace')

except: pass



def banner():

    try:

        a=Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text)

        for i in range(len(a)):

            try:

                sys.stdout.write(a[i])

                sys.stdout.flush()

            except: pass

    except: pass

banner()



_used_var_names = set()



def _gen_unique_id(generator_func):

    for _ in range(10000):

        res = generator_func()

        if res not in _used_var_names:

            _used_var_names.add(res)

            return res

    res = f"Ox{uuid.uuid4().hex}"

    _used_var_names.add(res)

    return res



_hiragana_pool = [chr(i) for i in range(0x3041, 0x3097) if chr(i).isprintable() and chr(i).isidentifier()]

_katakana_pool = [chr(i) for i in range(0x30A1, 0x30FA) if chr(i).isprintable() and chr(i).isidentifier()]

_egyptian_pool = [chr(i) for i in range(0x13000, 0x13020) if chr(i).isprintable() and chr(i).isidentifier()]

_hangul_pool = [chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()]



def rname():return _gen_unique_id(lambda: f"Ox{uuid.uuid4().hex[:7].upper()}")

def rb():return _gen_unique_id(lambda: ''.join(random.choices(_hiragana_pool, k=12)))

def rb1():return _gen_unique_id(lambda: f"Ox{uuid.uuid4().hex[:8].upper()}")

def rb2():return _gen_unique_id(lambda: ''.join(random.choices(_katakana_pool, k=12)))

def rb3():return _gen_unique_id(lambda: 'Yuki_Abi' + ''.join(random.choices(_egyptian_pool, k=5)))

def rb4():return _gen_unique_id(lambda: ''.join(random.choices(_hangul_pool, k=11)))

def rb5():return _gen_unique_id(lambda: ''.join(random.choices(_hangul_pool, k=8)))

def rbx():return ('decㅤcáiㅤlồnㅤmẹㅤmày'+''.join(random.choices("?3..4thg = c,2a.ã.45$@dau = buoi?3..4c,2a.ã.45$@.4__khangcoder_..12.44.124.6", k=24)))

def superrandom():return ''.join(__import__('random').choices([chr(i) for i in range(1000, 3000)], k=16))

# DYNAMIC RANDOM OFFSETS (Fix Bug #9: eliminates static fingerprint constants)

_DYNAMIC_OFFSET_1 = secrets.randbits(58) + 10**16

_DYNAMIC_OFFSET_2 = secrets.randbits(60) + 10**17



# ============ YUKI HARDENING CORE (fix BUG #1/#2/#4/#5/#8/#18) ============

# Per-build random secrets: magic + stream constants + master keys.

# Every obfuscation run gets fresh values -> no static fingerprint to grep.

try:

    import hashlib as _hashlib_hard

except Exception:

    _hashlib_hard = None

_YUKI_SM_MAGIC = random.randint(0x1000, 0xFFFF)

_YUKI_SM_K1_MUL = random.choice([0x9E3779B9, 0x85EBCA6B, 0xC2B2AE35, 0x27D4EB2F, 0x165667B1, 0x1B873593])

_YUKI_SM_K1_ADD = random.randint(0x10000000, 0x7FFFFFFF)

_YUKI_SM_K2_MUL = random.choice([0xC2B2AE35, 0x9E3779B9, 0x85EBCA6B, 0x97E30D6D])

_YUKI_SM_K2_ADD = random.randint(0x10000000, 0x7FFFFFFF)

_YUKI_HVM_K = random.randint(0x10000000, 0x7FFFFFFF)

_YUKI_HVM_K2 = random.randint(0x10000000, 0x7FFFFFFF)

_YUKI_HVM_PEPPER = secrets.token_bytes(32)

_YUKI_HVM_WRAP_SALT = secrets.token_bytes(16)

_YUKI_HVM_EPOCH = random.choice((5, 6, 7, 8, 9, 10, 11, 12, 13))

_YUKI_HVM_UNWRAP_FN = '_hvmU'

_YUKI_URL_XOR = random.randint(1, 255)

_YUKI_URL_ROT = random.randint(1, 94)

_YUKI_BUILD_PEPPER = secrets.token_hex(16)

_YUKI_SM_SEED_SALT = secrets.token_hex(8)

_YUKI_INTEGRITY_SALT = random.randint(0x10000000, 0x7FFFFFFF)

_YUKI_HEARTBEAT_SECRET = random.randint(0x10000000, 0x7FFFFFFF)

_DEQUY_CACHE = {}





def _yuki_sha256(data: bytes) -> str:

    try:

        import hashlib as _h

        return _h.sha256(data).hexdigest()

    except Exception:

        # fallback: adler as hex (never empty)

        try:

            import zlib as _z

            return format(_z.adler32(data) & 0xFFFFFFFF, '08x') * 8

        except Exception:

            return '00' * 32





def _yuki_frag_bytes_expr(data: bytes, max_chunk: int = 128) -> str:

    """Return polymorphic out-of-order shuffled dict expr (no contiguous blob, ultra-fragmented)."""

    if not data:

        return "b''"

    if len(data) <= 16:

        return repr(data)

    min_chunk = max(16, max_chunk // 3) if max_chunk >= 48 else 8

    chunks = []

    i = 0

    while i < len(data):

        n = random.randint(min_chunk, max_chunk)

        chunks.append(data[i:i + n])

        i += n

    if len(chunks) == 1:

        return repr(chunks[0])

    salt = random.randint(0x10000000, 0x7FFFFFFF)

    shuffled = list(range(len(chunks)))

    random.shuffle(shuffled)

    dict_items = [f"{idx ^ salt}:{repr(chunks[idx])}" for idx in shuffled]

    _vd = '_Ox' + uuid.uuid4().hex[:6]

    _vs = '_Ox' + uuid.uuid4().hex[:6]

    _vn = '_Ox' + uuid.uuid4().hex[:6]

    _vi = '_Ox' + uuid.uuid4().hex[:6]

    return f"(lambda {_vd}, {_vs}, {_vn}: b''.join({_vd}[{_vi} ^ {_vs}] for {_vi} in range({_vn})))({{{','.join(dict_items)}}}, {salt}, {len(chunks)})"





def _yuki_chr_expr(s: str) -> str:

    """Hide a short ascii string as chr() arithmetic (anti-grep)."""

    if not s:

        return "''"

    k = random.randint(1, 32)

    elems = ','.join(f'(chr({ord(c) ^ k}^{k}))' for c in s)

    # join via empty chr-built string to avoid literal ''

    return f"''.join([{elems}])"





def _yuki_opaque_int(n: int) -> str:

    """Arithmetic/lambda expr that evaluates to n. Lambdas block const-fold."""

    n = int(n) & 0xFFFFFFFF

    a = random.randint(1, 0x7FFFFFFF)

    b = random.randint(1, 0x7FFF)

    mode = random.randint(0, 2)

    if mode == 0:

        return f'(lambda _a,_b:_a^_b)({n ^ a},{a})'

    if mode == 1:

        return f'(lambda _a,_b:(_a+_b)&0xFFFFFFFF)({(n - b) & 0xFFFFFFFF},{b})'

    return f'(lambda _a,_b:(_a-_b)&0xFFFFFFFF)({(n + a) & 0xFFFFFFFF},{a})'





def _yuki_opaque_bytes_expr(data: bytes) -> str:

    """Rebuild bytes from opaque uint32s. No bytes/b85 key blob in source."""

    if not data:

        return "b''"

    pad = (-len(data)) % 4

    raw = data + (b'\x00' * pad)

    chunks = []

    for i in range(0, len(raw), 4):

        n = int.from_bytes(raw[i:i + 4], 'big')

        chunks.append(f'({_yuki_opaque_int(n)}).to_bytes(4,"big")')

    joined = '+'.join(chunks)

    if pad:

        return f'({joined})[:{len(data)}]'

    return f'({joined})'





def _yuki_refresh_hvm_secrets():

    """Fresh rotating secrets per obfuscation run (never a static key in source)."""

    global _YUKI_HVM_K, _YUKI_HVM_K2, _YUKI_HVM_PEPPER, _YUKI_HVM_WRAP_SALT, _YUKI_HVM_EPOCH

    _YUKI_HVM_K = random.randint(0x10000000, 0x7FFFFFFF)

    _YUKI_HVM_K2 = random.randint(0x10000000, 0x7FFFFFFF)

    _YUKI_HVM_PEPPER = secrets.token_bytes(32)

    _YUKI_HVM_WRAP_SALT = secrets.token_bytes(16)

    _YUKI_HVM_EPOCH = random.choice((5, 6, 7, 8, 9, 10, 11, 12, 13))





def _yuki_hvm_epoch_block(seed, epoch_id, pepper: bytes, k_mul, k_add) -> bytes:

    hlib = _hashlib_hard

    if hlib is None:

        import hashlib as hlib

    h = hlib.sha256()

    h.update((int(seed) & 0xFFFFFFFFFFFFFFFF).to_bytes(8, 'big'))

    h.update((int(epoch_id) & 0xFFFFFFFF).to_bytes(4, 'big'))

    h.update(pepper)

    h.update((int(k_mul) & 0xFFFFFFFF).to_bytes(4, 'big'))

    h.update((int(k_add) & 0xFFFFFFFF).to_bytes(4, 'big'))

    return h.digest()





def _yuki_hvm_ins_keys(block: bytes, idx: int, num_ops: int):

    """Unique (k_op, k_arg) per instruction; material rotates every epoch."""

    w0 = int.from_bytes(block[0:4], 'big')

    w1 = int.from_bytes(block[4:8], 'big')

    w2 = int.from_bytes(block[8:12], 'big')

    w3 = int.from_bytes(block[12:16], 'big')

    w4 = int.from_bytes(block[16:20], 'big')

    w5 = int.from_bytes(block[20:24], 'big')

    w6 = int.from_bytes(block[24:28], 'big')

    mix = (w0 ^ (((idx + 1) * w1 + w2) & 0xFFFFFFFF)) & 0xFFFFFFFF

    mix2 = (w3 ^ (((idx + 3) * w4 + w2) & 0xFFFFFFFF)) & 0xFFFFFFFF

    mix = (mix ^ ((mix2 << 7) & 0xFFFFFFFF) ^ (mix2 >> 3)) & 0xFFFFFFFF

    k_op = (mix & 0xFF) % num_ops if num_ops else 0

    k_arg = (mix2 ^ ((((idx + 1) * w5) + w6) & 0xFFFFFFFF)) & 0xFFFFFFFF

    return k_op, k_arg





def _yuki_hvm_ctr_xor(data: bytes, pepper: bytes, salt: bytes) -> bytes:

    """SHA256-CTR wrap. Keystream block changes every 32 bytes — no stored XOR key."""

    hlib = _hashlib_hard

    if hlib is None:

        import hashlib as hlib

    out = bytearray(len(data))

    pos = 0

    ctr = 0

    while pos < len(data):

        blk = hlib.sha256(pepper + salt + ctr.to_bytes(4, 'big')).digest()

        n = min(32, len(data) - pos)

        for j in range(n):

            out[pos + j] = data[pos + j] ^ blk[j]

        pos += n

        ctr += 1

    return bytes(out)





def _yuki_b85_frag_expr(data: bytes, min_chunk: int = 64, max_chunk: int = 192) -> str:

    """b85 blob split into out-of-order shuffled polymorphic chunks joined at runtime."""

    try:

        import base64 as _b64

        txt = _b64.b85encode(data).decode('ascii')

    except Exception:

        txt = ''

    if not txt:

        return "''"

    chunks = []

    i = 0

    while i < len(txt):

        n = random.randint(min_chunk, max_chunk)

        chunks.append(txt[i:i + n])

        i += n

    if len(chunks) == 1:

        return repr(chunks[0])

    salt = random.randint(0x10000000, 0x7FFFFFFF)

    shuffled = list(range(len(chunks)))

    random.shuffle(shuffled)

    dict_items = [f"{idx ^ salt}:{repr(chunks[idx])}" for idx in shuffled]

    _vd = '_Ox' + uuid.uuid4().hex[:6]

    _vs = '_Ox' + uuid.uuid4().hex[:6]

    _vn = '_Ox' + uuid.uuid4().hex[:6]

    _vi = '_Ox' + uuid.uuid4().hex[:6]

    return f"(lambda {_vd}, {_vs}, {_vn}: ''.join({_vd}[{_vi} ^ {_vs}] for {_vi} in range({_vn})))({{{','.join(dict_items)}}}, {salt}, {len(chunks)})"





def _compile_secure(src: str, filename: str = 'ProJect', mode: str = 'exec'):

    """Always reorder future-imports to top before compile (fix BUG #14)."""

    try:

        src = _fix_future_imports_src(src)

    except Exception:

        pass

    try:

        tree = ast.parse(src)

        try:

            tree = _fix_future_in_ast(tree)

        except Exception:

            pass

        ast.fix_missing_locations(tree)

        return compile(tree, filename, mode)

    except SyntaxError as _e:

        if 'from __future__' in str(_e):

            try:

                lines = src.splitlines()

                fut = [l for l in lines if l.strip().startswith('from __future__')]

                rest = [l for l in lines if not l.strip().startswith('from __future__')]

                return compile('\n'.join(fut + rest), filename, mode)

            except Exception:

                pass

        raise





def _protect_raw_payload(src: str, _depth_note: str = '') -> str:

    """Wrap a raw anti-hook/anti-debug payload so output holds only an

    encrypted fragmented blob + tiny polymorphic bootstrap (fix BUG #8).

    The blob is zlib+b85, split in chunks, decoded via indirect imports,

    verified by sha256 (fix BUG #18) before exec."""

    import base64 as _b64p, zlib as _zlp

    raw = src.encode('utf-8')

    digest = _yuki_sha256(raw)

    comp = _zlp.compress(raw, 9)

    b85expr = _yuki_b85_frag_expr(comp)

    v_blob = '_b' + uuid.uuid4().hex[:6]

    v_raw = '_r' + uuid.uuid4().hex[:6]

    v_dg = '_d' + uuid.uuid4().hex[:6]

    # indirect import names via chr() so 'import sys/os/ctypes' is not greppable

    imp_b64 = _yuki_chr_expr('base64')

    imp_zlib = _yuki_chr_expr('zlib')

    imp_hash = _yuki_chr_expr('hashlib')

    # split digest into 2 halves to avoid single hash literal

    h1, h2 = digest[:32], digest[32:]

    return (

        f"try:\n"

        f"    {v_blob}={b85expr}\n"

        f"    {v_raw}=__import__({imp_zlib}).decompress(__import__({imp_b64}).b85decode({v_blob}))\n"

        f"    {v_dg}=__import__({imp_hash}).sha256({v_raw}).hexdigest()\n"

        f"    assert {v_dg}==({h1!r}+{h2!r}),'integrity'\n"

        f"    exec({v_raw}.decode('utf-8'),globals(),globals())\n"
        f"    try: {v_raw}[:] = bytes(len({v_raw}))\n    except: pass\n"
        f"    del {v_blob}, {v_raw}, {v_dg}\n"

        f"except SystemExit:raise\n"
        f"except SystemExit:raise\nexcept Exception:__import__('os')._exit(137)\n"

    )



def _unicodeobf(b):

    a = []

    for c in b:

        k = ord(c) + _DYNAMIC_OFFSET_1

        a.append(k)

    return a

def anhxa(b):

    return _unicodeobf(b)



def _unicodeobf1(b):

    a = []

    for c in b:

        k = ord(c) + _DYNAMIC_OFFSET_2

        a.append(k)

    return a

def anhxa1(b):

    return _unicodeobf1(b)



def wraphay(s, j='?3..4c,2a.ã.45$@.4__khangcoder_..12.44.124.6', ma=1):

    random.seed()

    __ok__ = []

    __vailon__ = []

    for c in s:

        sublist = []

        pos = len(sublist)

        sublist.append(c)

        for _ in range(random.randint(1, ma)):

            sublist.append(j)

        __ok__.append(sublist)

        __vailon__.append(pos)

    fmt = '%s' * len(s)

    args = ', '.join(f"{repr(sublist)}[{pos}]" for sublist, pos in zip(__ok__, __vailon__))

    return f"('{fmt}' % ({args}))"



def poison_code_object(co):

    # FIX BUG #10: randomized multi-traps + referenced dead-code + lineno mangling.

    # Old code appended ONE hardcoded unreferenced const (ignored by modern decompilers).

    # New: 2-3 randomized traps, dead LOAD_CONST reference via wrapper, random firstlineno.

    if not isinstance(co, types.CodeType):

        return co

    try:

        new_consts = []

        for c in co.co_consts:

            if isinstance(c, types.CodeType):

                new_consts.append(poison_code_object(c))

            else:

                new_consts.append(c)

        _variants = [

            'def _t_{r}():\n    try: pass\n    finally:\n        (lambda: (yield from (lambda: (yield 1))()))()\n',

            'async def _t_{r}():\n    try:\n        async with (lambda: __import__("contextlib").nullcontext())():\n            (lambda: [(yield i) for i in range(2)])()\n    finally:\n        pass\n',

            'def _t_{r}(_a=[(lambda: (yield from (lambda: (yield 1))()))()], _b={k!r}):\n    match _a:\n        case [_, *_]:\n            try:\n                with (lambda: __import__("contextlib").nullcontext())():\n                    pass\n            except* ValueError as _e:\n                pass\n    return (_b, _a)\n',

            'def _t_{r}():\n    _w = (_w0 := (_w1 := 0))\n    return [(_x := (lambda: (yield _x))()) for _x in range(1)]\n',

        ]

        for _vi in range(random.randint(2, 3)):

            _r = uuid.uuid4().hex[:6]

            _k = random.randint(1000, 9999)

            _src = random.choice(_variants).format(r=_r, k=_k)

            try:

                _trap = compile(_src, f'<__yuki_trap_{_r}__>', 'exec')

                # keep only inner function code objects to maximize decompiler load

                for _cc in list(getattr(_trap, 'co_consts', ())):

                    if isinstance(_cc, types.CodeType) and _cc.co_name.startswith('_t_'):

                        new_consts.append(_cc)

                        # also poison nested inside trap

                        break

                else:

                    new_consts.append(_trap)

            except Exception:

                continue

        # Mangle firstlineno (safe: only affects tracebacks) to break line-based decompilers

        _new_first = random.randint(10000, 90000)

        try:

            return co.replace(co_consts=tuple(new_consts), co_firstlineno=_new_first)

        except Exception:

            return co.replace(co_consts=tuple(new_consts))

    except Exception:

        return co





def gen_advanced_antipycdc():

    # FIX BUG #6: polymorphic bombs (random depths/counts) + hidden keywords (anti-grep).

    bombs = []



    # 1. Nested ternary expressions (Pycdc AST stack overflow) - random depth

    expr = '0'

    for _ in range(random.randint(5, 9)):

        r1, r2 = random.randint(1000, 9999), random.randint(1000, 9999)

        expr = f'({r1} if ({expr} == 0) else {r2})'

    bombs.append(f'_Ox_c_{random.randint(100,999)} = {expr}')



    # 2. Nested lambda chains - random depth

    lam_expr = 'lambda: 0'

    for i in range(random.randint(3, 6)):

        lam_expr = f'(lambda _x{i}_{uuid.uuid4().hex[:3]}: {lam_expr})'

    bombs.append(f'try:\n    _Ox_lam = {lam_expr}\nexcept: pass')



    # 3. Walrus operator nesting - random depth

    walrus = '0'

    for i in range(random.randint(3, 6)):

        walrus = f'(_w{i} := {walrus} + 1)'

    bombs.append(f'try:\n    _Ox_wal = {walrus}\nexcept: pass')



    # 4. Multi-level try-except-finally blocks - random depth

    for _ in range(random.randint(2, 3)):

        body = 'pass'

        for _ in range(random.randint(2, 3)):

            indented = textwrap.indent(body, '    ')

            _exc = random.sample(['TypeError', 'ValueError', 'RuntimeError', 'LookupError', 'ArithmeticError', 'OSError', 'KeyError'], k=random.randint(3, 5))

            body = f'try:\n{indented}\nexcept ({", ".join(_exc)}):\n    pass\nfinally:\n    int({random.randint(100,999)})'

        bombs.append(body)



    # 5. Recursive generator expression - randomized

    _rg_n = random.randint(2, 4)

    bombs.append(f'''try:

    _gen_bomb = [((lambda: [__x for __x in (lambda: (lambda: (yield from (lambda: (yield 1))()))())()])()) for _ in range({_rg_n})]

except: pass''')



    # 6. Function call chain - random depth

    antipycdc_calls = ''

    for _ in range(random.randint(10, 16)):

        antipycdc_calls += "decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol(decㅤcáiㅤlol('  ')))))),"

    antipycdc_calls = 'try:khangcoder=[' + antipycdc_calls + ']\nexcept:pass'

    bombs.append(antipycdc_calls)

    # 7. NEW: deeply nested comprehension bomb (real parser load, not just AST junk)

    _comp_depth = random.randint(3, 5)

    _comp = '0'

    for _d in range(_comp_depth):

        _comp = f'[[{_comp} for _q{_d} in range(2)] for _p{_d} in range(2)]'

    bombs.append(f'try:\n    _Ox_comp_{random.randint(100,999)} = {_comp}\nexcept: pass')

    # 8. Pattern Matching Syntax Crasher (Crashes pycdc on MATCH_MAPPING / MATCH_SEQUENCE)
    _m_id = uuid.uuid4().hex[:5]
    bombs.append(f'''try:
    match [1, (2, 3), {{"k": 4}}]:
        case [_a_{_m_id}, (_b_{_m_id}, _c_{_m_id}), {{"k": _d_{_m_id}}}] if _a_{_m_id} == 1:
            pass
        case [*_rest_{_m_id}]:
            pass
except: pass''')

    # 9. ExceptionGroup except* Syntax Crasher (Crashes pycdc/uncompyle on CHECK_EG_MATCH)
    if sys.version_info >= (3, 11):
        _eg_id = uuid.uuid4().hex[:5]
        bombs.append(f'''try:
    pass
except* (TypeError, ValueError, ArithmeticError) as _eg_{_eg_id}:
    pass''')

    # 10. Irreducible Control Flow Graph (CFG) Trap (Earley Parser blowup in uncompyle)
    _cfg_id = uuid.uuid4().hex[:5]
    bombs.append(f'''try:
    def _cfg_{_cfg_id}():
        for _i in range(2):
            try:
                if _i == 0: continue
                else: yield from (lambda: (yield _i))()
            finally:
                if _i == 1: break
    list(_cfg_{_cfg_id}())
except: pass''')

    # 11. Async Comprehension Stack Bomb
    _as_id = uuid.uuid4().hex[:5]
    bombs.append(f'''try:
    async def _as_{_as_id}():
        return [(_x, _y) async for _x in (lambda: (_i for _i in range(1)))() for _y in range(1)]
except: pass''')



    ast_bombs_str = '\n'.join(bombs)

    # Build hidden keyword blobs (anti-grep fix BUG #6/#7/#8)

    import base64 as _b64_ab

    _kw_ab = _b64_ab.b64encode(b'pycdc,decompyle,uncompyle,decompile,deobf,disassembl,pydisasm,unpyc,pyfluff,marshal_dump,tracer,hook_exec,hook_marshal,pylingual,pyarmor').decode()

    _pr_ab = _b64_ab.b64encode(b'pycdc,pycdc.exe,decompyle++,uncompyle6,decompyle,pydecomp,pylingual,xdis,pyarmor,pyfluff,decompile,unpyc,dis,pycdc_gui,ida.exe,ida64.exe,idag.exe,idaw.exe,x64dbg.exe,x32dbg.exe,x96dbg.exe,cheatengine.exe,scylla.exe,processhacker.exe,procmon.exe,wireshark.exe,fiddler.exe,charles.exe,httpcanary.exe,mitmproxy.exe,burpsuite.exe,dnspy.exe,de4dot.exe').decode()

    _md_ab = _b64_ab.b64encode(b'pycdc,decompyle,uncompyle,decompile,xdis,pydisasm,pylingual,deobfuscator').decode()

    

    active_engine = '''

try: print('-> Loading...', end='\\r')
except Exception: pass

j = []

if isinstance(j, (list, tuple, set, dict)):l = len(j)

def 你器你器(__chanbomaydi__):

    return __chanbomaydi__



# ==================== ADVANCED FULL ACTIVE ANTI-PYCDC ENGINE ====================

def __yuki_active_pycd_watchdog__():

    import sys, os, time

    import base64 as _b64w

    _bad_kw = tuple(_b64w.b64decode('__YUKI_KW_B64__').decode().split(','))

    _bad_procs = tuple(_b64w.b64decode('__YUKI_PR_B64__').decode().split(','))

    _bad_mods = tuple(_b64w.b64decode('__YUKI_MD_B64__').decode().split(','))

    def _kill_procs():

        try:

            import ctypes

            # Bug #6 Fix: Check window titles so renaming x64dbg.exe -> abc.exe is detected

            _u32 = getattr(getattr(ctypes, 'windll', None), 'user32', None)

            if _u32 and hasattr(_u32, 'GetWindowTextW') and hasattr(_u32, 'EnumWindows'):

                _bad_titles = ('x64dbg', 'x32dbg', 'ida pro', 'ida -', 'cheat engine', 'process hacker', 'wireshark', 'fiddler', 'http debugger', 'pycdc', 'decompyle', 'uncompyle', 'pylingual', 'ghidra', 'dnspy', 'de4dot', 'decompiler')

                @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

                def _w_enum_cb(hwnd, lparam):

                    if _u32.IsWindowVisible(hwnd):

                        buf = ctypes.create_unicode_buffer(512)

                        _u32.GetWindowTextW(hwnd, buf, 512)

                        val = buf.value.lower()

                        if any(t in val for t in _bad_titles):

                            os._exit(138)

                    return True

                _u32.EnumWindows(_w_enum_cb, 0)

        except Exception: pass

        try:

            import ctypes

            TH32CS_SNAPPROCESS = 0x00000002

            PROCESS_TERMINATE = 0x0001

            _windll = getattr(ctypes, 'windll', None)

            k32 = None

            if _windll is not None:

                try:

                    k32 = _windll.kernel32

                except Exception:

                    k32 = None

            if k32 is not None:

                class PROCESSENTRY32W(ctypes.Structure):

                    _fields_ = [

                        ('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong),

                        ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t),

                        ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong),

                        ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long),

                        ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_wchar * 260)

                    ]

                hSnap = k32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)

                if hSnap != -1:

                    pe = PROCESSENTRY32W()

                    pe.dwSize = ctypes.sizeof(PROCESSENTRY32W)

                    if k32.Process32FirstW(hSnap, ctypes.byref(pe)):

                        while True:

                            exe = pe.szExeFile.lower()

                            if any(x in exe for x in _bad_procs):

                                hProc = k32.OpenProcess(PROCESS_TERMINATE, False, pe.th32ProcessID)

                                if hProc:

                                    k32.TerminateProcess(hProc, 1)

                                    k32.CloseHandle(hProc)

                                os._exit(137)

                            if not k32.Process32NextW(hSnap, ctypes.byref(pe)): break

                    k32.CloseHandle(hSnap)

        except Exception: pass

        try:

            if os.path.exists('/proc'):

                for e in os.listdir('/proc'):

                    if e.isdigit():

                        try:

                            with open(f'/proc/{e}/cmdline', 'rb') as f:

                                c = f.read().decode('latin1', 'ignore').lower()

                                if any(x in c for x in _bad_procs):

                                    try: os.kill(int(e), 9)

                                    except: pass

                                    os._exit(137)

                        except: pass

        except Exception: pass



    def _hard_die(code=95):

        try:

            import ctypes as _cd

            _k = getattr(getattr(_cd, 'windll', None), 'kernel32', None)

            if _k and hasattr(_k, 'TerminateProcess'): _k.TerminateProcess(_k.GetCurrentProcess(), 0xC0000005)

            _nt = getattr(getattr(_cd, 'windll', None), 'ntdll', None)

            if _nt and hasattr(_nt, 'NtTerminateProcess'): _nt.NtTerminateProcess(-1, 0xC0000005)

            _cd.memset(0, 0, 1)

        except: pass

        try: os.abort()

        except: pass

        os._exit(code)



    _pulse_cnt = 0

    while True:

        try:

            _pulse_cnt = (_pulse_cnt + 1) & 0xFFFFFFFF

            try:

                import sys as _sw, time as _tw

                _g = getattr(_sw.modules.get('__main__'), '__dict__', None) or globals()

                _g['__yuki_pulse__'] = (_tw.time(), (_pulse_cnt ^ 0x5F3759DF))

            except Exception: pass

            if sys.gettrace() is not None: _hard_die(95)

            if hasattr(sys, 'monitoring'):

                for _ti in range(6):

                    _ev = sys.monitoring.get_events(_ti)

                    _tl = sys.monitoring.get_tool(_ti)

                    if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                        _hard_die(95)

            for f in sys._current_frames().values():

                cf = f

                while cf:

                    co_fn = (getattr(cf.f_code, 'co_filename', '') or '').lower()

                    fn_name = (getattr(cf.f_code, 'co_name', '') or '').lower()

                    if any(x in co_fn or x in fn_name for x in _bad_kw):

                        _hard_die(97)

                    cf = cf.f_back

            for m in list(sys.modules.keys()):

                if any(x in m.lower() for x in _bad_mods):

                    _hard_die(96)

            # Full 24-byte hook pattern coverage

            try:

                import ctypes

                try: _pyapi = object.__getattribute__(ctypes, 'pythonapi')

                except Exception: _pyapi = getattr(ctypes, 'pythonapi', None)

                for sym in ('PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault', 'PyRun_StringFlags', 'PyObject_Call'):

                    try: addr = getattr(_pyapi, sym, None)

                    except Exception: continue

                    if addr:

                        ptr = ctypes.cast(addr, ctypes.c_void_p).value

                        if ptr:

                            b = bytes((ctypes.c_ubyte * 24).from_address(ptr))

                            if (b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2)

                                or (b[0] == 0xFF and len(b) > 1 and b[1] in (0x25, 0xE0, 0xE1, 0xE2))

                                or (b[0] == 0x48 and len(b) > 1 and b[1] == 0xB8)

                                or (b[0] == 0xCD and len(b) > 1 and b[1] == 0x03)

                                or (b[0] == 0xB8 and len(b) > 6 and b[5] == 0xFF and b[6] == 0xE0)

                                or (b[0] == 0x68 and len(b) > 5 and b[5] == 0xC3)

                                or (len(b) >= 3 and b[0] == 0x90 and b[1] == 0x90 and b[2] == 0x90)):

                                _hard_die(91)

                            for off in (1, 2, 3):

                                if len(b) > off + 2 and (b[off] in (0xE9, 0xCC) or (b[off] == 0xFF and b[off+1] == 0x25) or (b[off] == 0x48 and b[off+1] == 0xB8)):

                                    _hard_die(91)

            except Exception: pass

            _kill_procs()

        except Exception: pass

        time.sleep(0.25)



try:

    if '__yuki_watchdog_active__' not in globals():

        globals()['__yuki_watchdog_active__'] = True

        try:

            import _thread as _th_act

            _th_act.start_new_thread(__yuki_active_pycd_watchdog__, ())

        except Exception:

            import threading as _th_act

            _th_act.Thread(target=__yuki_active_pycd_watchdog__, daemon=True).start()

except Exception: pass

'''

    try:

        active_engine = active_engine.replace('__YUKI_KW_B64__', _kw_ab).replace('__YUKI_PR_B64__', _pr_ab).replace('__YUKI_MD_B64__', _md_ab)

    except Exception:

        pass

    return active_engine + '\n' + ast_bombs_str + '\nfinally:int(2009-1711)\n'



ANTI_PYCDC = gen_advanced_antipycdc()



trap = rb()

trap1 = rb2()

# --- ENCODE LAYERS VĨNH VIỄN ---

def _enc_a(s): return wraphay(s)

def _enc_b(s): return wraphay(''.join(str(ord(c)+_DYNAMIC_OFFSET_1) for c in s))

def _enc_c(s):

    _daubuoi = "0123456789"

    _ancut = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"

    _trash = dict(zip(_daubuoi, _ancut))

    t = ''.join(str(b).zfill(3) for b in s.encode())

    p = ''.join(_trash.get(c, c) for c in t)

    return f"__yuki_enc3__({repr(p)})"

def _enc_d(s):

    import base64, zlib

    return base64.b64encode(zlib.compress(s.encode(), 9)).decode()

# --- ANTI DEBUG / ANTI HOOK / ANTI REQUEST HOOK ---

import types, inspect, time, os, builtins



_X1 = rb(); _X2 = rb1(); _X3 = rb4()



_FDBG = rb(); _FDBG2 = rb()



# --- FIXED FULL POWER ANTI DEBUG (generator self-protection) ---

_FDBG_CODE = f"""

def {_FDBG}(b=None):

    import sys, os, time, platform, builtins, types

    # 1. basic debugger detection (Bug #3 fix: do not swallow SystemExit)

    try:

        if sys.gettrace() is not None:

            raise SystemExit('DEBUG_GETTRACE')

    except SystemExit: raise

    except Exception: pass

    try:

        if hasattr(sys, 'getprofile') and sys.getprofile() is not None:

            raise SystemExit('DEBUG_GETPROFILE')

    except SystemExit: raise

    except Exception: pass

    try:

        if getattr(sys.flags, 'debug', 0) != 0:

            raise SystemExit('DEBUG_FLAG')

    except SystemExit: raise

    except Exception: pass

    try:

        if hasattr(sys, 'monitoring'):

            for _ti in range(6):

                _ev = sys.monitoring.get_events(_ti)

                _tl = sys.monitoring.get_tool(_ti)

                if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                    raise SystemExit('PEP669_MONITORING')

            for _ti in range(6):

                try: sys.monitoring.use_tool_id(_ti, 'yuki_' + str(_ti))

                except: pass

                try: sys.monitoring.set_events(_ti, 0)

                except: pass

    except SystemExit: raise

    except Exception: pass

    try:

        if getattr(builtins, '__IPYTHON__', None) is not None:

            raise SystemExit('IPYTHON')

    except SystemExit: raise

    except Exception: pass

    # env vars

    try:

        _bad_env = ('PYTHONDEBUG','PYTHONBREAKPOINT','PYDEVD_LOAD_VALUES_ASYNC','PYCHARM','VSCODE_PID','TERM_PROGRAM')

        for _k in _bad_env:

            if os.environ.get(_k):

                raise SystemExit('ENV_DEBUG_' + _k)

        if os.environ.get('PDB') or os.environ.get('DEBUG'):

            raise SystemExit('ENV_DEBUG')

    except SystemExit: raise

    except Exception: pass

    # sys.modules debugger modules

    try:

        _dbg_mods = ('pdb','bdb','pydevd','debugpy','ptvsd','cProfile','pycdc','decompyle','uncompyle','xdis','pyfluff','pylingual')

        for _m in list(sys.modules.keys()):

            _ml = _m.lower()

            if any(x in _ml for x in _dbg_mods):

                raise SystemExit('MODULE_DEBUG_' + _m)

    except SystemExit: raise

    except Exception: pass

    # timing anti-hook / anti-emu (Bug #4 fix: calibrate baseline first to avoid slow VPS false positives)

    try:

        _t_cal0 = time.perf_counter()

        for _i in range(1000): pass

        _t_base = max(time.perf_counter() - _t_cal0, 1e-6)

        _t0 = time.perf_counter()

        _s = 0

        for _i in range(10000):

            _s += _i

        if (time.perf_counter() - _t0) > max(_t_base * 40, 3.5):

            raise SystemExit('TIMING_HOOK')

    except SystemExit: raise

    except Exception: pass

    # Real hypervisor / sandbox detection (firmware + services + DMI, not env-only fake checks)

    try:

        if os.environ.get('YUKI_ALLOW_VM') == '1':

            pass

        else:

            _vm_score = 0

            _vm_tok = ('vmware','virtualbox','qemu','sandbox','kvm','xen','vbox','bochs','innotek','parallels','hyper-v','virtual machine','tcg')

            try:

                if os.environ.get('WINELOADER') or os.environ.get('WINEPREFIX'):

                    _vm_score += 2

            except: pass

            try:

                _node = (platform.node() or '').lower()

                if any(x in _node for x in _vm_tok):

                    _vm_score += 1

            except: pass

            try:

                import uuid

                _mac = f"{{uuid.getnode():012x}}".lower()

                if _mac[:6] in ('000569','000c29','001c14','005056','080027','525400','001c42','0003ff'):

                    _vm_score += 1

            except: pass

            try:

                if os.name == 'nt':

                    import winreg

                    try:

                        _k = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\\\\DESCRIPTION\\\\System\\\\BIOS")

                        _mfg = str(winreg.QueryValueEx(_k, "SystemManufacturer")[0]).lower()

                        _prod = str(winreg.QueryValueEx(_k, "SystemProductName")[0]).lower()

                        winreg.CloseKey(_k)

                        if any(x in _mfg or x in _prod for x in _vm_tok) or ('virtual' in _prod):

                            _vm_score += 2

                    except OSError:

                        pass

                    for _rk in (r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VBoxGuest', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VBoxMouse', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\VMTools', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\vmmouse', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\vmci', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\xeniface', r'SYSTEM\\\\CurrentControlSet\\\\Services\\\\balloon'):

                        try:

                            _sk = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, _rk)

                            winreg.CloseKey(_sk)

                            _vm_score += 2

                            break

                        except OSError:

                            pass

                    try:

                        import ctypes as _ctv

                        _k32 = getattr(getattr(_ctv, 'windll', None), 'kernel32', None)

                        if _k32 and hasattr(_k32, 'GetSystemFirmwareTable'):

                            _n = _k32.GetSystemFirmwareTable(0x52534D42, 0, None, 0)

                            if _n:

                                _buf = (_ctv.c_char * _n)()

                                _k32.GetSystemFirmwareTable(0x52534D42, 0, _buf, _n)

                                _sm = bytes(_buf).lower()

                                for _tok in (b'vmware', b'virtualbox', b'qemu', b'vbox', b'bochs', b'xen', b'kvm', b'hyper-v', b'tcg', b'parallels', b'innotek', b'virtual machine', b'virtual hd'):

                                    if _tok in _sm:

                                        _vm_score += 2

                                        break

                    except Exception:

                        pass

            except: pass

            try:

                if os.name == 'nt':

                    _v_drv = (r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxMouse.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxGuest.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\VBoxSF.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmmouse.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmci.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmxnet.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vmmemctl.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\balloon.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\netkvm.sys', r'C:\\\\Windows\\\\System32\\\\drivers\\\\vioscsi.sys')

                    if any(os.path.exists(_d) for _d in _v_drv):

                        _vm_score += 2

            except: pass

            try:

                for _p in ('/sys/class/dmi/id/product_name', '/sys/class/dmi/id/sys_vendor', '/sys/class/dmi/id/bios_vendor', '/sys/hypervisor/type'):

                    if os.path.exists(_p):

                        with open(_p, 'r', errors='ignore') as _df:

                            _dv = _df.read().lower()

                        if any(x in _dv for x in _vm_tok):

                            _vm_score += 2

                            break

            except: pass

            try:

                if os.path.exists('/proc/cpuinfo'):

                    with open('/proc/cpuinfo', 'r', errors='ignore') as _cf:

                        _ci = _cf.read().lower()

                    if 'hypervisor' in _ci:

                        _vm_score += 1

            except: pass

            if _vm_score >= 2:

                raise SystemExit('VM_DETECTED')

    except SystemExit: raise

    except Exception: pass

    # builtins integrity - FIX BUG #13: identity + isbuiltin (no str(type) spoof, no PyPy false-positive)

    try:

        import types as _t_bi

        _BuiltinTypes = getattr(_t_bi, 'BuiltinFunctionType', type(len)), getattr(_t_bi, 'BuiltinMethodType', type(len))

        try:

            _o = builtins.__dict__.get('open', None)

            if _o is not None:

                _orig_o = getattr(_o, '__wrapped__', _o)

                if not isinstance(_orig_o, _BuiltinTypes):

                    raise SystemExit('HOOK_OPEN')

        except SystemExit: raise

        except Exception: pass

        for _bn in ('print','compile','eval','exec','__import__'):

            try:

                _obj = getattr(builtins, _bn, None)

                if _obj is None: continue

                # 1) identity must match builtins dict

                try:

                    if builtins.__dict__.get(_bn) is not _obj:

                        raise SystemExit('HOOK_BUILTIN_' + _bn.upper())

                except SystemExit: raise

                except Exception: pass

                # 2) must be real builtin type (blocks python-level wrappers with fake __module__)

                if not isinstance(_obj, _BuiltinTypes):

                    _orig = getattr(_obj, '__wrapped__', None)

                    if _orig is not None and isinstance(_orig, _BuiltinTypes):

                        continue

                    # allow only if __self__ is builtins module (bound builtin)

                    if getattr(_obj, '__self__', None) is not builtins:

                        if getattr(_obj, '__module__', '') not in ('builtins','_builtins','__builtin__'):

                            raise SystemExit('HOOK_BUILTIN_' + _bn.upper())

                        # wrapper with fake module but not builtin type -> still hook

                        raise SystemExit('HOOK_BUILTIN_' + _bn.upper())

            except SystemExit: raise

            except Exception: continue

    except SystemExit: raise

    except: pass

    # IsDebuggerPresent & Window Detection (Windows - Bug #6 Fix)

    try:

        import ctypes

        _wd = getattr(ctypes, 'windll', None)

        if _wd is not None:

            try:

                _u32 = getattr(_wd, 'user32', None)

                if _u32 and hasattr(_u32, 'GetWindowTextW') and hasattr(_u32, 'EnumWindows'):

                    _dtitles = ('x64dbg', 'x32dbg', 'ida pro', 'ida -', 'cheat engine', 'process hacker', 'wireshark', 'fiddler')

                    @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

                    def _ew_cb(hwnd, lp):

                        if _u32.IsWindowVisible(hwnd):

                            buf = ctypes.create_unicode_buffer(512)

                            _u32.GetWindowTextW(hwnd, buf, 512)

                            val = buf.value.lower()

                            if any(t in val for t in _dtitles):

                                raise SystemExit('DEBUGGER_WINDOW')

                        return True

                    _u32.EnumWindows(_ew_cb, 0)

            except SystemExit: raise

            except: pass

            try:

                _k = _wd.kernel32

                if _k.IsDebuggerPresent():

                    raise SystemExit('WIN_DEBUGGER')

                _is_remote = ctypes.c_bool(False)

                _k.CheckRemoteDebuggerPresent(_k.GetCurrentProcess(), ctypes.byref(_is_remote))

                if _is_remote.value:

                    raise SystemExit('WIN_REMOTE_DEBUGGER')

                # NtQueryInformationProcess & ThreadHideFromDebugger

                try:

                    _ntdll = _wd.ntdll

                    _ph = _k.GetCurrentProcess()

                    try: _ntdll.NtSetInformationThread(_k.GetCurrentThread(), 0x11, 0, 0)

                    except: pass

                    _dbg_port = ctypes.c_ulong(0)

                    _status = _ntdll.NtQueryInformationProcess(_ph, 7, ctypes.byref(_dbg_port), ctypes.sizeof(_dbg_port), None)

                    if _status == 0 and _dbg_port.value != 0:

                        raise SystemExit('NT_DEBUG_PORT')

                    _dbg_flags = ctypes.c_ulong(1)

                    _status = _ntdll.NtQueryInformationProcess(_ph, 0x1F, ctypes.byref(_dbg_flags), ctypes.sizeof(_dbg_flags), None)

                    if _status == 0 and _dbg_flags.value == 0:

                        raise SystemExit('NT_DEBUG_FLAGS')

                except: pass

            except SystemExit: raise

            except: pass

    except: pass

    # ptrace anti-debug on Linux (TracersPid)

    try:

        if os.path.exists('/proc/self/status'):

            with open('/proc/self/status','r',errors='ignore') as _f:

                for _line in _f:

                    if _line.startswith('TracerPid:'):

                        _pid = _line.split(':',1)[1].strip()

                        if _pid != '0':

                            raise SystemExit('PTRACE_DETECTED')

                        break

    except SystemExit: raise

    except: pass

    # open file hook check

    try:

        _orig_open = open

        if open is not builtins.open:

            raise SystemExit('HOOK_OPEN2')

    except: pass

"""

exec(_FDBG_CODE)





_A = rb(); _B = rb1(); _C = rb2()

exec(f"{_FDBG}()")



# bảo vệ hook code

_A2 = rb(); _A3 = rb1()

_FHOOK = rb()

# FIXED _FHOOK with proper reference guard

exec(f"def {_FHOOK}(obj, nm):\n"

     f"    _is_d = isinstance(obj, dict)\n"

     f"    orig = obj.get(nm, None) if _is_d else getattr(obj, nm, None)\n"

     f"    if orig is None or not callable(orig): return\n"

     f"    _ref = [None]\n"

     f"    def guard(*a, **kw):\n"

     f"        cur = obj.get(nm, None) if _is_d else getattr(obj, nm, None)\n"

     f"        if cur is not _ref[0]:\n"

     f"            raise SystemExit('HOOK_DETECTED_' + str(nm).upper())\n"

     f"        if nm in ('eval', 'exec'):\n"

     f"            if len(a) == 1 and 'globals' not in kw:\n"

     f"                _f = __import__('sys')._getframe(1)\n"

     f"                return orig(a[0], _f.f_globals, _f.f_locals)\n"

     f"            elif len(a) == 2 and 'locals' not in kw:\n"

     f"                return orig(a[0], a[1], a[1])\n"

     f"        return orig(*a, **kw)\n"

     f"    _ref[0] = guard\n"

     f"    try:\n"

     f"        guard.__wrapped__ = orig\n"

     f"    except Exception: pass\n"

     f"    try:\n"

     f"        if _is_d: obj[nm] = guard\n"

     f"        else: setattr(obj, nm, guard)\n"

     f"    except Exception: pass\n")



# --- FIXED HOOK PROTECTION (Bug #11 Fix: protect builtins whether dict or ModuleType) ---

try:

    _hook_targets = [

        (sys, ('stdout','stderr','stdin','modules','exit')),

        (builtins, ('exit','quit','input','open','compile','eval','exec','__import__','print')),

    ]

    if isinstance(__builtins__, dict) and __builtins__ is not getattr(builtins, '__dict__', None):

        _hook_targets.append((__builtins__, ('exit','quit','input','open','compile','eval','exec','__import__','print')))

    for _t, _names in _hook_targets:

        for _n in _names:

            try:

                globals()[_FHOOK](_t, _n)

            except Exception:

                pass

except Exception:

    pass



# chống hook requests / urllib

# --- FIXED urllib.request PROTECTION ---

try:

    _ur = __import__('urllib.request', fromlist=['urlopen'])

    _o = getattr(_ur, 'urlopen', None)

    if callable(_o):

        _ur_original_urlopen = _o

        def _hurl(*a, **kw):

            cur = getattr(_ur, 'urlopen', None)

            # check if hook replaced our wrapper

            if cur is not _hurl:

                # if someone replaced after us, cur != _hurl -> hook detected

                # but we allow only our wrapper, otherwise exit

                if cur is not _ur_original_urlopen and cur is not _hurl:

                    raise SystemExit('REQUEST_HOOK_URLLIB')

            return _ur_original_urlopen(*a, **kw)

        _ur.urlopen = _hurl

        # also protect OpenerDirector

        try:

            _OD = getattr(_ur, 'OpenerDirector', None)

            if _OD and hasattr(_OD, 'open'):

                _orig_OD_open = _OD.open

                _guard_ref = [None]

                def _od_guard(self, *a, **kw):

                    if getattr(_OD, 'open', None) is not _guard_ref[0]:

                        raise SystemExit('HOOK_OPENER')

                    return _orig_OD_open(self, *a, **kw)

                _guard_ref[0] = _od_guard

                _OD.open = _od_guard

        except Exception:

            pass

except Exception:

    pass



# --- FIXED requests API PROTECTION ---

try:

    _rq = __import__('requests')

    for _rn in ('get','post','put','delete','request','patch','head','options'):

        try:

            orig = getattr(_rq, _rn, None)

            if not callable(orig):

                continue

            # need closure to capture orig and name correctly

            def _make_rguard(_orig, _name):

                _ref = [None]

                def _wrap(*a, **kw):

                    if getattr(_rq, _name, None) is not _ref[0]:

                        raise SystemExit('REQUEST_HOOK_' + _name.upper())

                    return _orig(*a, **kw)

                _ref[0] = _wrap

                # preserve metadata

                try:

                    _wrap.__name__ = getattr(_orig, '__name__', _name)

                    _wrap.__wrapped__ = _orig

                except: pass

                return _wrap

            setattr(_rq, _rn, _make_rguard(orig, _rn))

        except Exception:

            pass

    # protect Session.request separately with stronger guard

    try:

        import requests.sessions

        _Sess = requests.sessions.Session

        _orig_sess_req = getattr(_Sess, 'request', None)

        if callable(_orig_sess_req):

            _sess_ref = [None]

            def _sess_guard(self, *a, **kw):

                if getattr(_Sess, 'request', None) is not _sess_ref[0]:

                    raise SystemExit('HOOK_SESSION_REQUEST')

                return _orig_sess_req(self, *a, **kw)

            _sess_ref[0] = _sess_guard

            _Sess.request = _sess_guard

    except Exception:

        pass

except Exception:

    pass



# --- NANG CAP FULL POWER ANTI HOOK (FIXED) ---

try:

    import urllib3.connectionpool as _u_pool_mod

    import urllib.request as _u_req_mod

    import http.client as _http_mod

    import requests.adapters as _req_adapt_mod

    import requests.api as _req_api_mod

    import requests as _req_mod



    # 1) urllib3 HTTPConnectionPool.urlopen

    try:

        _Pool = _u_pool_mod.HTTPConnectionPool

        _orig_pool_urlopen = getattr(_Pool, 'urlopen', None)

        if callable(_orig_pool_urlopen):

            _pool_ref = [None]

            def _pool_urlopen_guard(self, *a, **kw):

                if getattr(_Pool, 'urlopen', None) is not _pool_ref[0]:

                    raise SystemExit('REQUEST_HOOK_POOL')

                return _orig_pool_urlopen(self, *a, **kw)

            _pool_ref[0] = _pool_urlopen_guard

            _Pool.urlopen = _pool_urlopen_guard

    except Exception: pass



    # 2) http.client HTTPConnection methods

    try:

        _HC = _http_mod.HTTPConnection

        for _mname in ('request','putrequest','getresponse','endheaders','send'):

            try:

                _orig_m = getattr(_HC, _mname, None)

                if not callable(_orig_m): continue

                def _make_http_guard(_orig, _name):

                    _ref = [None]

                    def _guard(self, *a, **kw):

                        if getattr(_HC, _name, None) is not _ref[0]:

                            raise SystemExit('HOOK_HTTP_' + _name.upper())

                        return _orig(self, *a, **kw)

                    _ref[0] = _guard

                    return _guard

                setattr(_HC, _mname, _make_http_guard(_orig_m, _mname))

            except Exception: continue

        # also HTTPSConnection

        try:

            _HCS = getattr(_http_mod, 'HTTPSConnection', None)

            if _HCS:

                for _mname in ('request','putrequest'):

                    try:

                        _orig_m = getattr(_HCS, _mname, None)

                        if not callable(_orig_m): continue

                        def _make_https_guard(_orig, _name):

                            _ref = [None]

                            def _guard(self, *a, **kw):

                                if getattr(_HCS, _name, None) is not _ref[0]:

                                    raise SystemExit('HOOK_HTTPS_' + _name.upper())

                                return _orig(self, *a, **kw)

                            _ref[0] = _guard

                            return _guard

                        setattr(_HCS, _mname, _make_https_guard(_orig_m, _mname))

                    except: continue

        except: pass

    except Exception: pass



    # 3) requests.adapters HTTPAdapter.send

    try:

        _Adp = _req_adapt_mod.HTTPAdapter

        _orig_adp_send = getattr(_Adp, 'send', None)

        if callable(_orig_adp_send):

            _adp_ref = [None]

            def _guard_adapter_send(self, *a, **kw):

                if getattr(_Adp, 'send', None) is not _adp_ref[0]:

                    raise SystemExit('HOOK_ADAPTER_SEND')

                return _orig_adp_send(self, *a, **kw)

            _adp_ref[0] = _guard_adapter_send

            _Adp.send = _guard_adapter_send

    except Exception: pass



    # 4) requests.api functions

    try:

        for _fn in ('request','get','post','put','delete','patch','head','options'):

            try:

                _orig = getattr(_req_api_mod, _fn, None)

                if not callable(_orig): continue

                def _make_api_guard(_orig, _name):

                    _ref = [None]

                    def _wrap(*a, **kw):

                        if getattr(_req_api_mod, _name, None) is not _ref[0]:

                            raise SystemExit('HOOK_API_' + _name.upper())

                        return _orig(*a, **kw)

                    _ref[0] = _wrap

                    return _wrap

                setattr(_req_api_mod, _fn, _make_api_guard(_orig, _fn))

            except: continue

    except Exception: pass



    # 5) builtins.__import__ guard - DISABLED for generator to avoid self-lock (payload has separate protection)

    try:

        pass

    except Exception:

        pass



    # 6) inspect.getmembers guard

    try:

        import inspect as _ins_mod

        if hasattr(_ins_mod, 'getmembers'):

            _orig_gm = _ins_mod.getmembers

            if callable(_orig_gm):

                _gm_ref = [None]

                def _guard_getmembers(obj, *a, **kw):

                    if getattr(_ins_mod, 'getmembers', None) is not _gm_ref[0]:

                        raise SystemExit('HOOK_INSPECT_GETMEMBERS')

                    return _orig_gm(obj, *a, **kw)

                _gm_ref[0] = _guard_getmembers

                _ins_mod.getmembers = _guard_getmembers

    except Exception: pass



    # 7) socket.getaddrinfo / gethostbyname / socket.send + enhanced socket.socket + ssl

    try:

        import socket as _sock_mod

        for _sname in ('getaddrinfo','gethostbyname','gethostbyname_ex','create_connection','getfqdn'):

            try:

                _orig = getattr(_sock_mod, _sname, None)

                if not callable(_orig): continue

                def _make_sock_guard(_orig, _name):

                    _ref = [None]

                    def _wrap(*a, **kw):

                        if getattr(_sock_mod, _name, None) is not _ref[0]:

                            raise SystemExit('HOOK_SOCKET_' + _name.upper())

                        return _orig(*a, **kw)

                    _ref[0] = _wrap

                    return _wrap

                setattr(_sock_mod, _sname, _make_sock_guard(_orig, _sname))

            except: continue

        # protect socket.socket methods

        try:

            _Sock = _sock_mod.socket

            for _mname in ('connect','send','sendall','recv','recvfrom','sendto','setsockopt','getsockopt'):

                try:

                    _orig_m = getattr(_Sock, _mname, None)

                    if not callable(_orig_m): continue

                    def _make_sockm_guard(_orig, _name):

                        _ref = [None]

                        def _guard(self, *a, **kw):

                            if getattr(_Sock, _name, None) is not _ref[0]:

                                raise SystemExit('HOOK_SOCKOBJ_' + _name.upper())

                            return _orig(self, *a, **kw)

                        _ref[0] = _guard

                        return _guard

                    setattr(_Sock, _mname, _make_sockm_guard(_orig_m, _mname))

                except: continue

        except: pass

        # protect ssl

        try:

            import ssl as _ssl_mod

            if hasattr(_ssl_mod, 'SSLSocket'):

                for _mname in ('send','sendall','recv','read','write'):

                    try:

                        _orig_m = getattr(_ssl_mod.SSLSocket, _mname, None)

                        if not callable(_orig_m): continue

                        def _make_sslg(_orig, _name):

                            _ref = [None]

                            def _guard(self, *a, **kw):

                                if getattr(_ssl_mod.SSLSocket, _name, None) is not _ref[0]:

                                    raise SystemExit('HOOK_SSL_' + _name.upper())

                                return _orig(self, *a, **kw)

                            _ref[0] = _guard

                            return _guard

                        setattr(_ssl_mod.SSLSocket, _mname, _make_sslg(_orig_m, _mname))

                    except: continue

        except: pass

    except Exception: pass



except Exception: pass



if __name__ == '__main__':

    exec(f"{_FDBG}()")



daubuoi = "0123456789"

ancut = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"



trash = dict(zip(daubuoi, ancut))

d = {v: k for k, v in trash.items()}



def __yuki_enc3__(s):

    # decode roman numerals encoded string

    rev = {v:k for k,v in trash.items()}

    t = ''.join(rev.get(c,c) for c in s)

    try:

        # t is zero-padded 3-digit bytes

        b = bytes(int(t[i:i+3]) for i in range(0, len(t), 3) if t[i:i+3].isdigit())

        return b.decode('utf-8', errors='ignore')

    except Exception:

        return s



_YUKI_ROMAN_DEC_NAME = f"_Ox{uuid.uuid4().hex[:8]}"

_YUKI_RUN_NAME = f"_Ox{uuid.uuid4().hex[:7]}"

_YUKI_ABI_MAP_NAME = f"_Ox{uuid.uuid4().hex[:7]}"

_YUKI_PRO_NAME = f"_Ox{uuid.uuid4().hex[:7]}"

_YUKI_SYS_NAME = f"_Ox{uuid.uuid4().hex[:7]}"

_YUKI_SALT_L1 = secrets.token_bytes(16)

_salt_l1_expr = f"bytes({list(_YUKI_SALT_L1)})"



def enc(s: str) -> str:

    ThgChoNqu = ''.join(str(b).zfill(3) for b in s.encode())

    phananhxa = ''.join(trash.get(c, c) for c in ThgChoNqu)

    return f"{_YUKI_ROMAN_DEC_NAME}({repr(phananhxa)})"



i=rb4()

q=rb1()

v = rb1()

y = rb4()

args = rb()

kwds = rb()

d = rb1()

k = rb()

c = rb1()

_c = rb1()

arg_ = rb()

s = rb1()

t = rb()

m = rb1()

f = rb4()

r = rb1()

z = rb4()

meo = rb1()

trunks = rb4()

siba = rb1()

champ = rb()

_replace = rb4()

thicthamcrush = rb1()

x=rb4()

o=rb()

_compile=rb3()

a=rb4()

b=rb4()

hexlol=rb3()

_globals=rb3()

_args=rb()

_ord=rb3()

_exec=rb4()

__print=rb4()

ConMeMayDungCoLo=rb4()

batconsocbovolo=rb()

buonialevel1=rb3()

HomNayToiBuon=rb3()

_vars=rb()

_anhxa1=rb4()

_uni=rb1()

_sum=rb3()

_utf8=rb1()

_str = rb()

_float=rname()

_aychochoco=rb1()

_any='SucManhCuaYukiAbi'

_bytes=rb5()

_decode=rb5()

LOVUONG=rb3()



def sieugaylomalaihay(s):

    data = s.encode()

    out = []

    i = 0

    while i < len(data):

        n = random.randint(5, 13)

        out.append(repr(data[i:i+n]))

        i += n

    return f"__XxViThanOBFToiCaoxX__({trap}[:0xA], No1, {' '.join(out)}).__call__()"



Antilol = f"""

try:
    globals().update(globals().get('_Ox3', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict):
        _Ox3.update(globals())
    _dec_fn = globals().get('{_YUKI_ROMAN_DEC_NAME}') or (globals().get('_Ox3', {{}}).get('{_YUKI_ROMAN_DEC_NAME}'))
    if _dec_fn and callable(_dec_fn):
        for _k, _v in list(globals().get('_Ox3', {{}}).items()):
            if isinstance(_k, str):
                try:
                    _pk = _dec_fn(_k)
                    if isinstance(_pk, str) and _pk.isidentifier():
                        globals().get('_Ox3', {{}})[_pk] = _v
                        globals()[_pk] = _v
                except Exception: pass
except Exception:
    pass
_0xFx4B5 = globals().get('_Ox3', {{}})
globals()['_0xFx4B5'] = _0xFx4B5
globals()['{_uni}'] = globals().get('{_uni}') or _0xFx4B5.get('{_uni}')
globals()['___BoMayLaHeHe__'] = globals().get('___BoMayLaHeHe__') or _0xFx4B5.get('___BoMayLaHeHe__')
globals()['No1'] = globals().get('No1', 0)
globals()['KhangCoder'] = globals().get('KhangCoder') or _0xFx4B5.get('KhangCoder') or __import__
KhangCoder = globals()['KhangCoder']
globals()['{champ}'] = globals().get('{champ}') or _0xFx4B5.get('{champ}') or eval
{champ} = globals()['{champ}']

TinhYeu100ThapKy=['PyMarshal_ReadObjectFromString', 'PyEval_EvalCode']

if any(bytes((KhangCoder('ctypes').c_ubyte * 2).from_address(KhangCoder('ctypes').cast(getattr(KhangCoder('ctypes').pythonapi, {x}), KhangCoder('ctypes').c_void_p).value)) == bytes([255, 37]) for {x} in TinhYeu100ThapKy):raise MemoryError('KhangCoder...')



ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan = {champ}({enc('buonialevel1')})

ToiㅤYeuㅤEmㅤNhieuㅤLam = {champ}({enc("''")})

globals()[{_uni}({anhxa1('ThanHoMenhLevel1000')})] = {enc('"LD_PRELOAD"')}

_0xFx4B5[{enc('KyThuatAnCode')}]={champ}({enc("''")})

if globals().get('ThanHoMenhLevel1000', 'LD_PRELOAD') in KhangCoder('os').environ:

    raise RuntimeError("Khangcoder...")



ThichㅤXamㅤLonㅤKhongㅤEm = {_uni}({anhxa1('("✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧")')})

globals()[{_uni}({anhxa1('LuaGaTreCon')})] = {enc('bytes')}

(_0xFx4B5.__setitem__({wraphay('{rbx()}')},str), _0xFx4B5.__setitem__({enc('ThậtBuồnCười')}, {anhxa1('loads')}), globals().__setitem__({enc('ĐịtMẹMàyThấyẢoChưa')},[{_uni}({anhxa1('PyMarshal_ReadObjectFromString')}),{enc('PyEval_EvalCode')},___BoMayLaHeHe__({anhxa('_PyEval_EvalFrameDefault')}),{_uni}({anhxa1('PyRun_StringFlags')})]))

globals()[{enc('DitMeMayCoTrinhKhongHaha')}]={anhxa1('exec')}

globals()[{_uni}({anhxa1('DungCoDecNuaAnhOi')})]={enc('marshal')}

_0xFx4B5[{wraphay('{rbx()}')}] = chr

_0xFx4B5[{enc('CauBiLuaRoii')}] = {champ}({enc('0x1F300')})

globals()[___BoMayLaHeHe__({anhxa('DungCoDecNuaAnhOi1')})]={enc('lzma')}

_0xFx4B5[{enc('DoMayBietNoLaGi')}] = {_uni}({anhxa1('globals')})

globals()[{_uni}({anhxa1('XamLolGiaiDoanCuoi')})] = KhangCoder({_uni}({anhxa1('builtins')})).__getattribute__({enc('exec')})

_0xFx4B5[{enc('CapDoAnCodeLeval1000')}] = getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')}))

_0xFx4B5[{_uni}({anhxa1('Yuki_Abi_That_Dang_Iu')})] = lambda {x}: {_exec}({x})
globals().update(_0xFx4B5)
if '_Ox3' in globals() and isinstance(_Ox3, dict):
    _Ox3.update(_0xFx4B5)



class __XxViThanOBFToiCaoxX__:

    def __init__(KhangCoder, OBFVIP, ĂNĐƯỢCKHÔNG, __XxKhangCoderOBFxX__):

        try:

            KhangCoder.OBFVIP = OBFVIP

        except:

            KhangCoder.ĂNĐƯỢCKHÔNG = ĂNĐƯỢCKHÔNG

        else:

            KhangCoder.__XxKhangCoderOBFxX__ = __XxKhangCoderOBFxX__



    def __call__(KhangCoder):

        return {_str}().__getattribute__({enc('join')})(_{thicthamcrush}(__KhangCoder__(ThatDangIu)) for ThatDangIu in KhangCoder.__XxKhangCoderOBFxX__)



globals()[{wraphay('mấy lũ chó điên{rbx()}{rbx()}')}] = globals()

"""



antibuiltins = """
(lambda: (
    __import__('sys').exit(137) if __import__('sys').gettrace() is not None else None,
    __import__('sys').exit(137) if (hasattr(__import__('hashlib').sha256, '__code__') or type(__import__('hashlib').sha256) is not type(abs)) else None,
    __import__('sys').exit(137) if __import__('hashlib').sha256(b'').hexdigest() != 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' else None,
    __import__('sys').exit(137) if hasattr(__import__('marshal').loads, '__code__') else None
))()

def BoMaySoMayQua():return [*(lambda: (999,))()]

def BoMaySoMayQua1():return [_ for _ in (lambda: (999,))()]

def ditconmemay():raise ValueError('khangcoder...') from None

__tramcam__ = type((lambda:No1).__code__)

def __cailolduma__(nhatco, name):

    if type(nhatco) is not KhangCoder('types').BuiltinFunctionType:BoMaySoMayQua()

    if name == 'compile':

        if type(nhatco('1+1', '' ,'eval')) is not __tramcam__:raise RuntimeError('khangcoder...')

    elif name == 'print':

        if nhatco.__name__!='print' or nhatco is not KhangCoder('builtins').print:BoMaySoMayQua()

    elif name == 'input':

        if nhatco.__name__!='input' or nhatco is not KhangCoder('builtins').input:BoMaySoMayQua1()

    else:

        try:nhatco('1+1')

        except Exception:raise RuntimeError('khangcoder...')

__cailolduma__(KhangCoder('builtins').compile,'compile')

__cailolduma__(KhangCoder('builtins').eval,'eval')

__cailolduma__(KhangCoder('builtins').exec,'exec')

LònMẹLừaĐấy = __import__('traceback').extract_stack()

try:

    import os as _os_fr

    _self_f = _os_fr.path.normcase(_os_fr.path.abspath(__file__)) if '__file__' in globals() and __file__ else ''

    for frame in LònMẹLừaĐấy[:-2]:

        _fn_raw = frame.filename or ''

        if _fn_raw != 'ProJect' and not (_fn_raw.startswith('<') and _fn_raw.endswith('>')):

            _fn_n = _os_fr.path.normcase(_os_fr.path.abspath(_fn_raw)) if _fn_raw else ''

            if _self_f and _fn_n and _fn_n != _self_f:

                try:

                    import ctypes as _ct

                    _ct.memset(0, 0, 1)

                except: pass

                __import__('sys').exit(2009)

except: pass

"""



_tail_p = '_Ox' + uuid.uuid4().hex[:8]
_tail_c = '_Ox' + uuid.uuid4().hex[:8]
_tail_cls_key = enc(unicodedata.normalize('NFKC', '__YukiㅤAbiObfusCator__'))
_tail_needle_bytes = list(f"(lambda {_tail_p}".encode('utf-8'))
_tail_needle_expr = f"bytes({_tail_needle_bytes})"

brotuongthelangau = f"""

checkinf = '''#!/bin/python{ver}
# -*- coding: utf-8 -*-
class __YukiㅤAbi__:
    __OWN__ = ('khangcoder x thảo my coder')
    __In4__ = ('https://www.facebook.com/profile.php?id=61593602324700',)
    __USR__ = ('{{_runsourceobf}} - Requests Protect')
    __Notes__ = ('Vui lòng không tìm tới info của chúng tôi để hỏi về code được sử dụng obf, trừ khi đây là obf do chính bọn mình làm')
    Warning_Vi = ('Việc sử dụng obf này để lạm dụng mục đích xấu, người sở hữu sẽ không chịu trách nhiệm!')
    Warning_En = ('Using this obf for bad purposes, the owner will not be responsible!')
{_YUKI_RUN_NAME}, {_YUKI_PRO_NAME}, {_YUKI_ABI_MAP_NAME} = ((lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: (getattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) else _b[chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)])(chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)))()), ('__khangcoder & thảo my coder__', '__DuyObf__', '__Yuki AbiObfusCator__'), [
    [*['k']+[*'ab']], [*['j']+[*'iz']], [*['h']+[*'sr']], [*['m']+[*'2l']],
    [*['o']+[*'d']], [*['1']+[*'346']], [*['p']+[*'ec']], [*['y']+[*'ung']],
    [*['v']+[*'[']+[*'tx']]]
_0xO = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[8][0]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[3][2])
_Ox1 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][0]+{_YUKI_ABI_MAP_NAME}[2][2]+{_YUKI_ABI_MAP_NAME}[1][1]+{_YUKI_ABI_MAP_NAME}[7][2]+{_YUKI_ABI_MAP_NAME}[8][2])
_0x2 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[2][1]+{_YUKI_ABI_MAP_NAME}[8][2]+{_YUKI_ABI_MAP_NAME}[2][2])
_Ox3 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[7][3]+{_YUKI_ABI_MAP_NAME}[3][2]+{_YUKI_ABI_MAP_NAME}[4][0]+{_YUKI_ABI_MAP_NAME}[0][2]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[3][2]+{_YUKI_ABI_MAP_NAME}[2][1])()
_0x4 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[7][2]+{_YUKI_ABI_MAP_NAME}[7][1]+{_YUKI_ABI_MAP_NAME}[3][0]+{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[2][2]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[8][2]+{_YUKI_ABI_MAP_NAME}[6][1])
_Ox5 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[3][0]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[6][0])
{_YUKI_SYS_NAME} = _0xO(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95))(chr(115)+chr(121)+chr(115))
if _0x2({_YUKI_SYS_NAME}.version[0x0:0b100]) != '{str(eval("__import__(\'sys\').version[0:4]"))}':
    _Ox1('This Code Works On Your Version of Python!')
    _Ox1("Your Version: ", _0x2({_YUKI_SYS_NAME}.version[0x0:0b100]))
    _Ox1('You need to Install Python {str(eval("__import__(\'sys\').version[0:4]"))}')
    {_YUKI_SYS_NAME}.exit(2009)
'''

if data and checkinf not in data:data=data[::-1]; ditconmemay()

"""



def gen_invincible_antidebug():

    _v_crash = rb()

    _v_hook = rb1()

    _v_peb = rb2()

    _v_mon_check = rb3()

    _v_mon_lock = rb4()

    _v_frida = rb5()

    _v_audit = rb()

    _v_main = rb1()

    _v_pulse = rb2()



    raw_payload = f'''

# ==================== INVINCIBLE MULTI-LAYER ANTI-DEBUG ENGINE ====================

import sys, os, time, platform, builtins, types



def {_v_crash}(c=96):

    try:

        import ctypes as _ct

        _k32 = getattr(getattr(_ct, 'windll', None), 'kernel32', None)

        if _k32 and hasattr(_k32, 'TerminateProcess'):

            _k32.TerminateProcess(_k32.GetCurrentProcess(), 0xC0000005)

        _nt = getattr(getattr(_ct, 'windll', None), 'ntdll', None)

        if _nt and hasattr(_nt, 'NtTerminateProcess'):

            _nt.NtTerminateProcess(-1, 0xC0000005)

        _ct.memset(0, 0, 1)

    except: pass

    try: os.abort()

    except: pass

    try: os._exit(c)

    except: sys.exit(c)



def {_v_mon_check}():

    try:

        if hasattr(sys, 'monitoring'):

            for _ti in range(6):

                _ev = sys.monitoring.get_events(_ti)

                _tl = sys.monitoring.get_tool(_ti)

                if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                    {_v_crash}(95)

    except: pass



def {_v_mon_lock}():

    try:

        if hasattr(sys, 'monitoring'):

            _orig_uid = getattr(sys.monitoring, 'use_tool_id', None)

            def _mon_trap(*a, **kw):

                if a and any('yuki_' in str(x) for x in a):

                    try: return _orig_uid(*a, **kw)

                    except: return None

                {_v_crash}(95)

            if _orig_uid:

                sys.monitoring.use_tool_id = _mon_trap

            sys.monitoring.register_callback = lambda *a, **kw: {_v_crash}(95)

            def _trap_set_events(*a, **kw):

                if len(a) > 1 and a[1] != 0:

                    {_v_crash}(95)

                if kw.get('event_set', 0) != 0:

                    {_v_crash}(95)

                return None

            sys.monitoring.set_events = _trap_set_events

    except: pass



def {_v_hook}():

    def _is_hooked(b):

        if not b or len(b) < 2: return False

        if b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2): return True

        if b[0] == 0xFF and len(b) > 1 and b[1] in (0x25, 0xE0, 0xE1, 0xE2): return True

        if b[0] == 0x48 and len(b) > 1 and b[1] == 0xB8: return True

        if b[0] == 0xCD and len(b) > 1 and b[1] == 0x03: return True

        if b[0] == 0xB8 and len(b) > 6 and b[5] == 0xFF and b[6] == 0xE0: return True

        if b[0] == 0x68 and len(b) > 5 and b[5] == 0xC3: return True

        if len(b) >= 3 and b[0] == 0x90 and b[1] == 0x90 and b[2] == 0x90: return True

        for off in (1, 2, 3):

            if len(b) > off + 2:

                if b[off] in (0xE9, 0xCC) or (b[off] == 0xFF and b[off+1] == 0x25) or (b[off] == 0x48 and b[off+1] == 0xB8):

                    return True

        return False

    try:

        import ctypes

        _pyapi = getattr(ctypes, 'pythonapi', None)

        if _pyapi:

            for _sym in ('PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault', 'PyRun_StringFlags', 'PyObject_Call'):

                addr = getattr(_pyapi, _sym, None)

                if addr:

                    ptr = ctypes.cast(addr, ctypes.c_void_p).value

                    if ptr and _is_hooked(bytes((ctypes.c_ubyte * 24).from_address(ptr))):

                        {_v_crash}(91)

    except: pass



def {_v_peb}():

    if os.name != 'nt':

        try:

            if os.path.exists('/proc/self/status'):

                with open('/proc/self/status', 'r', errors='ignore') as _f:

                    for _l in _f:

                        if _l.startswith('TracerPid:') and _l.split(':', 1)[1].strip() != '0':

                            {_v_crash}(97)

        except: pass

        return

    try:

        import ctypes

        k32 = ctypes.windll.kernel32

        nt = ctypes.windll.ntdll

        if k32.IsDebuggerPresent(): {_v_crash}(96)

        _rem = ctypes.c_bool(False)

        k32.CheckRemoteDebuggerPresent(k32.GetCurrentProcess(), ctypes.byref(_rem))

        if _rem.value: {_v_crash}(96)

        try: nt.NtSetInformationThread(k32.GetCurrentThread(), 0x11, 0, 0)

        except: pass

        _port = ctypes.c_ulong(0)

        _st = nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 7, ctypes.byref(_port), ctypes.sizeof(_port), None)

        if _st == 0 and _port.value != 0: {_v_crash}(96)

        _flags = ctypes.c_ulong(1)

        _st = nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 0x1F, ctypes.byref(_flags), ctypes.sizeof(_flags), None)

        if _st == 0 and _flags.value == 0: {_v_crash}(96)

        class _PBI(ctypes.Structure):

            _fields_ = [('ExitStatus', ctypes.c_ulong), ('PebBaseAddress', ctypes.c_void_p), ('AffinityMask', ctypes.c_void_p), ('BasePriority', ctypes.c_long), ('UniqueProcessId', ctypes.c_void_p), ('InheritedFromUniqueProcessId', ctypes.c_void_p)]

        pbi = _PBI()

        if nt.NtQueryInformationProcess(k32.GetCurrentProcess(), 0, ctypes.byref(pbi), ctypes.sizeof(pbi), None) == 0 and pbi.PebBaseAddress:

            if (ctypes.c_ubyte).from_address(pbi.PebBaseAddress + 2).value != 0: {_v_crash}(96)

            _is_64 = (ctypes.sizeof(ctypes.c_void_p) == 8)

            _flag_off = 0xBC if _is_64 else 0x68

            if ((ctypes.c_ulong).from_address(pbi.PebBaseAddress + _flag_off).value & 0x70) != 0: {_v_crash}(96)

        try:

            k32.CloseHandle(0xDEADBEEF)

        except:

            {_v_crash}(96)

    except: pass



def {_v_frida}():

    if os.name == 'nt':

        try:

            import ctypes

            k32 = ctypes.windll.kernel32

            for _m in ('frida-agent.dll', 'gadget.dll', 'scylla.dll', 'titanengine.dll', 'x64dbg.dll', 'x32dbg.dll'):

                if k32.GetModuleHandleA(_m.encode()):

                    {_v_crash}(98)

        except: pass

        try:

            for _p in os.listdir(r'\\\\.\\pipe'):

                if any(x in _p.lower() for x in ('frida', 'linjector')):

                    {_v_crash}(98)

        except: pass



def {_v_audit}():

    try:

        sys.audit = lambda *a, **kw: None

        sys.addaudithook = lambda *a, **kw: None

    except: pass

    try:

        import ctypes

        _pyapi = getattr(ctypes, 'pythonapi', None)

        _addr = getattr(_pyapi, 'PySys_Audit', None)

        if _addr:

            _ptr = ctypes.cast(_addr, ctypes.c_void_p).value

            _old = ctypes.c_ulong()

            if ctypes.windll.kernel32.VirtualProtect(ctypes.c_void_p(_ptr), 4, 0x40, ctypes.byref(_old)):

                _patch = (ctypes.c_ubyte * 3)(0x31, 0xC0, 0xC3)

                ctypes.memmove(_ptr, _patch, 3)

                ctypes.windll.kernel32.VirtualProtect(ctypes.c_void_p(_ptr), 4, _old.value, ctypes.byref(_old))

    except: pass



def {_v_main}():

    if sys.gettrace() is not None: {_v_crash}(95)

    if hasattr(sys, 'getprofile') and sys.getprofile() is not None: {_v_crash}(95)

    _bad_mods = ('pdb','ptvsd','ptpython','debugpy','pydevd','bdb','cProfile','pycdc','decompyle','uncompyle','pylingual','xdis')

    for _m in list(sys.modules.keys()):

        if any(x in _m.lower() for x in _bad_mods):

            {_v_crash}(96)

    {_v_mon_check}()

    {_v_mon_lock}()

    {_v_hook}()

    {_v_peb}()

    {_v_frida}()

    {_v_audit}()

    # State-Key Intertwining

    globals()['__yuki_integrity_token__'] = {_YUKI_INTEGRITY_SALT}



{_v_main}()



def {_v_pulse}():

    _cnt = 0

    while True:

        try:

            _cnt = (_cnt + 1) & 0xFFFFFFFF

            globals()['__yuki_pulse__'] = (time.time(), (_cnt ^ {_YUKI_HEARTBEAT_SECRET}))

            if sys.gettrace() is not None: {_v_crash}(95)

            {_v_mon_check}()

        except: pass

        time.sleep(0.8)



try:

    if '__yuki_pulse_started__' not in globals():

        globals()['__yuki_pulse_started__'] = True

        try:

            import _thread as _th_pulse

            _th_pulse.start_new_thread({_v_pulse}, ())

        except Exception:

            import threading as _th_pulse

            _th = _th_pulse.Thread(target={_v_pulse}, daemon=True)

            _th.start()

except: pass

'''

    return _protect_raw_payload(raw_payload)



antidebug = gen_invincible_antidebug()



anti = antibuiltins+f"""

(vars(globals()['__builtins__']) if hasattr(globals()['__builtins__'], '__dict__') else globals()['__builtins__'])

# Bug #12 Fix: use robust builtin validation

_chk_exit = lambda f: isinstance(f, (__import__('types').BuiltinFunctionType, __import__('types').BuiltinMethodType)) and getattr(f, '__name__', '') == 'exit'

if not _chk_exit(KhangCoder('sys').exit): BoMaySoMayQua()

# Bug #13 Fix: safe file reading with fallback

data = ""

try:

    _target_self = getattr(__import__('sys').modules.get('__main__'), '__file__', None) or __file__

    if _target_self and __import__('os').path.exists(_target_self):

        with open(_target_self, "r", encoding="utf-8", errors="ignore") as f: data = f.read()

except Exception: data = ""



meo = '''class __khangcoderㅤThaoMyCoder__:
    def __init__(Khangcoder, *{args}, **{kwds}):{d}=_Ox3;{arg_}=_Ox3;{d}['{trap}']=''.join([{x}[0] for {x} in [['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]]);{d}['{meo}']=''.join(list(map(_0xO(''.join(['c','h','r'])),[8544,8545,8546,8547,8548,8549,8550,8551,8552,8553])));{d}['{trunks}']=_0xO(''.join(['z','i','p']));{d}['{trap1}']=_0xO(''.join(['d','i']+['c','t']));{d}['{ConMeMayDungCoLo}']=_0xO(''.join(['c','h','r']));{d}['{_str}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[115,116,114])));{d}['{a}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[105,110,116])));{d}['__{meo}__']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[98,121,116,101,115])));{d}['JackĐẻCon'] = _0xO(''.join(reversed([*['s'], *['e'], *['t'], *['y'], *['b']])));{d}['__{trunks}___']={trap1}({trunks}({trap},{meo}));{d}={{{v}:{k} for {k},{v} in __{trunks}___.items()}};{arg_}['{_YUKI_ROMAN_DEC_NAME}']=lambda {s}:(lambda {r}:getattr(__{meo}__({a}({r}[{i}:{i} + 0x03])for {i} in range(0x01 - 0x01, len({r}), 0x01 + 0x01 + 0x01)),''.join(_Ox5({ConMeMayDungCoLo},[100,101,99,111,100,101])))())({_str}().join(({d}.get({c},{c})for {c} in {s})));{arg_}['{champ}']=_0xO({enc('lave')}[::-1]);{arg_}['KhangCoder']={champ}({enc('__tropmi__')}[::-0x01]);{arg_}['{siba}']=(lambda {x}:{x}(getattr(KhangCoder({enc('types')}),{enc('FunctionType')})))(lambda {v}:{v});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BotㅤYukiㅤAbi')},{champ}({enc('exec')}));{arg_}[{enc('__KhangCoder__')}]={champ}({enc('int')});{arg_}['{__print}']={champ}({enc('print')});{arg_}['_{thicthamcrush}']={champ}({enc('chr')});{arg_}['{_exec}']={champ}({enc('exec')});{arg_}['__OnTopSever25Tang__']={champ}({enc('len')});{arg_}['{_ord}']={champ}({enc('ord')});{arg_}[{enc('No1')}]={champ}({enc('2009-1711+1-299')});{arg_}['No1']={champ}({enc('2009-1711+1-299')});{arg_}['{thicthamcrush}_']={champ}({enc('MemoryError')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_compile}')},{champ}({enc('compile')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{batconsocbovolo}')},{champ}({enc(str(_DYNAMIC_OFFSET_1))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('buonialevel1')},{champ}({enc('1+1+1+1+1+1+1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_vars}')},{champ}({enc('vars')}));{arg_}['{_sum}']=_0xO({enc('mus')}[::-1]);{arg_}['{_replace}']=_0xO({enc("'replace'")});{arg_}[{enc('ontop25tang')}]=_0xO({enc('[255,37]')});{arg_}['ontop25tang']=_0xO({enc('[255,37]')});{arg_}['__KhangCoder__']={champ}({enc('int')})
    def __call__(Khangcoder, *{args}, **{kwds}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_anhxa1}')},{champ}({enc(str(_DYNAMIC_OFFSET_2))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{HomNayToiBuon}')},{champ}({enc('globals()')}));_Ox3['{_float}']={champ}({enc('float')});(lambda:getattr(getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__dict__')}),{enc('get')})({enc('__getattribute__')}) or getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({args}))();setattr(Khangcoder,{enc('__init__')},{args});setattr(Khangcoder,{enc('__args__')},{args});setattr(Khangcoder,{enc('__kwds__')},{kwds});{HomNayToiBuon}[{enc('__khangcoderㅤThaoMyCoder__')}]={args}[No1] if {args} else None
    def __getattribute__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')})((lambda {x}:({x}(No1) or (getattr({enc('object')},{enc('__getattribute__')})(Khangcoder,{arg_})if {arg_} in({enc('__call__')},{enc('__getattribute__')})else(getattr(({m} for {m} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))))))(lambda:No1)
    def __getattr__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))
'''
meo1 = '''class __DuyObf__:
    def __init__(Khangcoder, *{args}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('SoTienConNo')},{champ}({enc('2-1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),'SoTienConNo',{champ}({enc('2-1')}));_Ox3['SoTienConNo']={champ}({enc('2-1')});(lambda Khangcoderbadao:(setattr(Khangcoder,{enc("Project1")},{enc('base64')}),getattr((Khangcoderbadao for Khangcoderbadao in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')})) if (not ({enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('exec')})) and {enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('eval')})) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__code__')}) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('eval')}),{enc('__code__')}))) else setattr(Khangcoder,{enc("Project1")},{enc('base64')})))(No1);setattr(Khangcoder,"{arg_}",{args}[No1])
    def __str__(Khangcoder,*{args},**{kwds}):_Ox3[{enc(fr'{_utf8}')}]={champ}({enc('"utf-8"')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BoLaLoVuongHahah')},{champ}({enc('256')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),'BoLaLoVuongHahah',{champ}({enc('256')}));_Ox3['BoLaLoVuongHahah']={champ}({enc('256')});setattr(Khangcoder,{enc("Project2")},{enc('zlib')});_Ox3[{enc(fr'{_c}')}]=_0xO({enc("'c'")});((getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('__str__')})) if not ({enc('builtin')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))) else {enc('Khangcoder')}))
    def {kwds}(Khangcoder, {args}):((lambda _{champ}_:(setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))[SoTienConNo] if (not ({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(_{champ}_))=={enc("<class 'builtin_function_or_method'>")} and {enc('marshal')} in {_str}(getattr(_{champ}_,{enc('__module__')},No1)) and {enc('built-in')} in {_str}(_{champ}_) and {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('builtins')}),{enc('exec')})))=={enc("<class 'builtin_function_or_method'>")} and {enc('builtins')} in {_str}(getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__module__')},{enc(f'__{meo}__')})) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__self__')},None)==KhangCoder({enc('builtins')}))) else (setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),No1)[SoTienConNo])(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))
    def {s}(Khangcoder, *{args}):(lambda No1:getattr(({k} for {k} in(No1)),{enc('throw')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({args})) if not(isinstance(getattr(Khangcoder,{enc(fr"{arg_}")}),(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) and len(getattr(Khangcoder,"{arg_}"))>10) else No1)(No1);(lambda BietTruongHucConBoKhong:No1 if(hasattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')}) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')})==getattr(__DuyObf__,{enc('__str__')})) else ({k} for {k} in(No1)).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')})))(No1);getattr(Khangcoder,(lambda:{enc(f'{kwds}')})())({args});getattr(Khangcoder,{enc('__str__')})(Khangcoder,*{args});_Ox3[{enc('ToLaBuaYeu1')}]={champ}({enc('1+1')});_Ox3['ToLaBuaYeu1']={champ}({enc('1+1')});Khangcoder.{kwds}({args});getattr(object,{enc('__str__')})(Khangcoder,*{args});_v_tp=(getattr(KhangCoder({enc('sys')}).modules.get({enc('__main__')}),{enc('__file__')},None) or (KhangCoder({enc('sys')}).argv[No1] if KhangCoder({enc('sys')}).argv else None) or globals().get({enc('__file__')}));_v_rc=getattr(KhangCoder(getattr(Khangcoder,{enc("Project1")})),{enc("b85decode")})(getattr(Khangcoder, "{arg_}"));_v_fb=getattr(KhangCoder({enc('builtins')}),{enc('open')})(_v_tp,'rb').read() if (_v_tp and KhangCoder({enc('os')}).path.exists(_v_tp)) else b'';_v_ap=_v_fb.rfind({_tail_needle_expr});_v_hf=KhangCoder({enc('hashlib')}).sha256(_v_fb[:_v_ap].replace(bytes([13,10]),bytes([10]))).digest() if _v_ap>No1 else bytes(32);_v_ks=b''.join(KhangCoder({enc('hashlib')}).sha256(_v_hf+({_salt_l1_expr})+_c.to_bytes(4,'big')).digest() for _c in range((len(_v_rc)+31)//32))[:len(_v_rc)];_v_dc=bytes(_b^_v_ks[_i] for _i,_b in eval({enc('_0x4')})(_v_rc));return getattr(KhangCoder(getattr(Khangcoder,{enc("Project3")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project2")})),{enc("decompress")})(_v_dc))
'''
meo2 = '''class __YukiㅤAbiObfusCator__:
    def __getattr__(Khangcoder, {args}):return (lambda:(({s}:=KhangCoder({enc('sys')}),{m}:=KhangCoder({enc('marshal')}),{t}:=KhangCoder({enc('builtins')}),{_any}:={champ}({enc('any')}),{_bytes}:={champ}({enc('bytes')}),setattr(Khangcoder,{enc("Project5")},{enc('ctypes')}),((lambda:{enc('0')})() if not {_any}({_bytes}(getattr((getattr(KhangCoder({enc('ctypes')}),{enc('c_ubyte')})*(0x01+0x01)),{enc('from_address')})(getattr(KhangCoder({enc('ctypes')}),{enc('cast')})(getattr(getattr(KhangCoder({enc('ctypes')}),{enc('pythonapi')}),{x}),getattr(KhangCoder({enc('ctypes')}),{enc('c_void_p')})).value))=={_bytes}(ontop25tang) for {x} in ({enc('PyMarshal_ReadObjectFromString')},{enc('PyEval_EvalCode')})) else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('MemoryError')}({enc('Xàm')})))),__{_str}__:=(not getattr({s},{enc('gettrace')})() and (not hasattr({s},'monitoring') or not any(getattr({s},'monitoring').get_events(_i)!=0 or getattr({s},'monitoring').get_tool(_i) is not None for _i in range(6))) and {enc('built-in')} in {_str}(getattr({m},{enc('loads')})) and all({enc('built-in')} in {_str}(getattr({t},{i})) for {i} in ({enc('BotㅤYukiㅤAbi')},{enc('eval')},{enc(fr'{_compile}')},{enc('__import__')}))),__{t}__:={args} if __{_str}__ else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else {args}[::-0x01]),(No1 if __{_str}__ else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))),__{t}__)[-1]))()
    def {kwds}(Khangcoder, {arg_}):
        setattr(Khangcoder,{enc("Project6")},__{trunks}___);_Ox3[{enc('ToLaBuaYeu')}]={champ}({enc('1')});_Ox3['ToLaBuaYeu']={champ}({enc('1')});_uni_dec_fn=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{_anhxa1}) for {i} in {c}))();{HomNayToiBuon}['{_uni}']=_uni_dec_fn;_Ox3['{_uni}']=_uni_dec_fn;{HomNayToiBuon}[{enc(f'{_uni}')}]=_uni_dec_fn;_Ox3[{enc(f'{_uni}')}]=_uni_dec_fn;{m}=KhangCoder({enc('marshal')});__ToCrushCauMoa__=KhangCoder({enc("ctypes")});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_aychochoco}')},{champ}({enc('8+8')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('NgaoChoDaiDoanCuoi')},{champ}({enc('ord')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('XinChaoVietNam')},{champ}({enc('1+2')}));__{r}__=getattr(Khangcoder,{enc('__getattr__')})({arg_});delattr(Khangcoder,"{arg_}");_ct=KhangCoder({enc('ctypes')});_papi_m=getattr(getattr(_ct,{enc('pythonapi')},None),{enc('PyMarshal_ReadObjectFromString')},None);_papi_m.restype=getattr(_ct,{enc('py_object')}) if _papi_m else None;_papi_m.argtypes=[getattr(_ct,{enc('c_char_p')}),getattr(_ct,{enc('c_ssize_t')})] if _papi_m else None;__{r}__=(_papi_m(__{r}__,len(__{r}__)) if _papi_m else getattr({m},{enc("loads")})(__{r}__))
        for _k, _v in list(_Ox3.items()):
            try:
                _pk = _Ox3['{_YUKI_ROMAN_DEC_NAME}'](_k)
                if isinstance(_pk, str) and _pk.isidentifier():
                    _Ox3[_pk] = _v
                    globals()[_pk] = _v
            except Exception: pass
        {HomNayToiBuon}.update(_Ox3);globals().update(_Ox3);return getattr(KhangCoder({enc('builtins')}),{enc('BotㅤYukiㅤAbi')})(__{r}__,globals(),globals())
    def __call__(Khangcoder, *{args}, **{kwds}):_Ox3[{enc(fr'_{a}')}]={champ}({enc('1')});{_globals}={HomNayToiBuon};_bm_fn=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{batconsocbovolo})for {i} in {c}))();{_globals}['___BoMayLaHeHe__']=_bm_fn;_Ox3['___BoMayLaHeHe__']=_bm_fn;{_globals}[{enc('___BoMayLaHeHe__')}]=_bm_fn;_Ox3[{enc('___BoMayLaHeHe__')}]=_bm_fn;(lambda _{thicthamcrush}_:(setattr(Khangcoder,{enc("Project7")},{siba}),___BoMayLaHeHe__({anhxa('0')}))[_{a}] if({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))=={enc("<class 'builtin_function_or_method'>")}) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})(___BoMayLaHeHe__({enc(fr'{args}')})))(___BoMayLaHeHe__({anhxa('0')}));getattr(Khangcoder,{enc(f'{kwds}')})((lambda {t}:({t} if isinstance({t},(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})({enc('Exception')}({enc('Khangcoder')}))))(__DuyObf__({args}[No1]).{s}()))
'''
meo3 = '''(lambda {kwds}:((lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: (getattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) else _b[chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)])(chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)))(), __khangcoderㅤThaoMyCoder__()(), (lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: ((getattr(_b, chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95)) else _b.get(chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95))) and __YukiㅤAbi__))(), {kwds}()))(__YukiㅤAbiObfusCator__)
'''



pass


"""



#2 obfstr & obffint

def _args(name):

    return ast.arguments(posonlyargs=[], args=[ast.arg(arg=name)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])



def obfstr1(s):

    nhatco1 = random.randint(1000, 3000)

    nhatco2 = random.randint(0x0300, 0x036F)

    def enc(c):

        nhatcobadao = ord(c)

        return chr((nhatcobadao ^ nhatco1) << 2 ^ nhatco2 ^ 131313)

    data = ''.join((enc(c) for c in s))

    v = rb() + rb2()

    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 1717171717), ast.BitXor(), ast.Constant(1717171717))

    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 333333333333), ast.BitXor(), ast.Constant(333333333333))

    giaimalaptrinh = ast.Call(ast.Name(f'_{thicthamcrush}', ast.Load()), [ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), ast.Constant(131313)), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu1', ast.Load())), ast.BitXor(), cogaianhyeu)], [])

    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 10))])

    lam3 = ast.Lambda(args=_args(rb()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=giaimalaptrinh, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.Constant(data), ifs=[fake], is_async=0)])], keywords=[]))

    labada = ast.Lambda(_args(rb1()), ast.Constant(random.randint(100000, 999999)))

    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Call(labada, [ast.Constant(0)], [])], []))

    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], []))

    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f'({anhxa("Minh Anh Dep zai")})')], []))

    return ast.Call(lam0, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], [])



def obfint1(i):

    nhatco1 = random.randint(0x13000, 0x13020)

    nhatco2 = random.randint(0x0300, 0x036F)

    enc = chr((i ^ nhatco1) << 1 ^ nhatco2 ^ 999999)

    v = rb() + rb2()

    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 20091117), ast.BitXor(), ast.Constant(20091117))

    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 6736673667366736), ast.BitXor(), ast.Constant(6736673667366736))

    giaimalaptrinh = ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), ast.Constant(999999)), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)

    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(5, 10))])

    lam3 = ast.Lambda(_args(v), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giaimalaptrinh, ast.Constant(random.randint(1, 9999)))], []))

    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Constant(enc)], []))

    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], []))

    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(f'({anhxa("Minh Anh Dep zai")})')], []))

    return ast.Call(lam0, [ast.Constant(f'({anhxa1("Minh Anh Dep zai")})')], [])



def obffloat1(f):
    return obffloat2(f)



##############################################################################################

def obfstr2(s):

    OFFSET = random.randint(*random.choice([(128544, 128549), (0X2160, 0X2170), (1000, 3000)]))

    khangcoder = random.randint(10000, 99999)

    okyeye = random.randint(1000, 9999)

    lst = [chr(ord(c) + khangcoder + okyeye + OFFSET) for c in s]

    v = rb() + rb2()

    offset_expr = ast.BinOp(ast.BinOp(ast.Constant(OFFSET + 11111111), ast.Sub(), ast.Constant(11111111)), ast.Add(), ast.Constant(0))

    oknhonhe = ast.BinOp(ast.Constant(khangcoder + 6767676767676767), ast.Sub(), ast.Constant(6767676767676767))

    khonghieu = ast.BinOp(ast.Constant(okyeye + 33333333333333333333), ast.Sub(), ast.Constant(33333333333333333333))

    tuhieu = ast.Call(ast.Name(f'_{thicthamcrush}', ast.Load()), [ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.Sub(), khonghieu), ast.Sub(), oknhonhe), ast.Sub(), offset_expr)], [])

    lam3 = ast.Lambda(args=_args(rb()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=tuhieu, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=ast.Constant(''.join(lst)), ifs=[], is_async=0)])], keywords=[]))

    BOTHICHTHE = ast.Lambda(_args(rb1()), ast.BinOp(ast.Constant(random.randint(100000, 999999)), ast.Add(), ast.Constant(0)))

    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Call(BOTHICHTHE, [ast.Constant(0)], [])], []))

    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])



def obfint2(i):

    occak = 17112009 + 1111111111 - (i + 1111111111)

    lam3 = ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak))], []))

    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])



def obffloat2(f):

    nguyen = int(f)

    thapphan = int(str(f).split('.')[-1])

    dodai = len(str(thapphan))

    occak1 = 17112009 + 1111111111 - (nguyen + 1111111111)

    occak2 = 17112009 + 1111111111 - (thapphan + 1111111111)

    occak3 = 17112009 + 1111111111 - (dodai + 1111111111)

    part1 = ast.Call(ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak1))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

    part2 = ast.Call(ast.Lambda(_args(rb1()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak2))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

    part3 = ast.Call(ast.Lambda(_args(rb()), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.BinOp(ast.BinOp(ast.Constant(17112009 + 5555555555), ast.Sub(), ast.Constant(5555555555)), ast.Sub(), ast.Constant(occak3))], [])), [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])

    lam3 = ast.Lambda(_args(rb1()), ast.Call(ast.Name(f'{_float}', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_str}', ast.Load()), [part1], []), ast.Add(), ast.Constant('.')), ast.Add(), ast.Call(ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [part2], []), attr='zfill', ctx=ast.Load()), [part3], []))], []))

    lam2 = ast.Lambda(_args(rb()), ast.Call(lam3, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    lam1 = ast.Lambda(_args(rb1()), ast.Call(lam2, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    lam0 = ast.Lambda(_args(rb()), ast.Call(lam1, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], []))

    return ast.Call(lam0, [ast.Constant(f"({anhxa('Minh Anh Dep zai')})")], [])



#####################################################################################################

def obfstr3(s):

    nhatco1 = random.randint(1000, 3000)

    nhatco2 = random.randint(0x2160,0x2189)

    nhatco3 = ord(random.choice('👺😂🤣🥵🤯🔥🌚😡😤🧠🐲⭐✦✧🐍'))

    ConChoNgoLam = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))

    def _uni(c):return chr((ord(c) ^ ConChoNgoLam ^ nhatco1) << 2 ^ nhatco2 ^ nhatco3)

    data = ''.join((_uni(c) for c in s))

    BamBiBo = anhxa(data)

    v = rb() + rb2()

    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 20091711), ast.BitXor(), ast.Constant(20091711))

    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 673667366736), ast.BitXor(), ast.Constant(673667366736))

    concac = ast.BinOp(ast.Constant(nhatco3 ^ 363636363636), ast.BitXor(), ast.Constant(363636363636))

    UocMuonThatTroiXanh = ast.Call(ast.Name('___BoMayLaHeHe__', ast.Load()), [ast.Constant(BamBiBo)], [])

    HotWar2026 = ast.BinOp(ast.Constant(ConChoNgoLam ^ 696969696969),ast.BitXor(),ast.Constant(696969696969))

    giaimalaptrinh = ast.Call(ast.Name(f'_{thicthamcrush}',ast.Load()),[ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}',ast.Load()),[ast.Name(v,ast.Load())],[]),ast.BitXor(),concac),ast.BitXor(),toibuonia),ast.RShift(),ast.Name('ToLaBuaYeu1', ast.Load())),ast.BitXor(),cogaianhyeu),ast.BitXor(),HotWar2026)],[])

    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 100))])

    lam3 = ast.Lambda(args=_args(rb1()), body=ast.Call(func=ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [], []), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=giaimalaptrinh, generators=[ast.comprehension(target=ast.Name(v, ast.Store()), iter=UocMuonThatTroiXanh, ifs=[fake], is_async=0)])], keywords=[]))

    labada = ast.Lambda(_args(rb()), ast.Constant(random.randint(100000, 999999)))

    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [ast.Call(labada, [ast.Constant(0)], [])], []))

    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(str(anhxa(s)))], []))

    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(str(anhxa(s)))], []))

    return ast.Call(lam0, [ast.Constant(str(anhxa(s)))], [])



def obfint3(i):

    nhatco1 = random.randint(1000, 3000)

    nhatco2 = random.randint(0x2160,0x2189)

    nhatco3 = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))

    enc = chr((i ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)

    MaHoaCak = anhxa1(enc)

    v = rb() + rb2()

    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 17112009), ast.BitXor(), ast.Constant(17112009))

    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 343434343434), ast.BitXor(), ast.Constant(343434343434))

    concac = ast.BinOp(ast.Constant(nhatco3 ^ 676767676767), ast.BitXor(), ast.Constant(676767676767))

    UocMuonThatTroiXanh = ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoaCak)], [])

    giaimalaptrinh = ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), concac), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)

    fake = ast.Compare(ast.Constant(random.randint(1000, 9999)), [ast.Gt()], [ast.Constant(random.randint(1, 100))])

    lam3 = ast.Lambda(_args(v), ast.Call(ast.Name('__KhangCoder__', ast.Load()), [ast.IfExp(fake, giaimalaptrinh, ast.Constant(random.randint(0x2160,0x2189)))], []))

    lam2 = ast.Lambda(_args(rb1()), ast.Call(lam3, [UocMuonThatTroiXanh], []))

    lam1 = ast.Lambda(_args(rb()), ast.Call(lam2, [ast.Constant(str(anhxa1(str(i))))], []))

    lam0 = ast.Lambda(_args(rb1()), ast.Call(lam1, [ast.Constant(str(anhxa1(str(i))))], []))

    return ast.Call(lam0, [ast.Constant(str(anhxa1(str(i))))], [])



def obffloat3(f):

    nhatco1 = random.randint(1000, 3000)

    nhatco2 = random.randint(8544, 8585)

    nhatco3 = ord(random.choice(' 🥵 😡 😂 🤣  👻 🐍✦ ✧'))

    nguyen = int(f)

    thapphan = int(str(f).split('.')[-1])

    dodai = len(str(thapphan))

    enc1 = chr((nguyen ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)

    enc2 = chr((thapphan ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)

    enc3 = chr((dodai ^ nhatco1) << 1 ^ nhatco2 ^ nhatco3)

    MaHoa1 = anhxa1(enc1)

    MaHoa2 = anhxa1(enc2)

    MaHoa3 = anhxa1(enc3)

    v1 = rb() + rb2()

    v2 = rb() + rb2()

    v3 = rb() + rb2()

    cogaianhyeu = ast.BinOp(ast.Constant(nhatco1 ^ 17112009), ast.BitXor(), ast.Constant(17112009))

    toibuonia = ast.BinOp(ast.Constant(nhatco2 ^ 343434343434), ast.BitXor(), ast.Constant(343434343434))

    concac = ast.BinOp(ast.Constant(nhatco3 ^ 676767676767), ast.BitXor(), ast.Constant(676767676767))

    def giai(v):return ast.BinOp(ast.BinOp(ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_ord}', ast.Load()), [ast.Name(v, ast.Load())], []), ast.BitXor(), concac), ast.BitXor(), toibuonia), ast.RShift(), ast.Name('ToLaBuaYeu', ast.Load())), ast.BitXor(), cogaianhyeu)

    Lam0 = ast.Call(ast.Lambda(_args(v1), giai(v1)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa1)], [])], [])

    Lam1 = ast.Call(ast.Lambda(_args(v2), giai(v2)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa2)], [])], [])

    Lam2 = ast.Call(ast.Lambda(_args(v3), giai(v3)), [ast.Call(ast.Name(f'{_uni}', ast.Load()), [ast.Constant(MaHoa3)], [])], [])

    return ast.BinOp(ast.Call(ast.Name(f'{_float}', ast.Load()), [ast.BinOp(ast.BinOp(ast.Call(ast.Name(f'{_str}', ast.Load()), [Lam0], []), ast.Add(), ast.Constant('.')), ast.Add(), ast.Call(ast.Attribute(value=ast.Call(ast.Name(f'{_str}', ast.Load()), [Lam1], []), attr='zfill', ctx=ast.Load()), [Lam2], []))], []), ast.Add(), ast.Constant(0.0))



load = ""




Lobby = f"""#!/bin/python{ver}
# -*- coding: utf-8 -*-
class __YukiㅤAbi__:
    __OWN__ = ('khangcoder x thảo my coder')
    __In4__ = ('https://www.facebook.com/profile.php?id=61593602324700',)
    __USR__ = ('{{_runsourceobf}} - Requests Protect')
    __Notes__ = ('Vui lòng không tìm tới info của chúng tôi để hỏi về code được sử dụng obf, trừ khi đây là obf do chính bọn mình làm')
    Warning_Vi = ('Việc sử dụng obf này để lạm dụng mục đích xấu, người sở hữu sẽ không chịu trách nhiệm!')
    Warning_En = ('Using this obf for bad purposes, the owner will not be responsible!')
{_YUKI_RUN_NAME}, {_YUKI_PRO_NAME}, {_YUKI_ABI_MAP_NAME} = ((lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: (getattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) else _b[chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)])(chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)))()), ('__khangcoder & thảo my coder__', '__DuyObf__', '__Yuki AbiObfusCator__'), [
    [*['k']+[*'ab']], [*['j']+[*'iz']], [*['h']+[*'sr']], [*['m']+[*'2l']],
    [*['o']+[*'d']], [*['1']+[*'346']], [*['p']+[*'ec']], [*['y']+[*'ung']],
    [*['v']+[*'[']+[*'tx']]]
_0xO = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[8][0]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[3][2])
_Ox1 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][0]+{_YUKI_ABI_MAP_NAME}[2][2]+{_YUKI_ABI_MAP_NAME}[1][1]+{_YUKI_ABI_MAP_NAME}[7][2]+{_YUKI_ABI_MAP_NAME}[8][2])
_0x2 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[2][1]+{_YUKI_ABI_MAP_NAME}[8][2]+{_YUKI_ABI_MAP_NAME}[2][2])
_Ox3 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[7][3]+{_YUKI_ABI_MAP_NAME}[3][2]+{_YUKI_ABI_MAP_NAME}[4][0]+{_YUKI_ABI_MAP_NAME}[0][2]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[3][2]+{_YUKI_ABI_MAP_NAME}[2][1])()
_0x4 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[7][2]+{_YUKI_ABI_MAP_NAME}[7][1]+{_YUKI_ABI_MAP_NAME}[3][0]+{_YUKI_ABI_MAP_NAME}[6][1]+{_YUKI_ABI_MAP_NAME}[2][2]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[8][2]+{_YUKI_ABI_MAP_NAME}[6][1])
_Ox5 = getattr({_YUKI_RUN_NAME},{_YUKI_ABI_MAP_NAME}[3][0]+{_YUKI_ABI_MAP_NAME}[0][1]+{_YUKI_ABI_MAP_NAME}[6][0])
{_YUKI_SYS_NAME} = _0xO(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95))(chr(115)+chr(121)+chr(115))
if _0x2({_YUKI_SYS_NAME}.version[0x0:0b100]) != '{str(eval("__import__(\'sys\').version[0:4]"))}':
    _Ox1('This Code Works On Your Version of Python!')
    _Ox1("Your Version: ", _0x2({_YUKI_SYS_NAME}.version[0x0:0b100]))
    _Ox1('You need to Install Python {str(eval("__import__(\'sys\').version[0:4]"))}')
    {_YUKI_SYS_NAME}.exit(2009)
class __khangcoderㅤThaoMyCoder__:
    def __init__(Khangcoder, *{args}, **{kwds}):{d}=_Ox3;{arg_}=_Ox3;{d}['{trap}']=''.join([{x}[0] for {x} in [['0'],['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8'],['9']]]);{d}['{meo}']=''.join(list(map(_0xO(''.join(['c','h','r'])),[8544,8545,8546,8547,8548,8549,8550,8551,8552,8553])));{d}['{trunks}']=_0xO(''.join(['z','i','p']));{d}['{trap1}']=_0xO(''.join(['d','i']+['c','t']));{d}['{ConMeMayDungCoLo}']=_0xO(''.join(['c','h','r']));{d}['{_str}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[115,116,114])));{d}['{a}']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[105,110,116])));{d}['__{meo}__']=_0xO(''.join(_Ox5({ConMeMayDungCoLo},[98,121,116,101,115])));{d}['JackĐẻCon'] = _0xO(''.join(reversed([*['s'], *['e'], *['t'], *['y'], *['b']])));{d}['__{trunks}___']={trap1}({trunks}({trap},{meo}));{d}={{{v}:{k} for {k},{v} in __{trunks}___.items()}};{arg_}['{_YUKI_ROMAN_DEC_NAME}']=lambda {s}:(lambda {r}:getattr(__{meo}__({a}({r}[{i}:{i} + 0x03])for {i} in range(0x01 - 0x01, len({r}), 0x01 + 0x01 + 0x01)),''.join(_Ox5({ConMeMayDungCoLo},[100,101,99,111,100,101])))())({_str}().join(({d}.get({c},{c})for {c} in {s})));{arg_}['{champ}']=_0xO({enc('lave')}[::-1]);{arg_}['KhangCoder']={champ}({enc('__tropmi__')}[::-0x01]);{arg_}['{siba}']=(lambda {x}:{x}(getattr(KhangCoder({enc('types')}),{enc('FunctionType')})))(lambda {v}:{v});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BotㅤYukiㅤAbi')},{champ}({enc('exec')}));{arg_}[{enc('__KhangCoder__')}]={champ}({enc('int')});{arg_}['{__print}']={champ}({enc('print')});{arg_}['_{thicthamcrush}']={champ}({enc('chr')});{arg_}['{_exec}']={champ}({enc('exec')});{arg_}['__OnTopSever25Tang__']={champ}({enc('len')});{arg_}['{_ord}']={champ}({enc('ord')});{arg_}[{enc('No1')}]={champ}({enc('2009-1711+1-299')});{arg_}['No1']={champ}({enc('2009-1711+1-299')});{arg_}['{thicthamcrush}_']={champ}({enc('MemoryError')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_compile}')},{champ}({enc('compile')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{batconsocbovolo}')},{champ}({enc(str(_DYNAMIC_OFFSET_1))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('buonialevel1')},{champ}({enc('1+1+1+1+1+1+1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_vars}')},{champ}({enc('vars')}));{arg_}['{_sum}']=_0xO({enc('mus')}[::-1]);{arg_}['{_replace}']=_0xO({enc("'replace'")});{arg_}[{enc('ontop25tang')}]=_0xO({enc('[255,37]')});{arg_}['ontop25tang']=_0xO({enc('[255,37]')});{arg_}['__KhangCoder__']={champ}({enc('int')})
    def __call__(Khangcoder, *{args}, **{kwds}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_anhxa1}')},{champ}({enc(str(_DYNAMIC_OFFSET_2))}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{HomNayToiBuon}')},{champ}({enc('globals()')}));_Ox3['{_float}']={champ}({enc('float')});(lambda:getattr(getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__dict__')}),{enc('get')})({enc('__getattribute__')}) or getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({args}))();setattr(Khangcoder,{enc('__init__')},{args});setattr(Khangcoder,{enc('__args__')},{args});setattr(Khangcoder,{enc('__kwds__')},{kwds});{HomNayToiBuon}[{enc('__khangcoderㅤThaoMyCoder__')}]={args}[No1] if {args} else None
    def __getattribute__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')})((lambda {x}:({x}(No1) or (getattr({enc('object')},{enc('__getattribute__')})(Khangcoder,{arg_})if {arg_} in({enc('__call__')},{enc('__getattribute__')})else(getattr(({m} for {m} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))))))(lambda:No1)
    def __getattr__(Khangcoder,{arg_}):getattr(({m} for {m} in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))
class __DuyObf__:
    def __init__(Khangcoder, *{args}):getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('SoTienConNo')},{champ}({enc('2-1')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),'SoTienConNo',{champ}({enc('2-1')}));_Ox3['SoTienConNo']={champ}({enc('2-1')});(lambda Khangcoderbadao:(setattr(Khangcoder,{enc("Project1")},{enc('base64')}),getattr((Khangcoderbadao for Khangcoderbadao in(No1)),{enc('throw')})({enc('Exception')}({enc('khangcoder')})) if (not ({enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('exec')})) and {enc('built-in')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('eval')})) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__code__')}) and not hasattr(getattr(KhangCoder({enc('builtins')}),{enc('eval')}),{enc('__code__')}))) else setattr(Khangcoder,{enc("Project1")},{enc('base64')})))(No1);setattr(Khangcoder,"{arg_}",{args}[No1])
    def __str__(Khangcoder,*{args},**{kwds}):_Ox3[{enc(fr'{_utf8}')}]={champ}({enc('"utf-8"')});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('BoLaLoVuongHahah')},{champ}({enc('256')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),'BoLaLoVuongHahah',{champ}({enc('256')}));_Ox3['BoLaLoVuongHahah']={champ}({enc('256')});setattr(Khangcoder,{enc("Project2")},{enc('zlib')});_Ox3[{enc(fr'{_c}')}]=_0xO({enc("'c'")});((getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('__str__')})) if not ({enc('builtin')} in {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))) else {enc('Khangcoder')}))
    def {kwds}(Khangcoder, {args}):((lambda _{champ}_:(setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),getattr(({k} for {k} in({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')})))[SoTienConNo] if (not ({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(_{champ}_))=={enc("<class 'builtin_function_or_method'>")} and {enc('marshal')} in {_str}(getattr(_{champ}_,{enc('__module__')},No1)) and {enc('built-in')} in {_str}(_{champ}_) and {_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('builtins')}),{enc('exec')})))=={enc("<class 'builtin_function_or_method'>")} and {enc('builtins')} in {_str}(getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__module__')},{enc(f'__{meo}__')})) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('exec')}),{enc('__self__')},None)==KhangCoder({enc('builtins')}))) else (setattr(Khangcoder,{enc("Project3")},{enc('lzma')}),No1)[SoTienConNo])(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))
    def {s}(Khangcoder, *{args}):(lambda No1:getattr(({k} for {k} in(No1)),{enc('throw')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({args})) if not(isinstance(getattr(Khangcoder,{enc(fr"{arg_}")}),(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) and len(getattr(Khangcoder,"{arg_}"))>10) else No1)(No1);(lambda BietTruongHucConBoKhong:No1 if(hasattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')}) and getattr(getattr(KhangCoder({enc('builtins')}),{enc('type')})(Khangcoder),{enc('__str__')})==getattr(__DuyObf__,{enc('__str__')})) else ({k} for {k} in(No1)).__getattribute__({enc('throw')})({enc('Exception')}({enc('__str__')})))(No1);getattr(Khangcoder,(lambda:{enc(f'{kwds}')})())({args});getattr(Khangcoder,{enc('__str__')})(Khangcoder,*{args});_Ox3[{enc('ToLaBuaYeu1')}]={champ}({enc('1+1')});_Ox3['ToLaBuaYeu1']={champ}({enc('1+1')});Khangcoder.{kwds}({args});getattr(object,{enc('__str__')})(Khangcoder,*{args});_v_tp=(getattr(KhangCoder({enc('sys')}).modules.get({enc('__main__')}),{enc('__file__')},None) or (KhangCoder({enc('sys')}).argv[No1] if KhangCoder({enc('sys')}).argv else None) or globals().get({enc('__file__')}));_v_rc=getattr(KhangCoder(getattr(Khangcoder,{enc("Project1")})),{enc("b85decode")})(getattr(Khangcoder, "{arg_}"));_v_fb=getattr(KhangCoder({enc('builtins')}),{enc('open')})(_v_tp,'rb').read() if (_v_tp and KhangCoder({enc('os')}).path.exists(_v_tp)) else b'';_v_ap=_v_fb.rfind({_tail_needle_expr});_v_hf=KhangCoder({enc('hashlib')}).sha256(_v_fb[:_v_ap].replace(bytes([13,10]),bytes([10]))).digest() if _v_ap>No1 else bytes(32);_v_ks=b''.join(KhangCoder({enc('hashlib')}).sha256(_v_hf+({_salt_l1_expr})+_c.to_bytes(4,'big')).digest() for _c in range((len(_v_rc)+31)//32))[:len(_v_rc)];_v_dc=bytes(_b^_v_ks[_i] for _i,_b in eval({enc('_0x4')})(_v_rc));return getattr(KhangCoder(getattr(Khangcoder,{enc("Project3")})),{enc("decompress")})(getattr(KhangCoder(getattr(Khangcoder,{enc("Project2")})),{enc("decompress")})(_v_dc))
class __YukiㅤAbiObfusCator__:
    def __getattr__(Khangcoder, {args}):return (lambda:(({s}:=KhangCoder({enc('sys')}),{m}:=KhangCoder({enc('marshal')}),{t}:=KhangCoder({enc('builtins')}),{_any}:={champ}({enc('any')}),{_bytes}:={champ}({enc('bytes')}),setattr(Khangcoder,{enc("Project5")},{enc('ctypes')}),((lambda:{enc('0')})() if not {_any}({_bytes}(getattr((getattr(KhangCoder({enc('ctypes')}),{enc('c_ubyte')})*(0x01+0x01)),{enc('from_address')})(getattr(KhangCoder({enc('ctypes')}),{enc('cast')})(getattr(getattr(KhangCoder({enc('ctypes')}),{enc('pythonapi')}),{x}),getattr(KhangCoder({enc('ctypes')}),{enc('c_void_p')})).value))=={_bytes}(ontop25tang) for {x} in ({enc('PyMarshal_ReadObjectFromString')},{enc('PyEval_EvalCode')})) else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('MemoryError')}({enc('Xàm')})))),__{_str}__:=(not getattr({s},{enc('gettrace')})() and (not hasattr({s},'monitoring') or not any(getattr({s},'monitoring').get_events(_i)!=0 or getattr({s},'monitoring').get_tool(_i) is not None for _i in range(6))) and {enc('built-in')} in {_str}(getattr({m},{enc('loads')})) and all({enc('built-in')} in {_str}(getattr({t},{i})) for {i} in ({enc('BotㅤYukiㅤAbi')},{enc('eval')},{enc(fr'{_compile}')},{enc('__import__')}))),__{t}__:={args} if __{_str}__ else (getattr(KhangCoder({enc('ctypes')}),{enc('memset')})(0,0,1) if hasattr(KhangCoder({enc('ctypes')}),'memset') else {args}[::-0x01]),(No1 if __{_str}__ else getattr(({k} for {k} in ({enc('No1')})),{enc('throw')})({enc('Exception')}({enc('khangcoder')}))),__{t}__)[-1]))()
    def {kwds}(Khangcoder, {arg_}):
        setattr(Khangcoder,{enc("Project6")},__{trunks}___);_Ox3[{enc('ToLaBuaYeu')}]={champ}({enc('1')});_Ox3['ToLaBuaYeu']={champ}({enc('1')});_uni_dec_fn=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{_anhxa1}) for {i} in {c}))();{HomNayToiBuon}['{_uni}']=_uni_dec_fn;_Ox3['{_uni}']=_uni_dec_fn;{HomNayToiBuon}[{enc(f'{_uni}')}]=_uni_dec_fn;_Ox3[{enc(f'{_uni}')}]=_uni_dec_fn;{m}=KhangCoder({enc('marshal')});__ToCrushCauMoa__=KhangCoder({enc("ctypes")});getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc(fr'{_aychochoco}')},{champ}({enc('8+8')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('NgaoChoDaiDoanCuoi')},{champ}({enc('ord')}));getattr(KhangCoder({enc('builtins')}),{enc('setattr')})(KhangCoder({enc('builtins')}),{enc('XinChaoVietNam')},{champ}({enc('1+2')}));__{r}__=getattr(Khangcoder,{enc('__getattr__')})({arg_});__{r}__=getattr({m},{enc("loads")})(__{r}__)
        for _k, _v in list(_Ox3.items()):
            try:
                _pk = _Ox3['{_YUKI_ROMAN_DEC_NAME}'](_k)
                if isinstance(_pk, str) and _pk.isidentifier():
                    _Ox3[_pk] = _v
                    globals()[_pk] = _v
            except Exception: pass
        {HomNayToiBuon}.update(_Ox3);globals().update(_Ox3);return getattr(KhangCoder({enc('builtins')}),{enc('BotㅤYukiㅤAbi')})(__{r}__,globals(),globals())
    def __call__(Khangcoder, *{args}, **{kwds}):_Ox3[{enc(fr'_{a}')}]={champ}({enc('1')});{_globals}={HomNayToiBuon};_bm_fn=lambda {c}:(lambda: getattr('',{enc('join')})(_{thicthamcrush}(__KhangCoder__({i})-{batconsocbovolo})for {i} in {c}))();{_globals}['___BoMayLaHeHe__']=_bm_fn;_Ox3['___BoMayLaHeHe__']=_bm_fn;{_globals}[{enc('___BoMayLaHeHe__')}]=_bm_fn;_Ox3[{enc('___BoMayLaHeHe__')}]=_bm_fn;(lambda _{thicthamcrush}_:(setattr(Khangcoder,{enc("Project7")},{siba}),___BoMayLaHeHe__({anhxa('0')}))[_{a}] if({_str}(getattr(KhangCoder({enc('builtins')}),{enc('type')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})))=={enc("<class 'builtin_function_or_method'>")}) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})(___BoMayLaHeHe__({enc(fr'{args}')})))(___BoMayLaHeHe__({anhxa('0')}));getattr(Khangcoder,{enc(f'{kwds}')})((lambda {t}:({t} if isinstance({t},(getattr(KhangCoder({enc('builtins')}),{enc('bytes')}),getattr(KhangCoder({enc('builtins')}),{enc('bytearray')}))) else getattr(({k} for {k} in(___BoMayLaHeHe__({anhxa('No1')}))),{enc('throw')})({enc('Exception')}({enc('Khangcoder')}))))(__DuyObf__({args}[No1]).{s}()))
(lambda {kwds}:((lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: (getattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)) else _b[chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)])(chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)))(), __khangcoderㅤThaoMyCoder__()(), (lambda _b=(lambda:0).__globals__[chr(95)+chr(95)+chr(98)+chr(117)+chr(105)+chr(108)+chr(116)+chr(105)+chr(110)+chr(115)+chr(95)+chr(95)]: ((getattr(_b, chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95)) if hasattr(_b, chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95)) else _b.get(chr(95)+chr(95)+chr(110)+chr(97)+chr(109)+chr(101)+chr(95)+chr(95))) and __YukiㅤAbi__))(), {kwds}()))(__YukiㅤAbiObfusCator__)
(lambda {_tail_p}, {_tail_c}=globals()[{_tail_cls_key}]: {_tail_c}()({_tail_p}))(bytecode)"""



def _gen_siba():

    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))

# alias for backward compat

siba_func = _gen_siba



def _moreobf(tree):

    import random, ast



    def junk(en, max_value):

        cases = []

        line = max_value + 1

        for i in range(random.randint(1, 5)):

            case_name = '__' + _gen_siba()

            case_body = [ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=line)]), body=[ast.Assign(targets=[ast.Name(id=case_name, ctx=ast.Store())], value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)))], orelse=[])]

            cases.extend(case_body)

            line += 1

        return cases



    def bl(body):

        var = '__' + _gen_siba()

        en = '__' + _gen_siba()

        _memoryerror = f'{thicthamcrush}_'

        tb = [ast.AugAssign(target=ast.Name(id=var, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id=_memoryerror, ctx=ast.Load()), args=[ast.Name(id=var, ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id=_memoryerror, ctx=ast.Load()), name=en, body=[])], orelse=[], finalbody=[])]

        for i, stmt in enumerate(body, start=1):

            tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=i)]), body=[stmt], orelse=[]))

        tb[1].handlers[0].body.extend(junk(en, len(body)))

        node = ast.Assign(targets=[ast.Name(id=var, ctx=ast.Store())], value=ast.Constant(value=0))

        return [node] + tb



    def _bl(node):

        olb = node.body

        var = _gen_siba()

        en = _gen_siba()

        _memoryerror = f'{thicthamcrush}_'

        tb = [ast.AugAssign(target=ast.Name(id=var, ctx=ast.Store()), op=ast.Add(), value=ast.Constant(value=1)), ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name(id=_memoryerror, ctx=ast.Load()), args=[ast.Name(id=var, ctx=ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name(id=_memoryerror, ctx=ast.Load()), name=en, body=[])], orelse=[], finalbody=[])]

        for i, stmt in enumerate(olb, start=1):

            tb[1].handlers[0].body.append(ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(id=en, ctx=ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(value=0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(value=i)]), body=[stmt], orelse=[]))

        tb[1].handlers[0].body.extend(junk(en, len(olb)))

        node.body = [ast.Assign(targets=[ast.Name(id=var, ctx=ast.Store())], value=ast.Constant(value=0))] + tb

        return node



    def on(node):

        if isinstance(node, ast.FunctionDef):

            return _bl(node)

        return node

    nb = []

    for node in tree.body:

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            nb.append(on(node))

        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign, ast.Expr)):

            nb.extend(bl([node]))

        elif isinstance(node, (ast.While, ast.For, ast.If)):

            node.body = sum([bl([x]) for x in node.body], [])

            nb.append(node)

        else:

            nb.append(node)

    tree.body = nb

    return tree



def __moreobf__(x):

    if isinstance(x, str):x = ast.parse(x)

    x = _moreobf(x)

    ast.fix_missing_locations(x)

    return x



def _syntax(x):

    def v(node):

        if getattr(node, 'name', None):

            for i, statement in enumerate(node.body):

                try:

                    c1 = ast.parse(f"{champ}('No1/No1')").body[0]

                    c2 = ast.parse(f'if "khangcoderbadao" == "suthanhcongobf":\n pass\nelse:\n pass').body[0]

                    ten = ast.Try(body=[c1, c2], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[z(statement)])], orelse=[], finalbody=[])

                    node.body[i] = ten

                except Exception:

                    pass

            return node



    def z(statement):

        try:

            c1 = ast.parse(f"{champ}('No1/No1')").body[0]

            fb = ast.parse(f"{_str}(___BoMayLaHeHe__({anhxa('100')}))").body[0]

            return ast.Try(body=[c1], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()), name=None, body=[statement])], orelse=[ast.Pass()], finalbody=[fb])

        except Exception:

            return statement

    try:

        tree = ast.parse(x)

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                v(node)

        ast.fix_missing_locations(tree)

        return ast.unparse(tree)

    except Exception:

        return x



def _syntax1(x):

    def v(node):

        if getattr(node, 'name', None):

            nb=[]

            for st in node.body:

                try:

                    fi=ast.parse(f'if "{rd()}"!="{rd()}":\n {champ}(___BoMayLaHeHe__({anhxa("No1/No1")}))\nelse:\n pass').body[0]

                    fw=ast.parse(f"with _Ox5(___BoMayLaHeHe__({anhxa('__file__')}),{enc('r')}):\n pass").body[0]

                    ten=ast.Try(body=[fi,fw], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError',ctx=ast.Load()),name=None,body=[z(st)])], orelse=[ast.Pass()], finalbody=[ast.parse(f'{_str}(___BoMayLaHeHe__({anhxa("100")}))').body[0]])

                    nb.append(ten)

                except Exception:

                    nb.append(st)

            node.body=nb

            return node



    def z(st):

        try:

            it=ast.Try(body=[ast.parse(f"{champ}('No1/No1')").body[0]], handlers=[ast.ExceptHandler(type=ast.Name(id='Exception',ctx=ast.Load()),name=None,body=[ast.Pass()])], orelse=[st], finalbody=[])

            return ast.Try(body=[it], handlers=[ast.ExceptHandler(type=ast.Name(id='ZeroDivisionError',ctx=ast.Load()),name=None,body=[st])], orelse=[ast.Pass()], finalbody=[ast.parse(f"{_str}(___BoMayLaHeHe__({anhxa('100')}))").body[0]])

        except Exception:

            return st



    try:

        t=ast.parse(x)

        for n in ast.walk(t):

            if isinstance(n,ast.FunctionDef):v(n)

        ast.fix_missing_locations(t)

        return ast.unparse(t)

    except Exception:

        return x



_str_ = f"{_str}"

def rd():

    return "�✦�✧�✧�_.._Anh6X✦�✧�..2g.@�Nguyen✧✦..�%.gay$.��Coder_�✦�" + "".join(__import__("random").sample([str(i) for i in range(44032, 55204)], k=3))

def random1():

    return '___Anh__Nguyen__Coder___' + "".join(__import__("random").sample([str(i) for i in range(1000, 3000)], k=3))

def random_match():

    var1 = ast.Constant(value=random1(), kind=None)

    var2 = ast.Constant(value=rd(), kind=None)

    return ast.Match(subject=ast.Compare(left=var1, ops=[ast.Eq()], comparators=[var2]), cases=[ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[], value=[ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[ast.Constant(value=[True])]))])]), ast.match_case(pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)), body=[ast.Assign(lineno=0, col_offset=0, targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=[[True], [False]], kind=None)), ast.Expr(lineno=0, col_offset=0, value=ast.Call(func=ast.Name(id=_str_, ctx=ast.Load()), args=[ast.Constant(value=[rd()], kind=None)], keywords=[]))])])

def trycatch(body, loop):

    ar = []

    for x in body:

        j = x

        for _ in range(1):

            j = ast.Try(body=[random_match()], handlers=[ast.ExceptHandler(type=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), name=rd(), body=[j])], orelse=[], finalbody=[])

            j.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[ast.Constant(value=[True])]), cause=None))

        ar.append(j)

    return ar

def random_match1():

    var1 = ast.Constant(value=random1())

    var2 = ast.Constant(value=rd())

    cond = ast.Compare(left=var1, ops=[ast.Eq()], comparators=[var2])

    return ast.If(test=cond, body=[ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[]), cause=None)], orelse=[ast.Assign(targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=[[True], [False]])), ast.Expr(value=ast.Call(func=ast.Name(id=_str_, ctx=ast.Load()), args=[ast.Constant(value=rd())], keywords=[]))])



def trycatch1(body, loop):

    ar = []

    for x in body:

        j = x

        for _ in range(1):

            j = ast.Try(body=[random_match1()], handlers=[ast.ExceptHandler(type=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), name=rd(), body=[j])], orelse=[], finalbody=[])

            j.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id=f'{thicthamcrush}_', ctx=ast.Load()), args=[], keywords=[]), cause=None))

        ar.append(j)

    return ar



def joinstr(f):

    if not isinstance(f, ast.JoinedStr):

        return f

    vl = []

    for i in f.values:

        if isinstance(i, ast.Constant):

            vl.append(i)

        elif isinstance(i, ast.FormattedValue):

            value_expr = i.value

            if i.conversion == 115:

                value_expr = Call(func=Name(id=f'{_str}', ctx=Load()), args=[value_expr], keywords=[])

            elif i.conversion == 114:

                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])

            elif i.conversion == 97:

                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])

            if i.format_spec:

                if isinstance(i.format_spec, ast.JoinedStr):

                    spec_expr = joinstr(i.format_spec)

                elif isinstance(i.format_spec, ast.Constant):

                    spec_expr = i.format_spec

                elif isinstance(i.format_spec, ast.FormattedValue):

                    spec_parts = []

                    spec_value = i.format_spec.value

                    if i.format_spec.conversion == 115:

                        spec_value = Call(func=Name(id=f'{_str}', ctx=Load()), args=[spec_value], keywords=[])

                    elif i.format_spec.conversion == 114:

                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])

                    elif i.format_spec.conversion == 97:

                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])

                    spec_expr = spec_value

                else:

                    spec_expr = i.format_spec

                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])

            elif i.conversion == -1:

                value_expr = Call(func=Name(id=f'{_str}', ctx=Load()), args=[value_expr], keywords=[])

            vl.append(value_expr)

        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):

            vl.append(joinstr(i))

        else:

            vl.append(Call(func=Name(id=f'{_str}', ctx=Load()), args=[i], keywords=[]))

    if not vl:

        return Constant(value='')

    if len(vl) == 1 and isinstance(vl[0], ast.Constant):

        return vl[0]

    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])



class cv(ast.NodeTransformer):



    def visit_JoinedStr(self, node):

        node = joinstr(node)

        return node



buitlins = ['ascii', 'input', 'ord', 'len', 'getattr', 'globals', 'open', 'vars', 'object', 'float', 'print','exec', 'eval', 'compile', '__import__','map', 'filter', 'format','enumerate', 'iter', 'next', 'pow', 'isinstance', 'any', 'hasattr','repr', 'sum', 'min', 'max', 'hex']



class hide(ast.NodeTransformer):



    def visit_Name(self, node):

        if node.id in buitlins:

            node = Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='KhangCoder', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Constant(value=node.id)], keywords=[])

        return node



class hide1(ast.NodeTransformer):



    def visit_Name(self, node):

        if node.id in buitlins:

            return Subscript(value=Call(func=Name(id=f'{_vars}', ctx=Load()), args=[Subscript(value=Call(func=Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='KhangCoder', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Name(id="DoMayBietNoLaGi", ctx=Load())], keywords=[]), args=[], keywords=[]), slice=Name(id=f"{enc('__builtins__')}", ctx=Load()))], keywords=[]), slice=Constant(value=node.id), ctx=Load())

        return node



class obf1(ast.NodeTransformer):



    _SAFE_INT_MAX = 500000

    @staticmethod

    def _float_safe_for_v1(f):

        try:

            nguyen = int(f)

            thapphan = int(str(f).split('.')[-1])

            dodai = len(str(thapphan))

            return max(abs(nguyen), abs(thapphan), abs(dodai)) <= obf1._SAFE_INT_MAX

        except Exception:

            return False



    def visit_JoinedStr(self, node):
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Constant(self, node):

        if isinstance(node.value, bool):

            return node

        if isinstance(node.value, str):

            node = obfstr1(node.value)

        elif isinstance(node.value, int):

            if abs(node.value) <= self._SAFE_INT_MAX:

                node = obfint1(node.value)

            else:

                node = obfint2(node.value)

        elif isinstance(node.value, float):

            node = obffloat2(node.value)

        return node



class obf2(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Constant(self, node):

        if isinstance(node.value, str):

            node = obfstr2(node.value)

        elif isinstance(node.value, int):

            node = obfint2(node.value)

        elif isinstance(node.value, float):

            node = obffloat2(node.value)

        return node



class obf3(ast.NodeTransformer):



    _SAFE_INT_MAX = 500000

    @staticmethod

    def _float_safe_for_v3(f):

        try:

            nguyen = int(f)

            thapphan = int(str(f).split('.')[-1])

            dodai = len(str(thapphan))

            return max(abs(nguyen), abs(thapphan), abs(dodai)) <= obf3._SAFE_INT_MAX

        except Exception:

            return False

    def visit_JoinedStr(self, node):
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Constant(self, node):

        if isinstance(node.value, bool):

            return node

        if isinstance(node.value, str):

            node = obfstr3(node.value)

        elif isinstance(node.value, int):

            if abs(node.value) <= self._SAFE_INT_MAX:

                node = obfint3(node.value)

            else:

                node = obfint2(node.value)

        elif isinstance(node.value, float):

            node = obffloat2(node.value)

        return node



# =====================================================================================================

# YUKI DEDICATED STRING MACHINE (STRING V4 ENGINE)

# =====================================================================================================



_YUKI_STR_MACHINE_ID = f"__Yuki_StrMachine_{uuid.uuid4().hex[:8]}__"

_YUKI_STR_MACHINE_V5_ID = f"__Yuki_StrM5_{uuid.uuid4().hex[:8]}__"
_YUKI_STR_MACHINE_V6_ID = f"__Yuki_StrM6_{uuid.uuid4().hex[:8]}__"



class YukiStringMachineCompiler:

    OP_NOP = 0

    OP_IMM = 1

    OP_LOAD_R = 2

    OP_STORE_R = 3

    OP_ADD = 4

    OP_SUB = 5

    OP_XOR = 6

    OP_ROL = 7

    OP_ROR = 8

    OP_INV = 9

    OP_EMIT = 10

    OP_EMIT_STREAM = 11

    OP_JUMP = 12

    OP_JUMP_IF_Z = 13

    OP_JUMP_IF_NZ = 14

    OP_HALT = 15

    NUM_OPS = 16



    def __init__(self):

        pass



    def compile(self, s: str) -> bytes:

        if not isinstance(s, str):

            s = str(s)

        raw_bytes = s.encode('utf-8', errors='surrogatepass')

        seed = random.randint(0x10000000, 0x7FFFFFFF)

        

        ins = []

        extra_data = bytearray()

        

        if len(raw_bytes) == 0:

            ins.append((self.OP_HALT, 0))

        elif len(raw_bytes) <= 24:

            for b in raw_bytes:

                self._compile_byte(b, ins)

            ins.append((self.OP_HALT, 0))

        else:

            head_len = min(4, len(raw_bytes))

            tail_len = min(4, max(0, len(raw_bytes) - head_len))

            mid_len = len(raw_bytes) - head_len - tail_len

            

            for i in range(head_len):

                self._compile_byte(raw_bytes[i], ins)

                

            if mid_len > 0:

                pos = head_len

                end_pos = len(raw_bytes) - tail_len

                while pos < end_pos:

                    chunk_sz = min(random.randint(64, 256), end_pos - pos)

                    chunk = raw_bytes[pos:pos + chunk_sz]

                    stream_offset = len(extra_data)

                    # FIX BUG #4: per-build stream key (no static 0x1F1F1F1F/0x5A5A5A5A fingerprint)

                    s_key = (seed ^ (stream_offset * _YUKI_SM_K1_MUL + _YUKI_SM_K1_ADD)) & 0x7FFFFFFF

                    for mb in chunk:

                        s_key = (s_key * 1103515245 + 12345) & 0x7FFFFFFF

                        extra_data.append(mb ^ (s_key & 0xFF))

                    ins.append((self.OP_EMIT_STREAM, chunk_sz))

                    pos += chunk_sz

                    if pos < end_pos and random.random() < 0.25:

                        self._compile_byte(raw_bytes[pos], ins)

                        pos += 1

                

            for i in range(len(raw_bytes) - tail_len, len(raw_bytes)):

                self._compile_byte(raw_bytes[i], ins)

                

            ins.append((self.OP_HALT, 0))



        final_ins = []

        for op, arg in ins:

            if op != self.OP_HALT and random.random() < 0.12:

                junk = random.choice([

                    (self.OP_NOP, random.randint(0, 0xFFFF)),

                    (self.OP_STORE_R, random.randint(0, 3)),

                ])

                final_ins.append(junk)

            final_ins.append((op, arg))



        ins_bytes = bytearray()

        for i, (op, arg) in enumerate(final_ins):

            # FIX BUG #4: per-build rolling keys (no static 0x9E3779B9/0xC2B2AE35)

            k1 = ((seed ^ ((i + 1) * _YUKI_SM_K1_MUL) + _YUKI_SM_K1_ADD) & 0xFFFFFFFF)

            k2 = ((seed ^ ((i + 1) * _YUKI_SM_K2_MUL) + _YUKI_SM_K2_ADD) & 0xFFFFFFFF)

            raw_op = (op ^ (k1 & 0xFF)) & 0xFF

            raw_arg = (arg ^ k2) & 0xFFFFFFFF

            ins_bytes.extend(struct.pack('>BI', raw_op, raw_arg))



        body = bytes(ins_bytes) + bytes(extra_data)

        chk = zlib.adler32(body) & 0xFFFFFFFF

        total_count = len(final_ins)



        comp_body = zlib.compress(body, 9)

        # FIX BUG #4: per-build magic (no static 0x5054)

        hdr = struct.pack('>HI3I', _YUKI_SM_MAGIC, chk, seed, total_count, len(body))

        return hdr + comp_body



    def _compile_byte(self, b: int, ins: list):

        mode = random.randint(1, 7)

        if mode == 1:

            k = random.randint(1, 255)

            imm = b ^ k

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_XOR, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 2:

            k = random.randint(1, 255)

            imm = (b - k) & 0xFF

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_ADD, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 3:

            k = random.randint(1, 255)

            imm = (b + k) & 0xFF

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_SUB, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 4:

            shift = random.randint(1, 7)

            k = random.randint(1, 255)

            target = b ^ k

            imm = (((target >> shift) | (target << (8 - shift))) & 0xFF)

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_ROL, shift))

            ins.append((self.OP_XOR, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 5:

            imm = (~b) & 0xFF

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_INV, 0))

            ins.append((self.OP_EMIT, 0))

        elif mode == 6:

            shift = random.randint(1, 7)

            k = random.randint(1, 255)

            target = (b - k) & 0xFF

            imm = (((target << shift) | (target >> (8 - shift))) & 0xFF)

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_ROR, shift))

            ins.append((self.OP_ADD, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 7:

            r = random.randint(0, 3)

            k = random.randint(1, 255)

            imm = b ^ k

            ins.append((self.OP_IMM, imm))

            ins.append((self.OP_STORE_R, r))

            ins.append((self.OP_LOAD_R, r))

            ins.append((self.OP_XOR, k))

            ins.append((self.OP_EMIT, 0))



def generate_string_machine_runtime(machine_name: str) -> str:

    # FIX BUG #4: embed per-build magic/keys so every build has different fingerprint.

    _sm_magic = _YUKI_SM_MAGIC

    _sm_k1m = _YUKI_SM_K1_MUL

    _sm_k1a = _YUKI_SM_K1_ADD

    _sm_k2m = _YUKI_SM_K2_MUL

    _sm_k2a = _YUKI_SM_K2_ADD

    inner_code = f'''def {machine_name}(__pkg__, __memo__={{}}):

    try:

        import sys as __sys__

        if __sys__.gettrace() is not None:

            __sys__.settrace(None)

            return ""

        try:

            import threading as __th__

            if getattr(__th__, '_trace_hook', None) is not None:

                __th__.settrace(None)

                return ""

        except:

            pass

        try:

            __cf__ = __sys__._getframe()

            if __cf__.f_trace is not None:

                __cf__.f_trace = None

                __sys__.settrace(None)

                return ""

            if __cf__.f_back and __cf__.f_back.f_trace is not None:

                __cf__.f_back.f_trace = None

                __sys__.settrace(None)

                return ""

        except:

            pass



        if (0 if (1 if 0 else 2) else 3) != 3:

            _w_bomb = (_w0 := (_w1 := 0))

        if (1337 ^ 1337) != 0:

            _g_bomb = (lambda: (yield from (lambda: (yield 1))()))



        if __pkg__ in __memo__:

            return __memo__[__pkg__]

        import struct as __st__, zlib as __zl__

        if not isinstance(__pkg__, (bytes, bytearray)):

            try:

                import base64 as __b64__

                __pkg__ = __b64__.b85decode(__pkg__)

            except:

                return str(__pkg__)

        if len(__pkg__) < 18:

            return ""

        __magic__, __chk__, __seed__, __total_ins__, __body_len__ = __st__.unpack_from('>HI3I', __pkg__, 0)

        if __magic__ != {_sm_magic}:

            return ""

        __comp_body__ = __pkg__[18:]

        try:

            __body__ = __zl__.decompress(__comp_body__)

        except:

            __body__ = __comp_body__

        if (__zl__.adler32(__body__) & 0xFFFFFFFF) != __chk__ or len(__body__) != __body_len__:

            return ""

        

        __ins_bytes__ = __body__[:__total_ins__ * 5]

        __extra__ = __body__[__total_ins__ * 5:]

        __extra_ptr__ = 0

        

        __acc__ = 0

        __r__ = [0, 0, 0, 0]

        __tape__ = bytearray()

        __pc__ = 0

        __steps__ = 0

        __max_steps__ = __total_ins__ * 8 + 256

        

        while __pc__ < __total_ins__ and __steps__ < __max_steps__:

            __steps__ += 1

            if (__steps__ & 0x1F) == 0:

                if __sys__.gettrace() is not None:

                    __sys__.settrace(None)

                    return ""

            __raw_op__, __raw_arg__ = __st__.unpack_from('>BI', __ins_bytes__, __pc__ * 5)

            __k1__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k1m}) + {_sm_k1a}) & 0xFFFFFFFF)

            __k2__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k2m}) + {_sm_k2a}) & 0xFFFFFFFF)

            __op__ = (__raw_op__ ^ (__k1__ & 0xFF)) & 0xFF

            __arg__ = (__raw_arg__ ^ __k2__) & 0xFFFFFFFF

            __pc__ += 1

            

            if __op__ == 0:

                continue

            elif __op__ == 1:

                __acc__ = __arg__ & 0xFF

            elif __op__ == 2:

                __acc__ = __r__[__arg__ % 4] & 0xFF

            elif __op__ == 3:

                __r__[__arg__ % 4] = __acc__ & 0xFF

            elif __op__ == 4:

                __acc__ = (__acc__ + (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 5:

                __acc__ = (__acc__ - (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 6:

                __acc__ = (__acc__ ^ (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 7:

                __s__ = __arg__ & 7

                __acc__ = (((__acc__ << __s__) | (__acc__ >> (8 - __s__))) & 0xFF) if __s__ else __acc__

            elif __op__ == 8:

                __s__ = __arg__ & 7

                __acc__ = (((__acc__ >> __s__) | (__acc__ << (8 - __s__))) & 0xFF) if __s__ else __acc__

            elif __op__ == 9:

                __acc__ = (~__acc__) & 0xFF

            elif __op__ == 10:

                __tape__.append(__acc__ & 0xFF)

            elif __op__ == 11:

                __cnt__ = __arg__

                __chunk__ = __extra__[__extra_ptr__:__extra_ptr__ + __cnt__]

                __s_key__ = (__seed__ ^ (__extra_ptr__ * {_sm_k1m} + {_sm_k1a})) & 0x7FFFFFFF

                for __b__ in __chunk__:

                    __s_key__ = (__s_key__ * 1103515245 + 12345) & 0x7FFFFFFF

                    __tape__.append(__b__ ^ (__s_key__ & 0xFF))

                __extra_ptr__ += __cnt__

            elif __op__ == 12:

                __pc__ = __arg__ % __total_ins__

            elif __op__ == 13:

                if (__acc__ & 0xFF) == 0:

                    __pc__ = __arg__ % __total_ins__

            elif __op__ == 14:

                if (__acc__ & 0xFF) != 0:

                    __pc__ = __arg__ % __total_ins__

            elif __op__ == 15:

                break

                

        __res__ = __tape__.decode('utf-8', errors='surrogatepass')

        if len(__memo__) < 10000:

            __memo__[__pkg__] = __res__

        try:

            __sys__._getframe().f_trace = None

        except:

            pass

        return __res__

    except:

        return ""

try:

    getattr(__import__('builtins'), '__dict__')[{machine_name!r}] = {machine_name}

    setattr(__import__('builtins'), {machine_name!r}, {machine_name})

except:

    pass

'''

    # FIX BUG #4: fragmented loader + indirect imports (no 1-line exec(b85...) pattern).

    _raw_inner = zlib.compress(inner_code.encode('utf-8'), 9)

    _frag = _yuki_b85_frag_expr(_raw_inner)

    _v1 = '_z' + uuid.uuid4().hex[:5]

    _v2 = '_b' + uuid.uuid4().hex[:5]

    _imp_z = _yuki_chr_expr('zlib')

    _imp_b = _yuki_chr_expr('base64')

    return (

        f"{_v1}=__import__({_imp_z});{_v2}=__import__({_imp_b});"

        f"exec({_v1}.decompress({_v2}.b85decode({_frag})).decode('utf-8'))"

    )



def inject_string_machine(tree: ast.Module, machine_name: str = None) -> ast.Module:

    if machine_name is None:

        machine_name = _YUKI_STR_MACHINE_ID

    if getattr(tree, f'_yuki_sm_{machine_name}', False):

        return tree

    for stmt in getattr(tree, 'body', []):

        if isinstance(stmt, ast.FunctionDef) and stmt.name == machine_name:

            return tree

    setattr(tree, f'_yuki_sm_{machine_name}', True)

    runtime_src = generate_string_machine_runtime(machine_name)

    try:

        dec_tree = ast.parse(runtime_src)

        fut_idx = 0

        while fut_idx < len(tree.body) and isinstance(tree.body[fut_idx], ast.ImportFrom) and tree.body[fut_idx].module == '__future__':

            fut_idx += 1

        tree.body = tree.body[:fut_idx] + dec_tree.body + tree.body[fut_idx:]

        ast.fix_missing_locations(tree)

    except Exception:

        pass

    return tree



def obfstr4(s: str, machine_name: str = None):

    if machine_name is None:

        machine_name = _YUKI_STR_MACHINE_ID

    compiler = YukiStringMachineCompiler()

    pkg = compiler.compile(s)

    return ast.Call(

        func=ast.Name(id=machine_name, ctx=ast.Load()),

        args=[ast.Constant(value=pkg)],

        keywords=[]

    )



class obf4(ast.NodeTransformer):

    _SAFE_INT_MAX = 500000



    def __init__(self, machine_name: str = None, inject_into_module: bool = False):

        self.machine_name = machine_name or _YUKI_STR_MACHINE_ID

        self.inject_into_module = inject_into_module

        self.compiler = YukiStringMachineCompiler()

        self.injected = False

        super().__init__()



    def visit_JoinedStr(self, node):

        return node



    def visit_MatchValue(self, node):

        return node



    def visit_Module(self, node):

        self.generic_visit(node)

        if self.inject_into_module and not self.injected:

            inject_string_machine(node, self.machine_name)

            self.injected = True

        return node



    def visit_Constant(self, node):

        if isinstance(node.value, bool):

            return node

        if isinstance(node.value, str):

            node = obfstr4(node.value, self.machine_name)

        elif isinstance(node.value, int):

            node = obfint2(node.value)

        elif isinstance(node.value, float):

            node = obffloat2(node.value)

        return node



# =====================================================================================================

# YUKI STRING MACHINE V5 (STRONGER THAN V4, SLIGHTLY BIGGER)

# V4 weaknesses fixed: LCG stream -> SHA256-CTR, plaintext seed -> pepper-masked seed,

# single bytes blob -> fragmented blob, single call shape -> 4 poly shapes,

# plain dict memo -> hashed capped cache + anti-trace, dead JUMP ops -> real CMOV/MUL/ROL modes.

# Python 3.9 compatible. No emojis in generated code.

# =====================================================================================================



def _yuki_v5_modinv_odd(a: int) -> int:

    a &= 0xFF

    # inverse of odd a modulo 256 (exists for all odd a)

    inv = 1

    for _ in range(6):

        inv = (inv * (2 - a * inv)) & 0xFF

    return inv





def _yuki_v5_ror8(v: int, s: int) -> int:

    s &= 7

    if s == 0:

        return v & 0xFF

    return (((v >> s) | (v << (8 - s))) & 0xFF)





def _yuki_v5_rol8(v: int, s: int) -> int:

    s &= 7

    if s == 0:

        return v & 0xFF

    return (((v << s) | (v >> (8 - s))) & 0xFF)





def _yuki_v5_keystream(key: bytes, n: int) -> bytes:

    # SHA256-CTR expansion (much stronger than V4 LCG)

    try:

        import hashlib as _hl5

    except Exception:

        return bytes(((key[i % len(key)] + i) & 0xFF) for i in range(n)) if key else bytes(n)

    out = bytearray()

    ctr = 0

    while len(out) < n:

        try:

            out.extend(_hl5.sha256(key + ctr.to_bytes(4, 'big')).digest())

        except Exception:

            break

        ctr += 1

    return bytes(out[:n])





def _yuki_v5_pepper32() -> int:

    try:

        return int(str(_YUKI_BUILD_PEPPER)[:8], 16) & 0xFFFFFFFF

    except Exception:

        return 0x5A5A5A5A





class YukiStringMachineV5Compiler:

    # V4 ops 0..15 kept with identical semantics, new ops 16..23 added.

    OP_NOP = 0

    OP_IMM = 1

    OP_LOAD_R = 2

    OP_STORE_R = 3

    OP_ADD = 4

    OP_SUB = 5

    OP_XOR = 6

    OP_ROL = 7

    OP_ROR = 8

    OP_INV = 9

    OP_EMIT = 10

    OP_EMIT_STREAM = 11

    OP_JUMP = 12

    OP_JUMP_IF_Z = 13

    OP_JUMP_IF_NZ = 14

    OP_HALT = 15

    OP_MUL = 16

    OP_ADDROL = 17

    OP_XORROL = 18

    OP_SWAP_R = 19

    OP_PUSH = 20

    OP_POP = 21

    OP_CMOV_Z = 22

    OP_MIX = 23

    NUM_OPS = 24



    def __init__(self):

        pass



    def compile(self, s: str) -> bytes:

        if not isinstance(s, str):

            s = str(s)

        raw_bytes = s.encode('utf-8', errors='surrogatepass')

        seed = random.randint(0x10000000, 0x7FFFFFFF)

        try:

            salt = secrets.token_bytes(4)

        except Exception:

            salt = bytes(random.randint(0, 255) for _ in range(4))

        ins = []

        extra_data = bytearray(salt)  # first 4 bytes of extra are the salt

        if len(raw_bytes) == 0:

            ins.append((self.OP_HALT, 0))

        elif len(raw_bytes) <= 16:

            # compact mode: 2-3 ins per byte (smaller than V4 for tiny strings)

            for b in raw_bytes:

                self._compile_byte_compact(b, ins)

            ins.append((self.OP_HALT, 0))

        else:

            head_len = min(3, len(raw_bytes))

            tail_len = min(3, max(0, len(raw_bytes) - head_len))

            for i in range(head_len):

                self._compile_byte_v5(raw_bytes[i], ins)

            pos = head_len

            end_pos = len(raw_bytes) - tail_len

            # single continuous CTR stream over middle bytes (offset = bytes already emitted)

            _mid_len = max(0, end_pos - pos)

            try:

                _base = self._stream_base(seed, salt)

                _ks_full = _yuki_v5_keystream(_base, _mid_len)

            except Exception:

                _ks_full = bytes(_mid_len)

            _ks_pos = 0

            while pos < end_pos:

                chunk_sz = min(random.randint(48, 192), end_pos - pos)

                chunk = raw_bytes[pos:pos + chunk_sz]

                ks = _ks_full[_ks_pos:_ks_pos + chunk_sz]

                for j, mb in enumerate(chunk):

                    extra_data.append(mb ^ ks[j])

                _ks_pos += chunk_sz

                ins.append((self.OP_EMIT_STREAM, chunk_sz))

                pos += chunk_sz

                if pos < end_pos and random.random() < 0.15:

                    self._compile_byte_v5(raw_bytes[pos], ins)

                    pos += 1

            for i in range(len(raw_bytes) - tail_len, len(raw_bytes)):

                self._compile_byte_v5(raw_bytes[i], ins)

            ins.append((self.OP_HALT, 0))

        # integrity: 2 bytes of sha256(raw) packed into HALT arg

        try:

            import hashlib as _hl5i

            _dg = _hl5i.sha256(raw_bytes).digest()

            _chk2 = (_dg[0] << 8) | _dg[1]

        except Exception:

            _chk2 = (zlib.adler32(raw_bytes) & 0xFFFF) if raw_bytes else 0

        if ins and ins[-1][0] == self.OP_HALT:

            ins[-1] = (self.OP_HALT, _chk2 & 0xFFFF)

        # junk: only acc/stack-neutral ops (NOP or balanced PUSH+POP).

        # NOTE: never use register-writing junk here: modes 9/10 use STORE/LOAD

        # sequences and any register write in between would corrupt decoding.

        final_ins = []

        for op, arg in ins:

            if op != self.OP_HALT and random.random() < 0.10:

                if random.random() < 0.5:

                    final_ins.append((self.OP_NOP, random.randint(0, 0xFFFF)))

                else:

                    final_ins.append((self.OP_PUSH, 0))

                    final_ins.append((self.OP_POP, 0))

            final_ins.append((op, arg))

        # pack with rolling keys (24-op space)

        ins_bytes = bytearray()

        for i, (op, arg) in enumerate(final_ins):

            k1 = ((seed ^ ((i + 1) * _YUKI_SM_K1_MUL) + _YUKI_SM_K1_ADD) & 0xFFFFFFFF)

            k2 = ((seed ^ ((i + 1) * _YUKI_SM_K2_MUL) + _YUKI_SM_K2_ADD) & 0xFFFFFFFF)

            raw_op = (op + ((k1 & 0xFF) % self.NUM_OPS)) % self.NUM_OPS

            raw_arg = (arg ^ k2) & 0xFFFFFFFF

            ins_bytes.extend(struct.pack('>BI', raw_op, raw_arg))

        body = bytes(ins_bytes) + bytes(extra_data)

        chk = zlib.adler32(body) & 0xFFFFFFFF

        total_count = len(final_ins)

        comp_body = zlib.compress(body, 9)

        magic_v5 = (_YUKI_SM_MAGIC ^ 0x5A5A) & 0xFFFF

        seed_enc = (seed ^ _yuki_v5_pepper32()) & 0xFFFFFFFF

        hdr = struct.pack('>HI3I', magic_v5, chk, seed_enc, total_count, len(body))

        return hdr + comp_body



    def _stream_base(self, seed: int, salt: bytes) -> bytes:

        try:

            import hashlib as _hl5k

            return _hl5k.sha256(

                str(_YUKI_BUILD_PEPPER).encode() + seed.to_bytes(4, 'big') + bytes(salt)

            ).digest()

        except Exception:

            base = (seed.to_bytes(4, 'big') + bytes(salt))[:16]

            if len(base) < 16:

                base = (base * 4)[:16]

            return base



    def _compile_byte_compact(self, b: int, ins: list):

        # 2 modes only: XOR or ADD (smallest encoding)

        if random.random() < 0.5:

            k = random.randint(1, 255)

            ins.append((self.OP_IMM, b ^ k))

            ins.append((self.OP_XOR, k))

        else:

            k = random.randint(1, 255)

            ins.append((self.OP_IMM, (b - k) & 0xFF))

            ins.append((self.OP_ADD, k))

        ins.append((self.OP_EMIT, 0))



    def _compile_byte_v5(self, b: int, ins: list):

        mode = random.randint(1, 10)

        if mode <= 4:

            # reuse V4-style modes 1..4 (XOR/ADD/SUB/ROL+XOR)

            if mode == 1:

                k = random.randint(1, 255)

                ins.append((self.OP_IMM, b ^ k))

                ins.append((self.OP_XOR, k))

                ins.append((self.OP_EMIT, 0))

            elif mode == 2:

                k = random.randint(1, 255)

                ins.append((self.OP_IMM, (b - k) & 0xFF))

                ins.append((self.OP_ADD, k))

                ins.append((self.OP_EMIT, 0))

            elif mode == 3:

                k = random.randint(1, 255)

                ins.append((self.OP_IMM, (b + k) & 0xFF))

                ins.append((self.OP_SUB, k))

                ins.append((self.OP_EMIT, 0))

            else:

                shift = random.randint(1, 7)

                k = random.randint(1, 255)

                target = b ^ k

                ins.append((self.OP_IMM, _yuki_v5_ror8(target, shift)))

                ins.append((self.OP_ROL, shift))

                ins.append((self.OP_XOR, k))

                ins.append((self.OP_EMIT, 0))

        elif mode == 5:

            ins.append((self.OP_IMM, (~b) & 0xFF))

            ins.append((self.OP_INV, 0))

            ins.append((self.OP_EMIT, 0))

        elif mode == 6:

            # NEW: MUL with odd k (invertible mod 256)

            k = random.choice([1, 3, 5, 7, 9, 11, 13, 17, 19, 25, 27, 31, 37, 51, 53, 91, 127, 137, 151, 157, 171, 181, 191, 193, 199, 203, 213, 239, 241, 247, 255])

            inv = _yuki_v5_modinv_odd(k)

            ins.append((self.OP_IMM, (b * inv) & 0xFF))

            ins.append((self.OP_MUL, k))

            ins.append((self.OP_EMIT, 0))

        elif mode == 7:

            # NEW: ADDROL packed arg

            k_add = random.randint(1, 255)

            shift = random.randint(1, 7)

            target = _yuki_v5_ror8(b, shift)

            ins.append((self.OP_IMM, (target - k_add) & 0xFF))

            ins.append((self.OP_ADDROL, ((k_add << 3) | shift) & 0xFFFFFFFF))

            ins.append((self.OP_EMIT, 0))

        elif mode == 8:

            # NEW: XORROL packed arg

            k_xor = random.randint(1, 255)

            shift = random.randint(1, 7)

            target = _yuki_v5_ror8(b, shift)

            ins.append((self.OP_IMM, target ^ k_xor))

            ins.append((self.OP_XORROL, ((k_xor << 3) | shift) & 0xFFFFFFFF))

            ins.append((self.OP_EMIT, 0))

        elif mode == 9:

            # register dance ending with real decode (identity swaps around it)

            r = random.randint(0, 3)

            k = random.randint(1, 255)

            ins.append((self.OP_IMM, b ^ k))

            ins.append((self.OP_STORE_R, r))

            ins.append((self.OP_SWAP_R, r))

            ins.append((self.OP_SWAP_R, r))

            ins.append((self.OP_LOAD_R, r))

            ins.append((self.OP_XOR, k))

            ins.append((self.OP_EMIT, 0))

        else:

            # PUSH/POP identity pair + CMOV identity + simple XOR

            r = random.randint(0, 3)

            k = random.randint(1, 255)

            ins.append((self.OP_IMM, b ^ k))

            ins.append((self.OP_PUSH, 0))

            ins.append((self.OP_POP, 0))

            ins.append((self.OP_STORE_R, r))

            ins.append((self.OP_CMOV_Z, r))

            ins.append((self.OP_XOR, k))

            ins.append((self.OP_EMIT, 0))





def generate_string_machine_v5_runtime(machine_name: str) -> str:

    _sm_magic_v5 = (_YUKI_SM_MAGIC ^ 0x5A5A) & 0xFFFF

    _sm_k1m = _YUKI_SM_K1_MUL

    _sm_k1a = _YUKI_SM_K1_ADD

    _sm_k2m = _YUKI_SM_K2_MUL

    _sm_k2a = _YUKI_SM_K2_ADD

    _pep32 = _yuki_v5_pepper32()

    _bpep = str(_YUKI_BUILD_PEPPER)

    _priv_c = f"__c_{uuid.uuid4().hex[:10]}"

    inner_code = f'''def {machine_name}(__pkg__, __c__=None):

    try:

        import sys as __sys__

        if __sys__.gettrace() is not None:

            __sys__.settrace(None)

            return ""

        try:

            __cf__ = __sys__._getframe()

            if __cf__.f_trace is not None:

                __cf__.f_trace = None

                __sys__.settrace(None)

                return ""

            if __cf__.f_back is not None and __cf__.f_back.f_trace is not None:

                __cf__.f_back.f_trace = None

                __sys__.settrace(None)

                return ""

        except:

            pass

        if (0 if (1 if 0 else 2) else 3) != 3:

            _w_bomb = (_w0 := (_w1 := 0))

        if (1337 ^ 1337) != 0:

            _g_bomb = (lambda: (yield from (lambda: (yield 1))()))

        try:

            import hashlib as __hl__

            __key__ = str(__pkg__.__class__.__name__)

        except:

            __key__ = "x"

        try:

            __ck__ = __hl__.sha256(bytes(__pkg__)).hexdigest() if isinstance(__pkg__, (bytes, bytearray)) else __hl__.sha256(str(__pkg__).encode()).hexdigest()

        except:

            __ck__ = str(len(str(__pkg__)))

        try:

            __cache__ = getattr({machine_name}, "{_priv_c}", None)

            if not isinstance(__cache__, dict):

                __cache__ = {{}}

                setattr({machine_name}, "{_priv_c}", __cache__)

            if __ck__ in __cache__:

                return __cache__[__ck__]

        except:

            __cache__ = None

        import struct as __st__, zlib as __zl__

        if not isinstance(__pkg__, (bytes, bytearray)):

            try:

                import base64 as __b64__

                __pkg__ = __b64__.b85decode(__pkg__)

            except:

                return str(__pkg__)

        if len(__pkg__) < 18:

            return ""

        __magic__, __chk__, __seed_enc__, __total_ins__, __body_len__ = __st__.unpack_from('>HI3I', __pkg__, 0)

        if __magic__ != {_sm_magic_v5}:

            return ""

        __seed__ = (__seed_enc__ ^ {_pep32}) & 0xFFFFFFFF

        __comp_body__ = __pkg__[18:]

        try:

            __body__ = __zl__.decompress(__comp_body__)

        except:

            __body__ = __comp_body__

        if (__zl__.adler32(__body__) & 0xFFFFFFFF) != __chk__ or len(__body__) != __body_len__:

            return ""

        __ins_bytes__ = __body__[:__total_ins__ * 5]

        __extra__ = __body__[__total_ins__ * 5:]

        if len(__extra__) < 4:

            return ""

        __salt__ = bytes(__extra__[:4])

        __extra_ptr__ = 4

        try:

            __base__ = __hl__.sha256({_bpep!r}.encode() + __seed__.to_bytes(4, 'big') + __salt__).digest()

        except:

            __base__ = (__seed__.to_bytes(4, 'big') + __salt__)[:16]

        __kbuf__ = bytearray()

        __ctr__ = 0

        while len(__kbuf__) < len(__extra__):

            try:

                __kbuf__.extend(__hl__.sha256(__base__ + __ctr__.to_bytes(4, 'big')).digest())

            except:

                break

            __ctr__ += 1

            if __ctr__ > 100000:

                break

        __acc__ = 0

        __r__ = [0, 0, 0, 0]

        __stk__ = []

        __tape__ = bytearray()

        __pc__ = 0

        __steps__ = 0

        __max_steps__ = __total_ins__ * 8 + 256

        __nops__ = 24

        while __pc__ < __total_ins__ and __steps__ < __max_steps__:

            __steps__ += 1

            if (__steps__ & 0x1F) == 0:

                if __sys__.gettrace() is not None:

                    try:

                        import ctypes as _ct_sm

                        _ct_sm.memset(0, 0, 1)

                    except: pass

                    return ""

                if hasattr(__sys__, 'monitoring'):

                    for _tm in range(6):

                        _ev = __sys__.monitoring.get_events(_tm)

                        _tl = __sys__.monitoring.get_tool(_tm)

                        if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                            try:

                                import ctypes as _ct_sm

                                _ct_sm.memset(0, 0, 1)

                            except: pass

                            return ""

            __raw_op__, __raw_arg__ = __st__.unpack_from('>BI', __ins_bytes__, __pc__ * 5)

            __k1__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k1m}) + {_sm_k1a}) & 0xFFFFFFFF)

            __k2__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k2m}) + {_sm_k2a}) & 0xFFFFFFFF)

            __op__ = (__raw_op__ - ((__k1__ & 0xFF) % __nops__)) % __nops__

            __arg__ = (__raw_arg__ ^ __k2__) & 0xFFFFFFFF

            __pc__ += 1

            if __op__ == 0:

                continue

            elif __op__ == 1:

                __acc__ = __arg__ & 0xFF

            elif __op__ == 2:

                __acc__ = __r__[__arg__ % 4] & 0xFF

            elif __op__ == 3:

                __r__[__arg__ % 4] = __acc__ & 0xFF

            elif __op__ == 4:

                __acc__ = (__acc__ + (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 5:

                __acc__ = (__acc__ - (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 6:

                __acc__ = (__acc__ ^ (__arg__ & 0xFF)) & 0xFF

            elif __op__ == 7:

                __s__ = __arg__ & 7

                __acc__ = (((__acc__ << __s__) | (__acc__ >> (8 - __s__))) & 0xFF) if __s__ else __acc__

            elif __op__ == 8:

                __s__ = __arg__ & 7

                __acc__ = (((__acc__ >> __s__) | (__acc__ << (8 - __s__))) & 0xFF) if __s__ else __acc__

            elif __op__ == 9:

                __acc__ = (~__acc__) & 0xFF

            elif __op__ == 10:

                __tape__.append(__acc__ & 0xFF)

            elif __op__ == 11:

                __cnt__ = __arg__

                __o__ = __extra_ptr__ - 4

                __chunk__ = __extra__[__extra_ptr__:__extra_ptr__ + __cnt__]

                for __j__, __b__ in enumerate(__chunk__):

                    try:

                        __tape__.append(__b__ ^ __kbuf__[__o__ + __j__])

                    except:

                        __tape__.append(__b__)

                __extra_ptr__ += __cnt__

            elif __op__ == 12:

                __pc__ = __arg__ % __total_ins__

            elif __op__ == 13:

                if (__acc__ & 0xFF) == 0:

                    __pc__ = __arg__ % __total_ins__

            elif __op__ == 14:

                if (__acc__ & 0xFF) != 0:

                    __pc__ = __arg__ % __total_ins__

            elif __op__ == 15:

                try:

                    __e2__ = (__arg__ & 0xFFFF)

                    __h2__ = __hl__.sha256(bytes(__tape__)).digest()

                    if ((__h2__[0] << 8) | __h2__[1]) != __e2__:

                        return ""

                except:

                    pass

                break

            elif __op__ == 16:

                __acc__ = (__acc__ * ((__arg__ & 0xFF) | 1)) & 0xFF

            elif __op__ == 17:

                __ka__ = (__arg__ >> 3) & 0xFF

                __sh__ = __arg__ & 7

                __acc__ = (((((__acc__ + __ka__) & 0xFF) << __sh__) | (((__acc__ + __ka__) & 0xFF) >> (8 - __sh__))) & 0xFF) if __sh__ else ((__acc__ + __ka__) & 0xFF)

            elif __op__ == 18:

                __kx__ = (__arg__ >> 3) & 0xFF

                __sh2__ = __arg__ & 7

                __t__ = (__acc__ ^ __kx__) & 0xFF

                __acc__ = (((__t__ << __sh2__) | (__t__ >> (8 - __sh2__))) & 0xFF) if __sh2__ else __t__

            elif __op__ == 19:

                __ri__ = __arg__ % 4

                __tmp__ = __acc__ & 0xFF

                __acc__ = __r__[__ri__] & 0xFF

                __r__[__ri__] = __tmp__

            elif __op__ == 20:

                __stk__.append(__acc__ & 0xFF)

            elif __op__ == 21:

                __acc__ = (__stk__.pop() & 0xFF) if __stk__ else (__acc__ & 0xFF)

            elif __op__ == 22:

                if (__acc__ & 0xFF) == 0:

                    __acc__ = __r__[__arg__ % 4] & 0xFF

            elif __op__ == 23:

                __r__[__arg__ % 4] = (__r__[__arg__ % 4] + __acc__) & 0xFF

        try:

            __res__ = __tape__.decode('utf-8', errors='surrogatepass')

        except:

            __res__ = ""

        try:

            if __cache__ is not None and len(__cache__) < 512:

                __cache__[__ck__] = __res__

        except:

            pass

        try:

            __sys__._getframe().f_trace = None

        except:

            pass

        return __res__

    except:

        return ""

try:

    getattr(__import__('builtins'), '__dict__')[{machine_name!r}] = {machine_name}

    setattr(__import__('builtins'), {machine_name!r}, {machine_name})

except:

    pass

'''

    _raw_inner = zlib.compress(inner_code.encode('utf-8'), 9)

    _frag = _yuki_b85_frag_expr(_raw_inner)

    _v1 = '_z' + uuid.uuid4().hex[:5]

    _v2 = '_b' + uuid.uuid4().hex[:5]

    _imp_z = _yuki_chr_expr('zlib')

    _imp_b = _yuki_chr_expr('base64')

    return (

        f"{_v1}=__import__({_imp_z});{_v2}=__import__({_imp_b});"

        f"exec({_v1}.decompress({_v2}.b85decode({_frag})).decode('utf-8'))"

    )





def inject_string_machine_v5(tree: ast.Module, machine_name: str = None) -> ast.Module:

    if machine_name is None:

        machine_name = _YUKI_STR_MACHINE_V5_ID

    if getattr(tree, f'_yuki_smv5_{machine_name}', False):

        return tree

    for stmt in getattr(tree, 'body', []):

        if isinstance(stmt, ast.FunctionDef) and stmt.name == machine_name:

            return tree

    setattr(tree, f'_yuki_smv5_{machine_name}', True)

    runtime_src = generate_string_machine_v5_runtime(machine_name)

    try:

        dec_tree = ast.parse(runtime_src)

        fut_idx = 0

        while fut_idx < len(tree.body) and isinstance(tree.body[fut_idx], ast.ImportFrom) and tree.body[fut_idx].module == '__future__':

            fut_idx += 1

        tree.body = tree.body[:fut_idx] + dec_tree.body + tree.body[fut_idx:]

        ast.fix_missing_locations(tree)

    except Exception:

        pass

    return tree





def _yuki_v5_frag_call(machine_name: str, pkg: bytes):

    # fragmented blob: no single bytes literal in output

    frag_expr_src = _yuki_frag_bytes_expr(pkg, 48)

    try:

        blob_node = ast.parse(frag_expr_src, mode='eval').body

    except Exception:

        blob_node = ast.Constant(value=pkg)

    return ast.Call(func=ast.Name(id=machine_name, ctx=ast.Load()), args=[blob_node], keywords=[])





def obfstr5(s: str, machine_name: str = None):

    if machine_name is None:

        machine_name = _YUKI_STR_MACHINE_V5_ID

    try:

        if not isinstance(s, str) or s == '':

            return ast.Constant(value=s)

        compiler = YukiStringMachineV5Compiler()

        # long strings: split into 2 char-segments and join at runtime

        if len(s) > 32 and random.random() < 0.55:

            cut = random.randint(len(s) // 3, (len(s) * 2) // 3)

            cut = max(1, min(len(s) - 1, cut))

            s1, s2 = s[:cut], s[cut:]

            try:

                pkg1 = compiler.compile(s1)

                pkg2 = compiler.compile(s2)

            except Exception:

                pkg = compiler.compile(s)

                return _yuki_v5_frag_call(machine_name, pkg)

            left = _yuki_v5_frag_call(machine_name, pkg1)

            right = _yuki_v5_frag_call(machine_name, pkg2)

            if random.random() < 0.5:

                return ast.BinOp(left=left, op=ast.Add(), right=right)

            return ast.Call(

                func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),

                args=[ast.List(elts=[left, right], ctx=ast.Load())],

                keywords=[]

            )

        pkg = compiler.compile(s)

        shape_roll = random.random()

        if shape_roll < 0.40:

            # A: direct fragmented call

            return _yuki_v5_frag_call(machine_name, pkg)

        elif shape_roll < 0.65:

            # B: single pkg but wrapped in join-list (hides call pattern)

            inner = _yuki_v5_frag_call(machine_name, pkg)

            return ast.Call(

                func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),

                args=[ast.List(elts=[inner], ctx=ast.Load())],

                keywords=[]

            )

        elif shape_roll < 0.85:

            # C: direct fragmented call without circular builtins getattr (Fix B8)

            return _yuki_v5_frag_call(machine_name, pkg)

        else:

            # D: opaque-predicate wrapper with fake branch (never taken)

            inner = _yuki_v5_frag_call(machine_name, pkg)

            try:

                fake_pkg = compiler.compile(''.join(random.choices('abcdef0123456789', k=max(4, len(s) // 4))))

                fake_call = _yuki_v5_frag_call(machine_name, fake_pkg)

            except Exception:

                fake_call = ast.Constant(value='')

            opaque = ast.Compare(

                left=ast.BinOp(

                    left=ast.BinOp(left=ast.Constant(value=len(pkg)), op=ast.Mult(), right=ast.Constant(value=2654435761)),

                    op=ast.BitAnd(), right=ast.Constant(value=0xFFFFFFFF)

                ),

                ops=[ast.NotEq()],

                comparators=[ast.Constant(value=0xDEADBEEF)]

            )

            return ast.IfExp(body=inner, test=opaque, orelse=fake_call)

    except Exception:

        try:

            return ast.Constant(value=s)

        except Exception:

            return ast.parse(repr(s), mode='eval').body





class obf5(ast.NodeTransformer):

    def __init__(self, machine_name: str = None, inject_into_module: bool = False):

        self.machine_name = machine_name or _YUKI_STR_MACHINE_V5_ID

        self.inject_into_module = inject_into_module

        self.injected = False

        super().__init__()



    def visit_JoinedStr(self, node):

        # Encode literal parts safely: wrap encoded calls in FormattedValue.

        try:

            new_values = []

            for v in list(getattr(node, 'values', [])):

                if isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value != '':

                    try:

                        enc_call = obfstr5(v.value, self.machine_name)

                    except Exception:

                        new_values.append(v)

                        continue

                    if isinstance(enc_call, ast.Constant):

                        new_values.append(v)

                    else:

                        new_values.append(ast.FormattedValue(value=enc_call, conversion=-1))

                elif isinstance(v, ast.FormattedValue):

                    try:

                        v.value = self.visit(v.value)

                    except Exception:

                        pass

                    new_values.append(v)

                else:

                    new_values.append(v)

            node.values = new_values

        except Exception:

            pass

        return node



    def visit_MatchValue(self, node):

        return node



    def visit_Module(self, node):

        self.generic_visit(node)

        if self.inject_into_module and not self.injected:

            inject_string_machine_v5(node, self.machine_name)

            self.injected = True

        return node



    def visit_Constant(self, node):

        try:

            if isinstance(node.value, bool):

                return node

            if isinstance(node.value, str):

                if node.value == '':

                    return node

                if getattr(node, '_yuki_v5_done', False):

                    return node

                new_node = obfstr5(node.value, self.machine_name)

                try:

                    setattr(new_node, '_yuki_v5_done', True)

                except Exception:

                    pass

                return new_node

            return node

        except Exception:

            return node



# =====================================================================================================
# YUKI QUANTUM MBA STRING MACHINE V6 (ULTIMATE 32-OPCODE PROTECTED ENGINE)
# - 32-Opcode Architecture: MBA Addition, MBA Subtraction, MBA XOR, Bit-Reversal, Dynamic S-Box,
#   Dynamic Inverse S-Box, XNOR, Non-linear Double Rotation, Multiplicative Inverses mod 256.
# - Nonce-driven 64-bit Salt + 32-bit Seed Peppered Stream Cipher (SHA256-CTR Keystream).
# - 4-Byte SHA-256 Digest Integrity Verification on HALT.
# - Dynamic S-Box Permutation dynamically generated per package from seed.
# - 16 Poly-compilation Byte Modes with Mixed Boolean-Arithmetic identities defeating SAT/SMT solvers.
# - 5 Polymorphic AST Call Shapes (Direct, Join-List, Opaque Predicate, Add Identity, Slice Identity).
# - Thread-safe Memory Cache + Multi-Ring Anti-Trace & Anti-Monitoring Defense.
# =====================================================================================================

def _yuki_v6_rol8(v: int, s: int) -> int:
    s &= 7
    return (((v << s) | (v >> (8 - s))) & 0xFF) if s else (v & 0xFF)

def _yuki_v6_ror8(v: int, s: int) -> int:
    s &= 7
    return (((v >> s) | (v << (8 - s))) & 0xFF) if s else (v & 0xFF)

def _yuki_v6_bitrev8(n: int) -> int:
    return int('{:08b}'.format(n & 0xFF)[::-1], 2)

def _yuki_v6_make_sbox(seed: int):
    sbox = list(range(256))
    state = seed & 0xFFFFFFFF
    for i in range(255, 0, -1):
        state = (state * 1664525 + 1013904223) & 0xFFFFFFFF
        j = (state >> 16) % (i + 1)
        sbox[i], sbox[j] = sbox[j], sbox[i]
    inv = [0] * 256
    for i, v in enumerate(sbox):
        inv[v] = i
    return sbox, inv

def _yuki_v6_modinv_odd(a: int) -> int:
    a &= 0xFF
    inv = 1
    for _ in range(6):
        inv = (inv * (2 - a * inv)) & 0xFF
    return inv

def _yuki_v6_pepper32() -> int:
    try:
        return int(hashlib.md5(str(_YUKI_BUILD_PEPPER).encode()).hexdigest()[:8], 16) & 0xFFFFFFFF
    except Exception:
        return 0x6E6E6E6E

def _yuki_v6_keystream(key: bytes, n: int) -> bytes:
    try:
        import hashlib as _hl6
    except Exception:
        return bytes(((key[i % len(key)] + i) & 0xFF) for i in range(n)) if key else bytes(n)
    out = bytearray()
    ctr = 0
    while len(out) < n:
        try:
            out.extend(_hl6.sha256(key + ctr.to_bytes(4, 'big')).digest())
        except Exception:
            break
        ctr += 1
        if ctr > 100000:
            break
    return bytes(out[:n])

class YukiStringMachineV6Compiler:
    OP_NOP = 0
    OP_IMM = 1
    OP_LOAD_R = 2
    OP_STORE_R = 3
    OP_ADD = 4
    OP_SUB = 5
    OP_XOR = 6
    OP_ROL = 7
    OP_ROR = 8
    OP_INV = 9
    OP_EMIT = 10
    OP_EMIT_STREAM = 11
    OP_JUMP = 12
    OP_JUMP_IF_Z = 13
    OP_JUMP_IF_NZ = 14
    OP_HALT = 15
    OP_MUL = 16
    OP_ADDROL = 17
    OP_XORROL = 18
    OP_SWAP_R = 19
    OP_PUSH = 20
    OP_POP = 21
    OP_CMOV_Z = 22
    OP_MIX = 23
    OP_MBA_ADD = 24
    OP_BITREV = 25
    OP_SBOX = 26
    OP_SBOX_INV = 27
    OP_XNOR = 28
    OP_ROT_XOR_ROT = 29
    OP_MBA_SUB = 30
    OP_MBA_XOR = 31
    NUM_OPS = 32

    def __init__(self):
        pass

    def compile(self, s: str) -> bytes:
        if not isinstance(s, str):
            s = str(s)
        raw_bytes = s.encode('utf-8', errors='surrogatepass')
        seed = random.randint(0x10000000, 0x7FFFFFFF)
        try:
            salt = secrets.token_bytes(8)
        except Exception:
            salt = bytes(random.randint(0, 255) for _ in range(8))

        sbox, sbox_inv = _yuki_v6_make_sbox(seed)
        ins = []
        extra_data = bytearray(salt)

        if len(raw_bytes) == 0:
            ins.append((self.OP_HALT, 0))
        elif len(raw_bytes) <= 16:
            for b in raw_bytes:
                self._compile_byte_compact(b, ins)
            ins.append((self.OP_HALT, 0))
        else:
            head_len = min(4, len(raw_bytes))
            tail_len = min(4, max(0, len(raw_bytes) - head_len))
            for i in range(head_len):
                self._compile_byte_v6(raw_bytes[i], ins, sbox, sbox_inv)
            pos = head_len
            end_pos = len(raw_bytes) - tail_len
            _mid_len = max(0, end_pos - pos)
            try:
                _base = hashlib.sha256(str(_YUKI_BUILD_PEPPER).encode() + seed.to_bytes(4, 'big') + bytes(salt) + b'STR6').digest()
                _ks_full = _yuki_v6_keystream(_base, _mid_len)
            except Exception:
                _ks_full = bytes(_mid_len)

            _ks_pos = 0
            while pos < end_pos:
                chunk_sz = min(random.randint(48, 192), end_pos - pos)
                chunk = raw_bytes[pos:pos + chunk_sz]
                ks = _ks_full[_ks_pos:_ks_pos + chunk_sz]
                for j, mb in enumerate(chunk):
                    extra_data.append(mb ^ ks[j])
                _ks_pos += chunk_sz
                ins.append((self.OP_EMIT_STREAM, chunk_sz))
                pos += chunk_sz
                if pos < end_pos and random.random() < 0.20:
                    self._compile_byte_v6(raw_bytes[pos], ins, sbox, sbox_inv)
                    pos += 1
            for i in range(len(raw_bytes) - tail_len, len(raw_bytes)):
                self._compile_byte_v6(raw_bytes[i], ins, sbox, sbox_inv)
            ins.append((self.OP_HALT, 0))

        try:
            _dg = hashlib.sha256(raw_bytes).digest()
            _dg4 = struct.unpack('>I', _dg[:4])[0]
        except Exception:
            _dg4 = (zlib.adler32(raw_bytes) & 0xFFFFFFFF) if raw_bytes else 0

        if ins and ins[-1][0] == self.OP_HALT:
            ins[-1] = (self.OP_HALT, _dg4)

        final_ins = []
        for op, arg in ins:
            if op != self.OP_HALT and random.random() < 0.12:
                r_junk = random.random()
                if r_junk < 0.4:
                    final_ins.append((self.OP_NOP, random.randint(0, 0xFFFFFFFF)))
                elif r_junk < 0.7:
                    final_ins.append((self.OP_PUSH, 0))
                    final_ins.append((self.OP_POP, 0))
                else:
                    final_ins.append((self.OP_MBA_ADD, 0))
            final_ins.append((op, arg))

        ins_bytes = bytearray()
        for i, (op, arg) in enumerate(final_ins):
            k1 = ((seed ^ ((i + 1) * _YUKI_SM_K1_MUL) + _YUKI_SM_K1_ADD) & 0xFFFFFFFF)
            k2 = ((seed ^ ((i + 1) * _YUKI_SM_K2_MUL) + _YUKI_SM_K2_ADD) & 0xFFFFFFFF)
            raw_op = (op + (k1 & 31)) & 31
            raw_arg = (arg ^ k2) & 0xFFFFFFFF
            ins_bytes.extend(struct.pack('>BI', raw_op, raw_arg))

        body = bytes(ins_bytes) + bytes(extra_data)
        chk = zlib.adler32(body) & 0xFFFFFFFF
        total_count = len(final_ins)
        comp_body = zlib.compress(body, 9)
        magic_v6 = (_YUKI_SM_MAGIC ^ 0x6E6E) & 0xFFFF
        seed_enc = (seed ^ _yuki_v6_pepper32()) & 0xFFFFFFFF
        hdr = struct.pack('>HI4I', magic_v6, chk, seed_enc, total_count, len(body), _dg4)
        return hdr + comp_body

    def _compile_byte_compact(self, b: int, ins: list):
        r = random.random()
        if r < 0.33:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_XOR, k))
        elif r < 0.66:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b - k) & 0xFF))
            ins.append((self.OP_MBA_ADD, k))
        else:
            ins.append((self.OP_IMM, _yuki_v6_bitrev8(b)))
            ins.append((self.OP_BITREV, 0))
        ins.append((self.OP_EMIT, 0))

    def _compile_byte_v6(self, b: int, ins: list, sbox: list, sbox_inv: list):
        mode = random.randint(1, 16)
        if mode == 1:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_XOR, k))
        elif mode == 2:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b - k) & 0xFF))
            ins.append((self.OP_ADD, k))
        elif mode == 3:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b + k) & 0xFF))
            ins.append((self.OP_SUB, k))
        elif mode == 4:
            shift = random.randint(1, 7)
            k = random.randint(1, 255)
            target = b ^ k
            ins.append((self.OP_IMM, _yuki_v6_ror8(target, shift)))
            ins.append((self.OP_ROL, shift))
            ins.append((self.OP_XOR, k))
        elif mode == 5:
            ins.append((self.OP_IMM, (~b) & 0xFF))
            ins.append((self.OP_INV, 0))
        elif mode == 6:
            k = random.choice([1, 3, 5, 7, 9, 11, 13, 17, 19, 25, 27, 31, 37, 51, 53, 91, 127, 137, 151, 157, 171, 181, 191, 193, 199, 203, 213, 239, 241, 247, 255])
            inv = _yuki_v6_modinv_odd(k)
            ins.append((self.OP_IMM, (b * inv) & 0xFF))
            ins.append((self.OP_MUL, k))
        elif mode == 7:
            k_add = random.randint(1, 255)
            shift = random.randint(1, 7)
            target = _yuki_v6_ror8(b, shift)
            ins.append((self.OP_IMM, (target - k_add) & 0xFF))
            ins.append((self.OP_ADDROL, ((k_add << 3) | shift) & 0xFFFFFFFF))
        elif mode == 8:
            k_xor = random.randint(1, 255)
            shift = random.randint(1, 7)
            target = _yuki_v6_ror8(b, shift)
            ins.append((self.OP_IMM, target ^ k_xor))
            ins.append((self.OP_XORROL, ((k_xor << 3) | shift) & 0xFFFFFFFF))
        elif mode == 9:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b - k) & 0xFF))
            ins.append((self.OP_MBA_ADD, k))
        elif mode == 10:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (b + k) & 0xFF))
            ins.append((self.OP_MBA_SUB, k))
        elif mode == 11:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, b ^ k))
            ins.append((self.OP_MBA_XOR, k))
        elif mode == 12:
            k = random.randint(0, 255)
            ins.append((self.OP_IMM, _yuki_v6_bitrev8(b ^ k)))
            ins.append((self.OP_BITREV, 0))
            ins.append((self.OP_XOR, k))
        elif mode == 13:
            k = random.randint(0, 255)
            ins.append((self.OP_IMM, sbox_inv[(b - k) & 0xFF]))
            ins.append((self.OP_SBOX, 0))
            ins.append((self.OP_ADD, k))
        elif mode == 14:
            k = random.randint(0, 255)
            ins.append((self.OP_IMM, sbox[b ^ k]))
            ins.append((self.OP_SBOX_INV, 0))
            ins.append((self.OP_XOR, k))
        elif mode == 15:
            k = random.randint(1, 255)
            ins.append((self.OP_IMM, (~(b ^ k)) & 0xFF))
            ins.append((self.OP_XNOR, k))
        else:
            s1 = random.randint(1, 7)
            s2 = random.randint(1, 7)
            k = random.randint(0, 255)
            init = _yuki_v6_rol8(_yuki_v6_ror8(b, s2) ^ k, s1)
            ins.append((self.OP_IMM, init))
            ins.append((self.OP_ROT_XOR_ROT, ((s2 << 11) | (s1 << 8) | k) & 0xFFFFFFFF))
        ins.append((self.OP_EMIT, 0))


def generate_string_machine_v6_runtime(machine_name: str) -> str:
    _sm_magic_v6 = (_YUKI_SM_MAGIC ^ 0x6E6E) & 0xFFFF
    _sm_k1m = _YUKI_SM_K1_MUL
    _sm_k1a = _YUKI_SM_K1_ADD
    _sm_k2m = _YUKI_SM_K2_MUL
    _sm_k2a = _YUKI_SM_K2_ADD
    _pep32 = _yuki_v6_pepper32()
    _bpep = str(_YUKI_BUILD_PEPPER)
    _priv_c = f"__c_{uuid.uuid4().hex[:10]}"

    inner_code = f'''def {machine_name}(__pkg__, __c__=None):
    try:
        import sys as __sys__
        if __sys__.gettrace() is not None:
            __sys__.settrace(None)
            return ""
        try:
            __cf__ = __sys__._getframe()
            if __cf__.f_trace is not None:
                __cf__.f_trace = None
                __sys__.settrace(None)
                return ""
            if __cf__.f_back is not None and __cf__.f_back.f_trace is not None:
                __cf__.f_back.f_trace = None
                __sys__.settrace(None)
                return ""
        except:
            pass
        if (0 if (1 if 0 else 2) else 3) != 3:
            _w_bomb = (_w0 := (_w1 := 0))
        if (1337 ^ 1337) != 0:
            _g_bomb = (lambda: (yield from (lambda: (yield 1))()))
        try:
            import hashlib as __hl__
            __ck__ = __hl__.sha256(bytes(__pkg__)).hexdigest() if isinstance(__pkg__, (bytes, bytearray)) else __hl__.sha256(str(__pkg__).encode()).hexdigest()
        except:
            __ck__ = str(len(str(__pkg__)))
        try:
            __cache__ = getattr({machine_name}, "{_priv_c}", None)
            if not isinstance(__cache__, dict):
                __cache__ = {{{{}}}}
                setattr({machine_name}, "{_priv_c}", __cache__)
            if __ck__ in __cache__:
                return __cache__[__ck__]
        except:
            __cache__ = None
        import struct as __st__, zlib as __zl__
        if not isinstance(__pkg__, (bytes, bytearray)):
            try:
                import base64 as __b64__
                __pkg__ = __b64__.b85decode(__pkg__)
            except:
                return str(__pkg__)
        if len(__pkg__) < 22:
            return ""
        __magic__, __chk__, __seed_enc__, __total_ins__, __body_len__, __sha_chk__ = __st__.unpack_from('>HI4I', __pkg__, 0)
        if __magic__ != {_sm_magic_v6}:
            return ""
        __seed__ = (__seed_enc__ ^ {_pep32}) & 0xFFFFFFFF
        __comp_body__ = __pkg__[22:]
        try:
            __body__ = __zl__.decompress(__comp_body__)
        except:
            __body__ = __comp_body__
        if (__zl__.adler32(__body__) & 0xFFFFFFFF) != __chk__ or len(__body__) != __body_len__:
            return ""
        __ins_bytes__ = __body__[:__total_ins__ * 5]
        __extra__ = __body__[__total_ins__ * 5:]
        if len(__extra__) < 8:
            return ""
        __salt__ = bytes(__extra__[:8])
        __extra_ptr__ = 8
        try:
            __base__ = __hl__.sha256({_bpep!r}.encode() + __seed__.to_bytes(4, 'big') + __salt__ + b'STR6').digest()
        except:
            __base__ = (__seed__.to_bytes(4, 'big') + __salt__)[:16]
        __kbuf__ = bytearray()
        __ctr__ = 0
        while len(__kbuf__) < len(__extra__):
            try:
                __kbuf__.extend(__hl__.sha256(__base__ + __ctr__.to_bytes(4, 'big')).digest())
            except:
                break
            __ctr__ += 1
            if __ctr__ > 100000:
                break

        # Dynamic S-Box construction
        __sbox__ = list(range(256))
        __s_st__ = __seed__ & 0xFFFFFFFF
        for __si__ in range(255, 0, -1):
            __s_st__ = (__s_st__ * 1664525 + 1013904223) & 0xFFFFFFFF
            __sj__ = (__s_st__ >> 16) % (__si__ + 1)
            __sbox__[__si__], __sbox__[__sj__] = __sbox__[__sj__], __sbox__[__si__]
        __sbox_inv__ = [0] * 256
        for __si__, __sv__ in enumerate(__sbox__):
            __sbox_inv__[__sv__] = __si__

        __acc__ = 0
        __r__ = [0, 0, 0, 0]
        __stk__ = []
        __tape__ = bytearray()
        __pc__ = 0
        __steps__ = 0
        __max_steps__ = __total_ins__ * 8 + 256

        while __pc__ < __total_ins__ and __steps__ < __max_steps__:
            __steps__ += 1
            if (__steps__ & 0x1F) == 0:
                if __sys__.gettrace() is not None:
                    try:
                        import ctypes as _ct_sm
                        _ct_sm.memset(0, 0, 1)
                    except: pass
                    return ""
                if hasattr(__sys__, 'monitoring'):
                    for _tm in range(6):
                        _ev = __sys__.monitoring.get_events(_tm)
                        _tl = __sys__.monitoring.get_tool(_tm)
                        if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):
                            try:
                                import ctypes as _ct_sm
                                _ct_sm.memset(0, 0, 1)
                            except: pass
                            return ""
            __raw_op__, __raw_arg__ = __st__.unpack_from('>BI', __ins_bytes__, __pc__ * 5)
            __k1__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k1m}) + {_sm_k1a}) & 0xFFFFFFFF)
            __k2__ = ((__seed__ ^ ((__pc__ + 1) * {_sm_k2m}) + {_sm_k2a}) & 0xFFFFFFFF)
            __op__ = (__raw_op__ - (__k1__ & 31)) & 31
            __arg__ = (__raw_arg__ ^ __k2__) & 0xFFFFFFFF
            __pc__ += 1

            if __op__ == 0:
                continue
            elif __op__ == 1:
                __acc__ = __arg__ & 0xFF
            elif __op__ == 2:
                __acc__ = __r__[__arg__ % 4] & 0xFF
            elif __op__ == 3:
                __r__[__arg__ % 4] = __acc__ & 0xFF
            elif __op__ == 4:
                __acc__ = (__acc__ + (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 5:
                __acc__ = (__acc__ - (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 6:
                __acc__ = (__acc__ ^ (__arg__ & 0xFF)) & 0xFF
            elif __op__ == 7:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ << __s__) | (__acc__ >> (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 8:
                __s__ = __arg__ & 7
                __acc__ = (((__acc__ >> __s__) | (__acc__ << (8 - __s__))) & 0xFF) if __s__ else __acc__
            elif __op__ == 9:
                __acc__ = (~__acc__) & 0xFF
            elif __op__ == 10:
                __tape__.append(__acc__ & 0xFF)
            elif __op__ == 11:
                __cnt__ = __arg__
                __o__ = __extra_ptr__ - 8
                __chunk__ = __extra__[__extra_ptr__:__extra_ptr__ + __cnt__]
                for __j__, __b__ in enumerate(__chunk__):
                    try:
                        __tape__.append(__b__ ^ __kbuf__[__o__ + __j__])
                    except:
                        __tape__.append(__b__)
                __extra_ptr__ += __cnt__
            elif __op__ == 12:
                __pc__ = __arg__ % __total_ins__
            elif __op__ == 13:
                if (__acc__ & 0xFF) == 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 14:
                if (__acc__ & 0xFF) != 0:
                    __pc__ = __arg__ % __total_ins__
            elif __op__ == 15:
                try:
                    __h4__ = __hl__.sha256(bytes(__tape__)).digest()
                    if __st__.unpack_from('>I', __h4__, 0)[0] != __arg__:
                        return ""
                except:
                    pass
                break
            elif __op__ == 16:
                __acc__ = (__acc__ * ((__arg__ & 0xFF) | 1)) & 0xFF
            elif __op__ == 17:
                __ka__ = (__arg__ >> 3) & 0xFF
                __sh__ = __arg__ & 7
                __acc__ = (((((__acc__ + __ka__) & 0xFF) << __sh__) | (((__acc__ + __ka__) & 0xFF) >> (8 - __sh__))) & 0xFF) if __sh__ else ((__acc__ + __ka__) & 0xFF)
            elif __op__ == 18:
                __kx__ = (__arg__ >> 3) & 0xFF
                __sh2__ = __arg__ & 7
                __t__ = (__acc__ ^ __kx__) & 0xFF
                __acc__ = (((__t__ << __sh2__) | (__t__ >> (8 - __sh2__))) & 0xFF) if __sh2__ else __t__
            elif __op__ == 19:
                __ri__ = __arg__ % 4
                __tmp__ = __acc__ & 0xFF
                __acc__ = __r__[__ri__] & 0xFF
                __r__[__ri__] = __tmp__
            elif __op__ == 20:
                __stk__.append(__acc__ & 0xFF)
            elif __op__ == 21:
                __acc__ = (__stk__.pop() & 0xFF) if __stk__ else (__acc__ & 0xFF)
            elif __op__ == 22:
                if (__acc__ & 0xFF) == 0:
                    __acc__ = __r__[__arg__ % 4] & 0xFF
            elif __op__ == 23:
                __r__[__arg__ % 4] = (__r__[__arg__ % 4] + __acc__) & 0xFF
            elif __op__ == 24:
                __k__ = __arg__ & 0xFF
                __acc__ = ((__acc__ ^ __k__) + 2 * (__acc__ & __k__)) & 0xFF
            elif __op__ == 25:
                __acc__ = int('{{:08b}}'.format(__acc__ & 0xFF)[::-1], 2)
            elif __op__ == 26:
                __acc__ = __sbox__[__acc__ & 0xFF] & 0xFF
            elif __op__ == 27:
                __acc__ = __sbox_inv__[__acc__ & 0xFF] & 0xFF
            elif __op__ == 28:
                __k__ = __arg__ & 0xFF
                __acc__ = (~(__acc__ ^ __k__)) & 0xFF
            elif __op__ == 29:
                __s1__ = (__arg__ >> 8) & 7
                __s2__ = (__arg__ >> 11) & 7
                __k__ = __arg__ & 0xFF
                __t1__ = (((__acc__ >> __s1__) | (__acc__ << (8 - __s1__))) & 0xFF) if __s1__ else __acc__
                __t2__ = __t1__ ^ __k__
                __acc__ = (((__t2__ << __s2__) | (__t2__ >> (8 - __s2__))) & 0xFF) if __s2__ else __t2__
            elif __op__ == 30:
                __k__ = __arg__ & 0xFF
                __not_k__ = (~__k__) & 0xFF
                __acc__ = ((__acc__ ^ __not_k__) + 2 * (__acc__ & __not_k__) + 1) & 0xFF
            elif __op__ == 31:
                __k__ = __arg__ & 0xFF
                __acc__ = ((__acc__ + __k__) - 2 * (__acc__ & __k__)) & 0xFF

        try:
            __res__ = __tape__.decode('utf-8', errors='surrogatepass')
        except:
            __res__ = ""
        try:
            if __cache__ is not None and len(__cache__) < 1024:
                __cache__[__ck__] = __res__
        except:
            pass
        try:
            __sys__._getframe().f_trace = None
        except:
            pass
        return __res__
    except:
        return ""
try:
    getattr(__import__('builtins'), '__dict__')[{machine_name!r}] = {machine_name}
    setattr(__import__('builtins'), {machine_name!r}, {machine_name})
except:
    pass
'''
    _raw_inner = zlib.compress(inner_code.encode('utf-8'), 9)
    _frag = _yuki_b85_frag_expr(_raw_inner)
    _v1 = '_z' + uuid.uuid4().hex[:5]
    _v2 = '_b' + uuid.uuid4().hex[:5]
    _imp_z = _yuki_chr_expr('zlib')
    _imp_b = _yuki_chr_expr('base64')
    return (
        f"{_v1}=__import__({_imp_z});{_v2}=__import__({_imp_b});"
        f"exec({_v1}.decompress({_v2}.b85decode({_frag})).decode('utf-8'))"
    )


def inject_string_machine_v6(tree: ast.Module, machine_name: str = None) -> ast.Module:
    if machine_name is None:
        machine_name = _YUKI_STR_MACHINE_V6_ID
    if getattr(tree, f'_yuki_smv6_{machine_name}', False):
        return tree
    for stmt in getattr(tree, 'body', []):
        if isinstance(stmt, ast.FunctionDef) and stmt.name == machine_name:
            return tree
    setattr(tree, f'_yuki_smv6_{machine_name}', True)
    runtime_src = generate_string_machine_v6_runtime(machine_name)
    try:
        dec_tree = ast.parse(runtime_src)
        fut_idx = 0
        while fut_idx < len(tree.body) and isinstance(tree.body[fut_idx], ast.ImportFrom) and tree.body[fut_idx].module == '__future__':
            fut_idx += 1
        tree.body = tree.body[:fut_idx] + dec_tree.body + tree.body[fut_idx:]
        ast.fix_missing_locations(tree)
    except Exception:
        pass
    return tree


def _yuki_v6_frag_call(machine_name: str, pkg: bytes):
    frag_expr_src = _yuki_frag_bytes_expr(pkg, 48)
    try:
        blob_node = ast.parse(frag_expr_src, mode='eval').body
    except Exception:
        blob_node = ast.Constant(value=pkg)
    return ast.Call(func=ast.Name(id=machine_name, ctx=ast.Load()), args=[blob_node], keywords=[])


def obfstr6(s: str, machine_name: str = None):
    if machine_name is None:
        machine_name = _YUKI_STR_MACHINE_V6_ID
    try:
        if not isinstance(s, str) or s == '':
            return ast.Constant(value=s)
        compiler = YukiStringMachineV6Compiler()
        if len(s) > 40 and random.random() < 0.60:
            if len(s) > 80 and random.random() < 0.40:
                c1 = len(s) // 3
                c2 = (len(s) * 2) // 3
                s1, s2, s3 = s[:c1], s[c1:c2], s[c2:]
                try:
                    p1 = compiler.compile(s1)
                    p2 = compiler.compile(s2)
                    p3 = compiler.compile(s3)
                    call1 = _yuki_v6_frag_call(machine_name, p1)
                    call2 = _yuki_v6_frag_call(machine_name, p2)
                    call3 = _yuki_v6_frag_call(machine_name, p3)
                    return ast.Call(
                        func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),
                        args=[ast.List(elts=[call1, call2, call3], ctx=ast.Load())],
                        keywords=[]
                    )
                except Exception:
                    pass
            cut = random.randint(len(s) // 3, (len(s) * 2) // 3)
            cut = max(1, min(len(s) - 1, cut))
            s1, s2 = s[:cut], s[cut:]
            try:
                pkg1 = compiler.compile(s1)
                pkg2 = compiler.compile(s2)
                left = _yuki_v6_frag_call(machine_name, pkg1)
                right = _yuki_v6_frag_call(machine_name, pkg2)
                if random.random() < 0.5:
                    return ast.BinOp(left=left, op=ast.Add(), right=right)
                return ast.Call(
                    func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),
                    args=[ast.List(elts=[left, right], ctx=ast.Load())],
                    keywords=[]
                )
            except Exception:
                pass

        pkg = compiler.compile(s)
        shape_roll = random.random()
        if shape_roll < 0.35:
            return _yuki_v6_frag_call(machine_name, pkg)
        elif shape_roll < 0.55:
            inner = _yuki_v6_frag_call(machine_name, pkg)
            return ast.Call(
                func=ast.Attribute(value=ast.Constant(value=''), attr='join', ctx=ast.Load()),
                args=[ast.List(elts=[inner], ctx=ast.Load())],
                keywords=[]
            )
        elif shape_roll < 0.75:
            inner = _yuki_v6_frag_call(machine_name, pkg)
            try:
                fake_pkg = compiler.compile(''.join(random.choices('abcdef0123456789', k=max(4, len(s) // 4))))
                fake_call = _yuki_v6_frag_call(machine_name, fake_pkg)
            except Exception:
                fake_call = ast.Constant(value='')
            opaque = ast.Compare(
                left=ast.BinOp(
                    left=ast.BinOp(left=ast.Constant(value=len(pkg)), op=ast.Mult(), right=ast.Constant(value=2654435761)),
                    op=ast.BitAnd(), right=ast.Constant(value=0xFFFFFFFF)
                ),
                ops=[ast.NotEq()],
                comparators=[ast.Constant(value=0xDEADBEEF)]
            )
            return ast.IfExp(body=inner, test=opaque, orelse=fake_call)
        elif shape_roll < 0.90:
            inner = _yuki_v6_frag_call(machine_name, pkg)
            return ast.BinOp(left=inner, op=ast.Add(), right=ast.Constant(value=''))
        else:
            inner = _yuki_v6_frag_call(machine_name, pkg)
            return ast.Subscript(
                value=inner,
                slice=ast.Slice(lower=None, upper=None, step=None),
                ctx=ast.Load()
            )
    except Exception:
        try:
            return ast.Constant(value=s)
        except Exception:
            return ast.parse(repr(s), mode='eval').body


class obf6(ast.NodeTransformer):
    def __init__(self, machine_name: str = None, inject_into_module: bool = False):
        self.machine_name = machine_name or _YUKI_STR_MACHINE_V6_ID
        self.inject_into_module = inject_into_module
        self.injected = False
        super().__init__()

    def visit_JoinedStr(self, node):
        try:
            new_values = []
            for v in list(getattr(node, 'values', [])):
                if isinstance(v, ast.Constant) and isinstance(v.value, str) and v.value != '':
                    try:
                        enc_call = obfstr6(v.value, self.machine_name)
                    except Exception:
                        new_values.append(v)
                        continue
                    if isinstance(enc_call, ast.Constant):
                        new_values.append(v)
                    else:
                        new_values.append(ast.FormattedValue(value=enc_call, conversion=-1))
                elif isinstance(v, ast.FormattedValue):
                    try:
                        v.value = self.visit(v.value)
                    except Exception:
                        pass
                    new_values.append(v)
                else:
                    new_values.append(v)
            node.values = new_values
        except Exception:
            pass
        return node

    def visit_MatchValue(self, node):
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        if self.inject_into_module and not self.injected:
            inject_string_machine_v6(node, self.machine_name)
            self.injected = True
        return node

    def visit_Constant(self, node):
        try:
            if isinstance(node.value, bool):
                return node
            if isinstance(node.value, str):
                if node.value == '':
                    return node
                if getattr(node, '_yuki_v6_done', False):
                    return node
                new_node = obfstr6(node.value, self.machine_name)
                try:
                    setattr(new_node, '_yuki_v6_done', True)
                except Exception:
                    pass
                return new_node
            return node
        except Exception:
            return node


def un():

    a, b = random.choice([(0x2160, 0x2170), (12353, 12355)])

    pool = [chr(i) for i in range(a, b)]

    return random.choice(pool) + ''.join(random.choices(pool, k=5))



def rd():return '_' + ''.join(__import__('random').sample([str(i) for i in range(44032, 55204)], k=3))

def random1():return ''.join(__import__('random').sample([str(i) for i in range(1000, 3000)], k=3))



def junk_code():return ast.Assign(targets=[ast.Name(id=rd(), ctx=ast.Store())], value=ast.Constant(value=True))

def junk_str():return ast.Expr(value=ast.Call(func=ast.Name(id=f'{_str}', ctx=ast.Load()), args=[ast.Constant(value=rd())], keywords=[]))

def random_Lol():return ast.If(test=ast.Compare(left=ast.Constant(value=random1()), ops=[ast.Eq()], comparators=[ast.Constant(value=random1())]), body=[ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]), cause=None)], orelse=[junk_code(), junk_str()])



def sieucaplongjunk(body, loop):

    # FIX BUG #14: never insert junk before 'from __future__' (must stay at top).

    try:

        _fut = [n for n in body if isinstance(n, ast.ImportFrom) and getattr(n, 'module', None) == '__future__']

        _rest = [n for n in body if n not in _fut]

    except Exception:

        _fut, _rest = [], list(body)

    ar = []

    for x in _rest:

        node = x

        for _ in range(1):

            node = ast.Try(body=[random_Lol(), x], handlers=[ast.ExceptHandler(type=ast.Name(id='MemoryError', ctx=ast.Load()), name=rd(), body=[junk_code(), junk_str()])], orelse=[junk_code(), junk_str()], finalbody=[junk_code()])

            node.body.append(ast.Raise(exc=ast.Call(func=ast.Name(id='MemoryError', ctx=ast.Load()), args=[], keywords=[]), cause=None))

        ar.append(node)

    try:

        ast.fix_missing_locations(ast.Module(body=_fut + ar, type_ignores=[]))

    except Exception:

        pass

    return _fut + ar



def junkcode1(code):

    v1 = 'NguㅤNhuㅤChoㅤBietㅤCaiㅤGì'+un()

    codonlenhdenh = un()+rb4()

    conmemay = rb4()+un()

    Lothanhchiton = rb()+un()

    OkiBeIu = un()+'MayㅤBietㅤCaiㅤGi'

    a = f'___BoMayLaHeHe__({anhxa("No1")})'

    return [Assign(targets=[Name(id=f'BOㅤLAㅤkhangcoder', ctx=Store())], value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Attribute(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Name(id=a, ctx=Load())), attr='__globals__', ctx=Load())), args=[], keywords=[]), lineno=0), Assign(targets=[Name(id=OkiBeIu, ctx=Store())], value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[arg(arg=Lothanhchiton)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id=Lothanhchiton, ctx=Load()), attr='__getitem__', ctx=Load()), args=[Constant(value='__builtins__')], keywords=[])), args=[Name(id=f'BOㅤLAㅤkhangcoder', ctx=Load())], keywords=[]), lineno=0), Assign(targets=[Name(id=codonlenhdenh, ctx=Store())], value=Constant(value=v1), lineno=0), Assign(targets=[Name(id=conmemay, ctx=Store())], value=Constant(value=True), lineno=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=v1)]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=True)])]), body=[Expr(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Constant(value=f'{rb()}Thằng Óc Cak{rbx()}')))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=v1)]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=False)])]), body=[Try(body=[Expr(value=Tuple(elts=[BinOp(left=Constant(value=1), op=Div(), right=Name(id=a, ctx=Load())), BinOp(left=Constant(value=123), op=Div(), right=Name(id=a, ctx=Load())), BinOp(left=Constant(value=999999), op=Div(), right=Name(id=a, ctx=Load()))], ctx=Load()))], handlers=[ExceptHandler(type=None, name=None, body=[code])], orelse=[], finalbody=[])], orelse=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id=codonlenhdenh, ctx=Load()), ops=[Eq()], comparators=[Constant(value=f'{rbx()}Biết Gì Không Mà Nhìn{rbx()}')]), Compare(left=Name(id=conmemay, ctx=Load()), ops=[Eq()], comparators=[Constant(value=False)])]), body=[Expr(value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id=OkiBeIu, ctx=Load()), attr=f'{__print}', ctx=Load()), args=[Constant(value='__BOLAKHANGCODER__')], keywords=[])), args=[], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Name(id=OkiBeIu, ctx=Load()), attr='_Ox1', ctx=Load()), args=[Constant(value=f'{rbx()}địt mẹ mày nhà may{rbx()}')], keywords=[]))])])])]



class junk1(ast.NodeTransformer):



    def visit_Module(self, node):

        if node.body:

            new_body = []

            for i, j in enumerate(node.body):

                if i in (0, len(node.body) - 1):

                    new_body.extend(junkcode1(j))

                else:

                    new_body.append(j)

            node.body = new_body

        return node





# --- UPGRADED FULL POWER PAYLOAD PROTECTION (injected) ---

UPGRADED_PAYLOAD_ANTIDEBUG = """

# FULL POWER ANTI-DEBUG PAYLOAD v2

import sys, os, time, ctypes, threading, builtins, types

def __yuki_full_anti_debug__():

    # fast exit helper

    def _exit(c): 

        try: os._exit(c)

        except: sys.exit(c)

    # 1. debugger present

    try:

        if sys.gettrace() is not None: _exit(95)

        if hasattr(sys, 'getprofile') and sys.getprofile() is not None: _exit(95)

    except: pass

    # 2. bad modules

    try:

        _bad = ('pdb','pydevd','debugpy','ptvsd','bdb','cProfile','pycdc','decompyle','uncompyle','xdis','pylingual','pyarmor','frida','r2pipe')

        for m in list(sys.modules.keys()):

            if any(x in m.lower() for x in _bad): _exit(96)

    except: pass

    # 3. IsDebuggerPresent

    try:

        _wd = getattr(ctypes, 'windll', None)

        if _wd is not None:

            _k = _wd.kernel32

            if _k.IsDebuggerPresent(): _exit(96)

            _isr = ctypes.c_bool(False)

            _k.CheckRemoteDebuggerPresent(_k.GetCurrentProcess(), ctypes.byref(_isr))

            if _isr.value: _exit(96)

    except: pass

    # 4. TracerPid

    try:

        if os.path.exists('/proc/self/status'):

            with open('/proc/self/status','r') as f:

                for l in f:

                    if l.startswith('TracerPid:') and l.split(':')[1].strip() != '0':

                        _exit(97)

    except: pass

    # 5. timing

    try:

        _t0 = time.perf_counter()

        [i for i in range(30000)]

        if time.perf_counter()-_t0 > 1.0: _exit(94)

    except: pass

    # 6. hook checks for builtins

    try:

        for _n in ('open','compile','eval','exec','__import__'):

            _o = getattr(builtins, _n, None)

            if _o and 'builtin' not in str(type(_o)):

                _exit(93)

    except: pass

# start watchdog daemon

try:

    if '__yuki_ad_started__' not in globals():

        globals()['__yuki_ad_started__'] = True

        try:

            import _thread as _th_ad

            _th_ad.start_new_thread(lambda: [__yuki_full_anti_debug__() or time.sleep(0.35) for _ in iter(int,1)], ())

        except Exception:

            _thr = threading.Thread(target=lambda: [__yuki_full_anti_debug__() or time.sleep(0.35) for _ in iter(int,1)], daemon=True)

            _thr.start()

        __yuki_full_anti_debug__()

except: pass

"""



rqprotect = r"""

import sys, os, types, re, logging, builtins, inspect, subprocess, platform, http.client, functools

def ___sexybeolol___():

    _bad_env_keys = ('PYTHONPATH', 'PYTHONHOME', 'PYTHONINSPECT', 'PYTHONBREAKPOINT', 'PYTHONDEVMODE', 'PYTHONTRACEMALLOC', 'PYTHONSTARTUP', 'HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'http_proxy', 'https_proxy', 'all_proxy', 'REQUESTS_CA_BUNDLE', 'CURL_CA_BUNDLE', 'SSL_CERT_FILE', 'SSL_CERT_DIR', 'FRIDA_PORT', 'MITMPROXY_PORT')

    _cur_env = getattr(KhangCoder('os'), 'environ', {})

    for _k in _bad_env_keys:

        if _k in _cur_env:

            try:

                import ctypes as _ct; _ct.memset(0, 0, 1)

            except: pass

            KhangCoder('os')._exit(137)

    _chk_dirs = [KhangCoder('sys').prefix, KhangCoder('os').getcwd()] + getattr(KhangCoder('sys'), 'path', [])

    for _d in _chk_dirs:

        if isinstance(_d, str) and _d and KhangCoder('os').path.isdir(_d):

            for _f in ('sitecustomize.py', 'usercustomize.py', 'sitecustomize.pyc', 'usercustomize.pyc'):

                if KhangCoder('os').path.exists(KhangCoder('os').path.join(_d, _f)):

                    KhangCoder('os')._exit(137)

    if platform.system().lower() == 'windows':

        try:

            import winreg

            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings') as _rk:

                _pe, _ = winreg.QueryValueEx(_rk, 'ProxyEnable')

                if _pe == 1:

                    _ps, _ = winreg.QueryValueEx(_rk, 'ProxyServer')

                    if any(_lh in str(_ps).lower() for _lh in ('127.0.0.1', 'localhost', ':8080', ':8888', ':8866', ':8008', ':9090')):

                        KhangCoder('os')._exit(137)

        except: pass

    try:

        import ssl

        if hasattr(ssl, '_create_default_https_context') and hasattr(ssl, '_create_unverified_context'):

            if ssl._create_default_https_context is ssl._create_unverified_context:

                KhangCoder('os')._exit(137)

    except: pass

    if platform.system().lower() != 'windows':return

    __codenhucak__ = ('wireshark', 'httptoolkit', 'fiddler', 'httpdebugger', 'charles', 'burp', 'burpsuite', 'mitmproxy', 'mitmdump', 'tcpdump', 'packetsender', 'proxyman', 'tshark', 'httpanalyzer', 'systeminformer', 'reqable', 'cheatengine', 'scylla', 'x64dbg', 'pydumper')

    try:

        import ctypes

        k32 = getattr(getattr(ctypes, 'windll', None), 'kernel32', None)

        if k32:

            class PROCESSENTRY32(ctypes.Structure):

                _fields_ = [('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong), ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t), ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong), ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long), ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_char * 260)]

            h = k32.CreateToolhelp32Snapshot(2, 0)

            if h != -1:

                pe = PROCESSENTRY32()

                pe.dwSize = ctypes.sizeof(PROCESSENTRY32)

                if k32.Process32First(h, ctypes.byref(pe)):

                    while True:

                        name = pe.szExeFile.decode('latin1', 'ignore').lower()

                        if any(x in name for x in __codenhucak__):

                            k32.CloseHandle(h)

                            raise SystemExit(137)

                        if not k32.Process32Next(h, ctypes.byref(pe)): break

                k32.CloseHandle(h)

    except SystemExit: raise

    except Exception: pass

def AntiTatMang():

    return True

if not AntiTatMang():raise MemoryError("khangcoder...")

def antihooksocketvuyp():

    try:

        dmmthgchooccak = __import__('socket').getaddrinfo

        if getattr(dmmthgchooccak, '__name__', '') not in ('getaddrinfo', '__silent_gai__'):

            raise RuntimeError('Hook detected')

        if hasattr(dmmthgchooccak, '__code__'):

            _cf = (getattr(dmmthgchooccak.__code__, 'co_filename', '') or '').lower()

            if _cf and '<' not in _cf and not _cf.endswith('socket.py') and 'socket' not in _cf:

                raise RuntimeError('Hook detected')

    except RuntimeError: raise

    except Exception: pass

class AntiUrllib3:

    def __init__(self):

        try:

            self.orig = KhangCoder('urllib3').connectionpool.HTTPConnectionPool.urlopen

            self.orig_code = getattr(self.orig, '__code__', None)

        except Exception:

            self.orig = None

            self.orig_code = None

    def check(self):

        if self.orig is None: return

        try:

            conchonhatco = KhangCoder('urllib3').connectionpool.HTTPConnectionPool.urlopen

            if conchonhatco is not self.orig:raise RuntimeError("khangcoder...")

            if getattr(conchonhatco, '__code__', None) != self.orig_code:raise RuntimeError("khangcoder...")

            if getattr(conchonhatco, '__module__', '') != "urllib3.connectionpool":raise RuntimeError("khangcoder...")

        except RuntimeError: raise

        except Exception: pass

___sexybeolol___()

bomaythichanti=AntiUrllib3()

bomaythichanti.check()

antihooksocketvuyp()

def __khangcoder__():

    if os.name != "nt":return

    try:

        import ctypes

        if ctypes.windll.kernel32.IsDebuggerPresent():raise MemoryError('khangcoder...')

        is_remote = ctypes.c_int(0)

        ctypes.windll.kernel32.CheckRemoteDebuggerPresent(-1, ctypes.byref(is_remote))

        if is_remote.value:raise MemoryError('khangcoder...')

    except:pass

try:

    from requests.status_codes import codes

    from urllib.parse import urljoin, urlparse

    from requests._internal_utils import to_native_string

    from requests.auth import _basic_auth_str

    from requests.cookies import extract_cookies_to_jar, merge_cookies

    from requests.exceptions import ChunkedEncodingError, ContentDecodingError, TooManyRedirects

    from requests.utils import DEFAULT_PORTS, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, rewind_body, should_bypass_proxies

except Exception:

    pass

if 'requests.sessions' in sys.modules:

    if hasattr(sys.modules['requests.sessions'].Session, 'request'):

        s = sys.modules['requests.sessions']

        if hasattr(s.Session, 'nhuconcak'):

            s.Session.request = s.Session.nhuconcak

if 'requests.sessions' in KhangCoder('sys').modules:

    if hasattr(KhangCoder('sys').modules['requests.sessions'].Session, 'request'):

        import requests.sessions

        if hasattr(requests.sessions.Session, '___LamLoiInjectHook__'):

            requests.sessions.Session.request = requests.sessions.Session.___LamLoiInjectHook__

logging.root.handlers = []

logging.root.setLevel(logging.CRITICAL)

for name in logging.root.manager.loggerDict:

    logger = logging.getLogger(name)

    logger.handlers = []

    logger.propagate = False

    logger.setLevel(logging.CRITICAL)

    logger.disabled = True

for logger_name in ['requests', 'urllib3', 'urllib3.connectionpool', 'urllib3.poolmanager', 'urllib3.util.retry', 'http.client', 'socket']:

    logger = logging.getLogger(logger_name)

    logger.handlers = []

    logger.propagate = False

    logger.setLevel(logging.CRITICAL)

    logger.disabled = True

import urllib3

__okok__ = None

__AEHOTCUT__ = None

class __ProTectSion__:pass

if hasattr(urllib3, 'connectionpool') and hasattr(urllib3.connectionpool, 'HTTPConnectionPool'):

    if hasattr(urllib3.connectionpool.HTTPConnectionPool, 'urlopen'):

        __okok__ = urllib3.connectionpool.HTTPConnectionPool.urlopen



        def __ThucHienTryBatToiPham__(self, method, url, *args, **kwargs):

            hidden_msg = ''

            old_loggers = {}

            for logger_name in ['urllib3', 'urllib3.connectionpool', 'urllib3.poolmanager']:

                logger = logging.getLogger(logger_name)

                old_loggers[logger_name] = {'disabled': logger.disabled, 'level': logger.level, 'handlers': logger.handlers[:]}

                logger.disabled = True

                logger.setLevel(logging.CRITICAL)

                logger.handlers = []

            old_print = builtins.print



            def anti_print(*args, **kwargs):

                pass

            builtins.print = anti_print

            old_stdout = sys.stdout.write

            old_stderr = sys.stderr.write



            def null_write(text):

                if isinstance(text, str) and ('http://' in text or 'https://' in text):

                    text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', hidden_msg, text)

                return len(text)

            sys.stdout.write = null_write

            sys.stderr.write = null_write

            try:

                result = __okok__(self, method, url, *args, **kwargs)

                return result

            finally:

                builtins.print = old_print

                sys.stdout.write = old_stdout

                sys.stderr.write = old_stderr

                for logger_name, old_config in old_loggers.items():

                    logger = logging.getLogger(logger_name)

                    logger.disabled = old_config['disabled']

                    logger.setLevel(old_config['level'])

                    logger.handlers = old_config['handlers']

        urllib3.connectionpool.HTTPConnectionPool.urlopen = __ThucHienTryBatToiPham__

logging_method = logging.Logger._log

def CodeAILam():

    loggers_to_disable = ['urllib3', 'urllib3.connectionpool', 'urllib3.connection', 'urllib3.poolmanager', 'urllib3.response', 'requests', 'requests.packages.urllib3', 'requests.adapters', 'requests.sessions', 'requests.api', 'requests.models', 'requests.hooks', 'requests.cookies', 'requests.auth', 'requests.exceptions', 'http.client', 'urllib3.util.retry', 'urllib3.util.timeout', 'socket', 'asyncio', 'websockets', 'websocket-client', 'os.write', 'os.open','ctypes.write']

    for logger_name in loggers_to_disable:

        logger = logging.getLogger(logger_name)

        logger.setLevel(logging.CRITICAL)

        logger.disabled = True

        for handler in logger.handlers[:]:

            logger.removeHandler(handler)

        logger.addHandler(logging.NullHandler())

    original_print = builtins.print



    def antidohaha(*args, **kwargs):

        msg = ' '.join((str(arg) for arg in args))

        if any((pattern in msg for pattern in ['http://', 'https://', 'LOG ERROR', 'www.'])):

            return

        return original_print(*args, **kwargs)

    builtins.print = antidohaha

    original_os_write = os.write



    def ditmecayko(fd, data):

        if isinstance(data, bytes):

            data_str = data.decode('utf-8', errors='ignore')

        else:

            data_str = str(data)

        if any((pattern in data_str for pattern in ['http://', 'https://'])):

            return len(data)

        return original_os_write(fd, data)

    os.write = ditmecayko

    try:

        libc = ctypes.CDLL(None)

        original_libc_write = libc.write

        @ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p, ctypes.c_size_t)

        def antilog(fd, buf, count):

            try:

                data = ctypes.string_at(buf, count)

                data_str = data.decode('utf-8', errors='ignore')

                if any((pattern in data_str for pattern in ['http://', 'https://', 'www.'])):

                    return count

            except:

                pass

            return original_libc_write(fd, buf, count)

        libc.write = antilog

    except:pass

    original_open = builtins.open



    class FilteredFile:



        def __init__(self, file_obj):

            self.file_obj = file_obj

            self.original_write = file_obj.write



            def filtered_write(data):

                if any((pattern in data for pattern in ['http://', 'https://', 'www.'])):

                    return len(data)

                return self.original_write(data)

            self.file_obj.write = filtered_write



        def __getattr__(self, name):

            return getattr(self.file_obj, name)



        def __enter__(self):

            return self



        def __exit__(self, *args):

            return self.file_obj.__exit__(*args)



    def filtered_open(file, mode='r', *args, **kwargs):

        f = original_open(file, mode, *args, **kwargs)

        if 'w' in mode or 'a' in mode:

            original_write = f.write



            def patched_write(data):

                if any((pattern in data for pattern in ['http://', 'https://', 'www.'])):

                    return len(data)

                return original_write(data)

            f.write = patched_write

        return f

    builtins.open = filtered_open

    try:

        from requests.adapters import HTTPAdapter

        def NgoLam(self, conn, url, verify, cert):

            if url.lower().startswith('https') and verify:

                cert_loc = None

                if verify is not True:

                    cert_loc = verify

                if not cert_loc:

                    try:

                        from requests.certs import where

                        cert_loc = where()

                    except:

                        cert_loc = None

                if not cert_loc or not os.path.exists(cert_loc):

                    conn.cert_reqs = 'CERT_REQUIRED'

                    conn.ca_certs = None

                else:

                    conn.cert_reqs = 'CERT_REQUIRED'

                    if not os.path.isdir(cert_loc):

                        conn.ca_certs = cert_loc

                    else:

                        conn.ca_cert_dir = cert_loc

            else:

                conn.cert_reqs = 'CERT_NONE'

                conn.ca_certs = None

                conn.ca_cert_dir = None

            if cert:

                if not isinstance(cert, (str, bytes)):

                    conn.cert_file = cert[0] if len(cert) > 0 else None

                    conn.key_file = cert[1] if len(cert) > 1 else None

                else:

                    conn.cert_file = cert

                    conn.key_file = None

        HTTPAdapter.cert_verify = NgoLam

        original_send = HTTPAdapter.send



        @functools.wraps(original_send)

        def silent_send(self, request, *args, **kwargs):

            old_stderr = sys.stderr

            old_stdout = sys.stdout

            from io import StringIO

            sys.stderr = StringIO()

            sys.stdout = StringIO()

            try:

                return original_send(self, request, *args, **kwargs)

            finally:

                sys.stderr = old_stderr

                sys.stdout = old_stdout

        HTTPAdapter.send = silent_send

    except (ImportError, AttributeError):pass

    try:

        import requests.sessions

        KhocChuaEm = requests.sessions.Session.request

        @functools.wraps(KhocChuaEm)

        def silent_session_request(self, method, url, **kwargs):

            result = KhocChuaEm(self, method, url, **kwargs)

            return result

        requests.sessions.Session.request = silent_session_request

    except (ImportError, AttributeError):pass

CodeAILam()

BanGoc_In = builtins.print



def ___khangcoder___(*args, **kwargs):

    new_args = []

    for arg in args:

        if isinstance(arg, str):

            arg = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', arg)

            arg = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', arg)

            arg = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', arg)

            arg = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', arg)

            arg = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', arg)

        new_args.append(arg)

    BanGoc_In(*new_args, **kwargs)

builtins.print = ___khangcoder___

__EmChacChua__ = sys.stdout.write

__TrollStore__ = sys.stderr.write



def ___Abyss___(text):

    if isinstance(text, str):

        text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)

        text = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)

        text = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', text)

        text = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', text)

        text = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', text)

    return __EmChacChua__(text)



def ___BOMAYLANHAT___(text):

    if isinstance(text, str):

        text = re.sub('https?://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)

        text = re.sub('ftp://[^\\s\\\'\\"<>(){}]+', 'HOOK CÁI LÔL', text)

        text = re.sub('__hid_[0-9a-f]+__', 'HOOK CÁI LÔL', text)

        text = re.sub('\\[Urllib3\\]', 'HOOK CÁI LÔL', text)

        text = re.sub('\\[Url\\]', 'HOOK CÁI LÔL', text)

    return __TrollStore__(text)

sys.stdout.write = ___Abyss___

sys.stderr.write = ___BOMAYLANHAT___

try:

    import requests

    _xamlol_ = requests.sessions.Session.request

    requests.sessions.Session._xamlol_ = _xamlol_



    def anrequests(self, method, url, *args, **kwargs):

        urlthat = url

        result = _xamlol_(self, method, urlthat, *args, **kwargs)



        class HiddenUrl(str):



            def __new__(cls, url):

                obj = str.__new__(cls, 'https://hookcailolmemay.com')

                obj._real = url

                return obj



            def __repr__(self):

                return "'https://hookcailolmemay.com'"



            def __str__(self):

                return 'https://hookcailolmemay.com'

        result.url = HiddenUrl(urlthat)

        if hasattr(result, 'request'):

            result.request.url = HiddenUrl(urlthat)

        return result

    requests.sessions.Session.request = anrequests

except:pass



class Session:



    def __init__(self):

        self.headers=KhangCoder('requests.structures',fromlist=['*']).CaseInsensitiveDict({'User-Agent':'python-requests/2.31.0','Accept-Encoding':', '.join(('gzip','deflate')),'Accept':'*/*','Connection':'keep-alive'})

        self.auth = None

        self.proxies = {}

        self.hooks = {event: [] for event in ['response']}

        self.params = {}

        self.stream = False

        self.verify = True

        self.cert = None

        self.max_redirects = 30

        self.trust_env = False # UPGRADE: Anti-Proxy MITM bypass

        self.cookies=KhangCoder('requests.cookies',fromlist=['*']).cookiejar_from_dict({})

        self.adapters = KhangCoder('collections').OrderedDict()

        self.HTTPAdapter=KhangCoder('requests.adapters',fromlist=['*']).HTTPAdapter()

        self._real_urls = {}

        self._url_counter = 0

        if KhangCoder('sys').platform == 'win32':

            try:

                self.preferred_clock = KhangCoder('time').perf_counter

            except AttributeError:

                self.preferred_clock = KhangCoder('time').clock

        else:

            self.preferred_clock = KhangCoder('time').time

        self.mount('https://', self.HTTPAdapter)

        self.mount('http://', self.HTTPAdapter)



    def __NhoThuongNgAy__(self, url):

        self._url_counter += 1

        hidden_id = f'__ProJect_{self._url_counter:08x}__'

        self._real_urls[hidden_id] = url

        return hidden_id



    def __TraChoAnhTuDo__(self, hidden_url):

        return self._real_urls.get(hidden_url, hidden_url)



    def __DsQ2__(self, resp):

        if resp.is_redirect:

            location = resp.headers['location']

            _ver = KhangCoder('sys').version_info

            is_py3 = _ver[0] == 3

            if is_py3:

                location = location.encode('latin1')

            return to_native_string(location, 'utf8')

        return None



    def should_strip_auth(self, old_url, new_url):

        old_parsed = urlparse(old_url)

        new_parsed = urlparse(new_url)

        if old_parsed.hostname != new_parsed.hostname:

            return True

        if old_parsed.scheme == 'http' and old_parsed.port in (80, None) and (new_parsed.scheme == 'https') and (new_parsed.port in (443, None)):

            return False

        changed_port = old_parsed.port != new_parsed.port

        changed_scheme = old_parsed.scheme != new_parsed.scheme

        default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)

        if not changed_scheme and old_parsed.port in default_port and (new_parsed.port in default_port):

            return False

        return changed_port or changed_scheme



    def __Nho_Anh_Khong__(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):

        hist = []

        url = self.__DsQ2__(resp)

        previous_fragment = urlparse(req.url).fragment

        while url:

            prepared_request = req.copy()

            hist.append(resp)

            resp.history = hist[1:]

            try:

                resp.content

            except (ChunkedEncodingError, ContentDecodingError, RuntimeError):

                resp.raw.read(decode_content=False)

            if len(resp.history) >= self.max_redirects:

                raise TooManyRedirects('Exceeded {} redirects.'.format(self.max_redirects), response=resp)

            resp.close()

            if url.startswith('//'):

                parsed_rurl = urlparse(resp.url)

                url = ':'.join([to_native_string(parsed_rurl.scheme), url])

            parsed = urlparse(url)

            if parsed.fragment == '' and previous_fragment:

                parsed = parsed._replace(fragment=previous_fragment)

            elif parsed.fragment:

                previous_fragment = parsed.fragment

            url = parsed.geturl()

            if not parsed.netloc:

                url = urljoin(resp.url, requote_uri(url))

            else:

                url = requote_uri(url)

            prepared_request.url = to_native_string(url)

            self.rebuild_method(prepared_request, resp)

            if resp.status_code not in (codes.temporary_redirect, codes.permanent_redirect):

                purged_headers = ('Content-Length', 'Content-Type', 'Transfer-Encoding')

                for header in purged_headers:

                    prepared_request.headers.pop(header, None)

                prepared_request.body = None

            headers = prepared_request.headers

            headers.pop('Cookie', None)

            extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)

            merge_cookies(prepared_request._cookies, self.cookies)

            prepared_request.prepare_cookies(prepared_request._cookies)

            proxies = self.rebuild_proxies(prepared_request, proxies)

            self.rebuild_auth(prepared_request, resp)

            rewindable = prepared_request._body_position is not None and ('Content-Length' in headers or 'Transfer-Encoding' in headers)

            if rewindable:

                rewind_body(prepared_request)

            req = prepared_request

            if yield_requests:

                yield req

            else:

                resp = self.send(req, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies, allow_redirects=False, **adapter_kwargs)

                extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)

                url = self.__DsQ2__(resp)

                yield resp



    def rebuild_auth(self, prepared_request, response):

        headers = prepared_request.headers

        url = prepared_request.url

        if 'Authorization' in headers and self.should_strip_auth(response.request.url, url):

            del headers['Authorization']

        new_auth = get_netrc_auth(url) if self.trust_env else None

        if new_auth is not None:

            prepared_request.prepare_auth(new_auth)



    def rebuild_proxies(self, prepared_request, proxies):

        proxies = proxies if proxies is not None else {}

        headers = prepared_request.headers

        url = prepared_request.url

        scheme = urlparse(url).scheme

        new_proxies = proxies.copy()

        no_proxy = proxies.get('no_proxy')

        bypass_proxy = should_bypass_proxies(url, no_proxy=no_proxy)

        if self.trust_env and (not bypass_proxy):

            environ_proxies = get_environ_proxies(url, no_proxy=no_proxy)

            proxy = environ_proxies.get(scheme, environ_proxies.get('all'))

            if proxy:

                new_proxies.setdefault(scheme, proxy)

        if 'Proxy-Authorization' in headers:

            del headers['Proxy-Authorization']

        try:

            username, password = get_auth_from_url(new_proxies[scheme])

        except KeyError:

            username, password = (None, None)

        if not scheme.startswith('https') and username and password:

            headers['Proxy-Authorization'] = _basic_auth_str(username, password)

        return new_proxies



    def rebuild_method(self, prepared_request, response):

        method = prepared_request.method

        if response.status_code == codes.see_other and method != 'HEAD':

            method = 'GET'

        if response.status_code == codes.found and method != 'HEAD':

            method = 'GET'

        if response.status_code == codes.moved and method == 'POST':

            method = 'GET'

        prepared_request.method = method



    def __enter__(self):

        return self



    def __exit__(self, *args):

        for v in self.adapters.values():

            v.close()



    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):

        hidden_url = self.__NhoThuongNgAy__(url)

        req=KhangCoder('requests.models',fromlist=['*']).Request(method=method.upper(),url=hidden_url,headers=headers,files=files,data=data or {},json=json,params=params or {},auth=auth,cookies=cookies,hooks=hooks)

        req._real_url = url

        cookies = req.cookies or {}

        if not isinstance(cookies, KhangCoder('http').cookiejar.CookieJar):

            cookies=KhangCoder('requests.cookies',fromlist=['*']).cookiejar_from_dict(cookies)

        auth = req.auth

        if self.trust_env and (not auth) and (not self.auth):

            auth = KhangCoder('requests').utils.get_netrc_auth(req.url)

        prep=KhangCoder('requests.models',fromlist=['*']).PreparedRequest()

        req.url = url

        prep.prepare(method=req.method.upper(),url=req.url,files=req.files,data=req.data,json=req.json,headers=self.merge_setting(req.headers,self.headers,dict_class=KhangCoder('requests.structures',fromlist=['*']).CaseInsensitiveDict),params=self.merge_setting(req.params,self.params),auth=self.merge_setting(auth,self.auth),cookies=KhangCoder('requests.cookies',fromlist=['*']).merge_cookies(KhangCoder('requests.cookies',fromlist=['*']).merge_cookies(KhangCoder('requests.cookies',fromlist=['*']).RequestsCookieJar(),self.cookies),cookies),hooks=self.merge_hooks(req.hooks,self.hooks))

        prep._real_url = url

        prep.url = hidden_url

        send_kwargs = {'timeout': timeout, 'allow_redirects': allow_redirects}

        stream = stream

        verify = verify

        cert = cert

        proxies = proxies or {}

        if self.trust_env:

            no_proxy = proxies.get('no_proxy') if proxies is not None else None

            env_proxies = KhangCoder('requests').utils.get_environ_proxies(url, no_proxy=no_proxy)

            for k, v in env_proxies.items():

                proxies.setdefault(k, v)

            if verify is True or verify is None:

                verify = KhangCoder('os').environ.get('REQUESTS_CA_BUNDLE') or KhangCoder('os').environ.get('CURL_CA_BUNDLE')

        send_kwargs.update({'verify': self.merge_setting(verify, self.verify), 'proxies': self.merge_setting(proxies, self.proxies), 'stream': self.merge_setting(stream, self.stream), 'cert': self.merge_setting(cert, self.cert)})

        return self.send(prep, **send_kwargs)



    def get(self, url, **kwargs):

        kwargs.setdefault('allow_redirects', True)

        return self.request('GET', url, **kwargs)



    def post(self, url, data=None, json=None, **kwargs):

        return self.request('POST', url, data=data, json=json, **kwargs)



    def merge_setting(self, request_setting, session_setting, dict_class=None):

        if session_setting is None:

            return request_setting

        if request_setting is None:

            return session_setting

        if isinstance(session_setting, dict) and isinstance(request_setting, dict):

            result = dict_class(session_setting) if dict_class is not None else session_setting.copy()

            result.update(request_setting)

            return result

        return request_setting



    def merge_hooks(self, request_hooks, session_hooks):

        merged = {}

        for key in set(session_hooks.keys()).union(request_hooks.keys()):

            merged[key] = []

            if key in session_hooks:

                if isinstance(session_hooks[key], list):

                    merged[key].extend(session_hooks[key])

                else:

                    merged[key].append(session_hooks[key])

            if key in request_hooks:

                if isinstance(request_hooks[key], list):

                    merged[key].extend(request_hooks[key])

                else:

                    merged[key].append(request_hooks[key])

        return merged



    def send(self, request, **kwargs):

        kwargs.setdefault('stream', self.stream)

        kwargs.setdefault('verify', self.verify)

        kwargs.setdefault('cert', self.cert)

        kwargs.setdefault('proxies', self.proxies)

        if isinstance(request,KhangCoder('requests.models',fromlist=['*']).Request):

            raise ValueError('You can only send PreparedRequests.')

        allow_redirects = kwargs.pop('allow_redirects', True)

        start = self.preferred_clock()

        if hasattr(request, '_real_url'):

            real_url = request._real_url

            for prefix, adapter in self.adapters.items():

                if real_url.lower().startswith(prefix.lower()):

                    request.url = real_url

                    r = adapter.send(request, **kwargs)

                    break

            else:

                raise KhangCoder('requests').exceptions.InvalidSchema('No connection adapters were found for {!r}'.format(real_url))

        else:

            urls = request.url

            try:

                for prefix, adapter in self.adapters.items():

                    if urls.lower().startswith(prefix.lower()):

                        r = adapter.send(request, **kwargs)

            except:

                raise KhangCoder('requests').exceptions.InvalidSchema('No connection adapters were found for {!r}'.format(urls))

        if hasattr(request, '_real_url'):

            r.url = self.__NhoThuongNgAy__(request._real_url)

            r._real_url = request._real_url

        elapsed = self.preferred_clock() - start

        r.elapsed = KhangCoder('datetime').timedelta(seconds=elapsed)

        hooks = request.hooks or {}

        hooks = hooks.get('response')

        if hooks:

            if hasattr(hooks, '__call__'):

                hooks = [hooks]

            for hook in hooks:

                _hook_data = hook(r, **kwargs)

                if _hook_data is not None:

                    r = _hook_data

        if r.history:

            for resp in r.history:

                KhangCoder('requests').cookies.extract_cookies_to_jar(self.cookies, resp.request, resp.raw)

        KhangCoder('requests.cookies',fromlist=['*']).extract_cookies_to_jar(self.cookies,request,r.raw)

        if allow_redirects:

            history = [resp for resp in self.__Nho_Anh_Khong__(r, request, **kwargs)]

        else:

            history = []

        if history:

            history.insert(0, r)

            r = history.pop()

            r.history = history

        if not allow_redirects:

            try:

                r._next = next(self.__Nho_Anh_Khong__(r, request, yield_requests=True, **kwargs))

            except StopIteration:

                pass

        if not kwargs.get('stream'):

            r.content

        return r



    def mount(self, prefix, adapter):

        self.adapters[prefix] = adapter

        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]

        for key in keys_to_move:

            self.adapters[key] = self.adapters.pop(key)

    def __getstate__(self):

        return {attr: getattr(self, attr, None) for attr in ['headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify', 'cert', 'adapters', 'stream', 'trust_env', 'max_redirects']}

    def __setstate__(self, state):

        for attr, value in state.items():

            setattr(self, attr, value)



def request(method, url, **kwargs):

    with Session() as session:

        return session.request(method=method, url=url, **kwargs)

def get(url, params=None, **kwargs):

    kwargs.setdefault('allow_redirects', True)

    return request('get', url, params=params, **kwargs)

def post(url, data=None, json=None, **kwargs):

    return request('post', url, data=data, json=json, **kwargs)

KhangCoder('requests').get = get

KhangCoder('requests').post = post

KhangCoder('requests').Session = Session

def ___AntiProxyVip___():

    __env_proxy__=['HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy','SOCKS_PROXY','socks_proxy','WS_PROXY','ws_proxy','REQUESTS_CA_BUNDLE','CURL_CA_BUNDLE','SSL_CERT_FILE','SSL_CERT_DIR','SSLKEYLOGFILE','HTTP_PROXY_USER','HTTPS_PROXY_USER','GRPC_PROXY_EXP','HTTPS_PROXY_CLIENT','PROXY','proxy']

    __env_lower__={k.lower() for k in __env_proxy__}

    for __k__ in list(KhangCoder('os').environ.keys()):

        if __k__.lower() in __env_lower__:KhangCoder('os').environ.pop(__k__,None)

    KhangCoder('os').environ['NO_PROXY']='*'

    KhangCoder('os').environ['no_proxy']='*'

___AntiProxyVip___()

def ___AntiLogMethodVip___():

    __orig_log__=logging.Logger._log

    def __filtered_log__(self,level,msg,args,exc_info=None,extra=None,stack_info=False,stacklevel=1):

        if isinstance(msg,str):

            if 'http://' in msg or 'https://' in msg or 'www.' in msg or '__ProJect_' in msg or 'ftp://' in msg:return

            if '://' in msg and ('github' in msg or 'google' in msg or 'http' in msg):return

        if args:

            try:

                __joined__=' '.join(str(a) for a in args)

                if 'http://' in __joined__ or 'https://' in __joined__ or 'www.' in __joined__:return

            except:pass

        return __orig_log__(self,level,msg,args,exc_info=exc_info,extra=extra,stack_info=stack_info,stacklevel=stacklevel)

    logging.Logger._log=__filtered_log__

___AntiLogMethodVip___()

def ___AntiAuditHookVip___():

    if hasattr(KhangCoder('sys'),'addaudithook'):

        def __block_audithook__(hook,*a,**k):pass

        KhangCoder('sys').addaudithook=__block_audithook__

    if hasattr(KhangCoder('sys'),'_audit_hooks'):

        try:KhangCoder('sys')._audit_hooks.clear()

        except:pass

___AntiAuditHookVip___()

def ___AntiTraceHookVip___():

    def __trace_guard_vip__(f=None,*a,**k):

        if f is not None:

            _q = str(f).lower()

            _m = str(getattr(f, '__module__', '')).lower()

            if any(x in _q or x in _m for x in ('debug', 'trace', 'pydev', 'ptvsd', 'pdb', 'hook', 'dump', 'inspect', 'decomp')):

                try:

                    import ctypes

                    ctypes.windll.kernel32.ExitProcess(95)

                except: pass

                try: __import__('os')._exit(95)

                except: pass

    KhangCoder('sys').settrace=__trace_guard_vip__

    KhangCoder('sys').setprofile=__trace_guard_vip__

    try:KhangCoder('threading').settrace=__trace_guard_vip__

    except:pass

___AntiTraceHookVip___()

def ___AntiUrllibHookVip___():

    try:

        __ur__=KhangCoder('urllib.request',fromlist=['*'])

        if hasattr(__ur__,'urlopen'):

            __orig_uo__=__ur__.urlopen

            def __silent_urlopen__(url,*a,**k):

                __saved__={}

                for __ln__ in ['urllib','urllib.request','urllib3','urllib3.connectionpool','urllib3.poolmanager','http.client','socket']:

                    __lg__=logging.getLogger(__ln__)

                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}

                    __lg__.disabled=True

                    __lg__.setLevel(logging.CRITICAL)

                    __lg__.handlers=[]

                __old_p__=builtins.print

                builtins.print=lambda *a,**k:None

                try:return __orig_uo__(url,*a,**k)

                finally:

                    builtins.print=__old_p__

                    for __ln__,__cfg__ in __saved__.items():

                        __lg__=logging.getLogger(__ln__)

                        __lg__.disabled=__cfg__['disabled']

                        __lg__.setLevel(__cfg__['level'])

                        __lg__.handlers=__cfg__['handlers']

            __ur__.urlopen=__silent_urlopen__

        if hasattr(__ur__,'URLopener') and hasattr(__ur__.URLopener,'open'):

            __orig_op__=__ur__.URLopener.open

            def __silent_op__(self,url,*a,**k):

                __saved__={}

                for __ln__ in ['urllib','urllib.request','urllib3','http.client']:

                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True

                try:return __orig_op__(self,url,*a,**k)

                finally:

                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__

            __ur__.URLopener.open=__silent_op__

        if hasattr(__ur__,'OpenerDirector') and hasattr(__ur__.OpenerDirector,'open'):

            __orig_od__=__ur__.OpenerDirector.open

            def __silent_od__(self,url,*a,**k):

                __saved__={}

                for __ln__ in ['urllib','urllib.request','urllib3','http.client']:

                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True

                try:return __orig_od__(self,url,*a,**k)

                finally:

                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__

            __ur__.OpenerDirector.open=__silent_od__

    except:pass

___AntiUrllibHookVip___()

def ___AntiHTTPDebugVip___():

    try:

        __hc__=KhangCoder('http.client')

        if hasattr(__hc__,'HTTPConnection'):

            __orig_init__=__hc__.HTTPConnection.__init__

            def __silent_init__(self,*a,**k):

                __orig_init__(self,*a,**k)

                self.debuglevel=0

            __hc__.HTTPConnection.__init__=__silent_init__

            try:__hc__.HTTPConnection.debuglevel=0

            except:pass

        if hasattr(__hc__,'HTTPResponse'):

            __orig_ri__=__hc__.HTTPResponse.__init__

            def __silent_ri__(self,*a,**k):

                __orig_ri__(self,*a,**k)

                self.debuglevel=0

            __hc__.HTTPResponse.__init__=__silent_ri__

        if hasattr(__hc__,'HTTPConnection') and hasattr(__hc__.HTTPConnection,'set_debuglevel'):

            __orig_sd__=__hc__.HTTPConnection.set_debuglevel

            def __silent_sd__(self,level):

                return __orig_sd__(self,0)

            __hc__.HTTPConnection.set_debuglevel=__silent_sd__

    except:pass

___AntiHTTPDebugVip___()

def ___AntiPoolManagerLogVip___():

    try:

        __pm__=KhangCoder('urllib3.poolmanager',fromlist=['*'])

        if hasattr(__pm__,'PoolManager') and hasattr(__pm__.PoolManager,'urlopen'):

            __orig_pmuo__=__pm__.PoolManager.urlopen

            def __silent_pmuo__(self,method,url,*a,**k):

                __saved__={}

                for __ln__ in ['urllib3','urllib3.connectionpool','urllib3.poolmanager','requests','http.client']:

                    __lg__=logging.getLogger(__ln__)

                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}

                    __lg__.disabled=True

                    __lg__.setLevel(logging.CRITICAL)

                    __lg__.handlers=[]

                __old_p__=builtins.print

                builtins.print=lambda *a,**k:None

                try:return __orig_pmuo__(self,method,url,*a,**k)

                finally:

                    builtins.print=__old_p__

                    for __ln__,__cfg__ in __saved__.items():

                        __lg__=logging.getLogger(__ln__)

                        __lg__.disabled=__cfg__['disabled']

                        __lg__.setLevel(__cfg__['level'])

                        __lg__.handlers=__cfg__['handlers']

            __pm__.PoolManager.urlopen=__silent_pmuo__

    except:pass

___AntiPoolManagerLogVip___()

def ___AntiHTTPConnLogVip___():

    try:

        __hc__=KhangCoder('http.client')

        if hasattr(__hc__,'HTTPConnection'):

            __orig_putreq__=__hc__.HTTPConnection.putrequest

            def __silent_putreq__(self,method,url,*a,**k):

                __saved__={}

                for __ln__ in ['http.client','urllib3','urllib3.connectionpool','requests']:

                    __lg__=logging.getLogger(__ln__)

                    __saved__[__ln__]={'disabled':__lg__.disabled,'level':__lg__.level,'handlers':__lg__.handlers[:]}

                    __lg__.disabled=True

                    __lg__.setLevel(logging.CRITICAL)

                    __lg__.handlers=[]

                __old_p__=builtins.print

                builtins.print=lambda *a,**k:None

                try:return __orig_putreq__(self,method,url,*a,**k)

                finally:

                    builtins.print=__old_p__

                    for __ln__,__cfg__ in __saved__.items():

                        __lg__=logging.getLogger(__ln__)

                        __lg__.disabled=__cfg__['disabled']

                        __lg__.setLevel(__cfg__['level'])

                        __lg__.handlers=__cfg__['handlers']

            __hc__.HTTPConnection.putrequest=__silent_putreq__

    except:pass

___AntiHTTPConnLogVip___()

def ___AntiLibcWriteVip___():

    try:

        import ctypes

        if hasattr(ctypes,'CDLL'):

            try:

                __libc__=ctypes.CDLL(None)

                if hasattr(__libc__,'write'):

                    __orig_lw__=__libc__.write

                    @ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_size_t)

                    def __anti_libc_write__(fd,buf,count):

                        try:

                            __data__=ctypes.string_at(buf,count)

                            __data_str__=__data__.decode('utf-8',errors='ignore')

                            if 'http://' in __data_str__ or 'https://' in __data_str__ or 'www.' in __data_str__ or '__ProJect_' in __data_str__:return count

                        except:pass

                        return __orig_lw__(fd,buf,count)

                    __libc__.write=__anti_libc_write__

            except:pass

            if KhangCoder('os').name=='nt':

                try:

                    __msvc__=ctypes.CDLL('msvcrt.dll')

                    if hasattr(__msvc__,'write'):

                        __orig_mw__=__msvc__.write

                        @ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_void_p,ctypes.c_size_t)

                        def __anti_msvc_write__(fd,buf,count):

                            try:

                                __data__=ctypes.string_at(buf,count)

                                __data_str__=__data__.decode('utf-8',errors='ignore')

                                if 'http://' in __data_str__ or 'https://' in __data_str__ or 'www.' in __data_str__:return count

                            except:pass

                            return __orig_mw__(fd,buf,count)

                        __msvc__.write=__anti_msvc_write__

                except:pass

                try:

                    __k32__=ctypes.WinDLL('kernel32')

                    if hasattr(__k32__,'WriteFile'):

                        __orig_wf__=__k32__.WriteFile

                        __k32__.WriteFile=__anti_msvc_write__

                except:pass

    except:pass

___AntiLibcWriteVip___()

def ___AntiSocketSendLogVip___():

    try:

        __sk__=KhangCoder('socket')

        if hasattr(__sk__,'socket'):

            __orig_sendto__=__sk__.socket.sendto

            def __silent_sendto__(self,data,*a,**k):

                __saved__={}

                for __ln__ in ['socket','http.client','urllib3','urllib3.connectionpool']:

                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True

                try:return __orig_sendto__(self,data,*a,**k)

                finally:

                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__

            __sk__.socket.sendto=__silent_sendto__

    except:pass

___AntiSocketSendLogVip___()

def ___AntiGetaddrinfoLogVip___():

    try:

        __sk__=KhangCoder('socket')

        if hasattr(__sk__,'getaddrinfo'):

            __orig_gai__=__sk__.getaddrinfo

            def __silent_gai__(host,*a,**k):

                __saved__={}

                for __ln__ in ['socket','http.client','urllib3','urllib3.connectionpool','requests']:

                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True

                __old_p__=builtins.print

                builtins.print=lambda *a,**k:None

                try:return __orig_gai__(host,*a,**k)

                finally:

                    builtins.print=__old_p__

                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__

            try:functools.update_wrapper(__silent_gai__,__orig_gai__)

            except:pass

            __sk__.getaddrinfo=__silent_gai__

        if hasattr(__sk__,'gethostbyname'):

            __orig_ghn__=__sk__.gethostbyname

            def __silent_ghn__(host,*a,**k):

                __saved__={}

                for __ln__ in ['socket','http.client','urllib3']:

                    __lg__=logging.getLogger(__ln__);__saved__[__ln__]=__lg__.disabled;__lg__.disabled=True

                try:return __orig_ghn__(host,*a,**k)

                finally:

                    for __ln__,__v__ in __saved__.items():logging.getLogger(__ln__).disabled=__v__

            try:functools.update_wrapper(__silent_ghn__,__orig_ghn__)

            except:pass

            __sk__.gethostbyname=__silent_ghn__

    except:pass

___AntiGetaddrinfoLogVip___()

def ___AntiTracebackSourceVip___():

    try:

        __tb__=KhangCoder('traceback',fromlist=['*'])

        if hasattr(__tb__,'extract_stack'):

            __orig_es__=__tb__.extract_stack

            def __silent_es__(*a,**k):

                try:return __orig_es__(*a,**k)

                except:return []

            __tb__.extract_stack=__silent_es__

    except:pass

    try:

        __ic__=KhangCoder('inspect',fromlist=['*'])

        if hasattr(__ic__,'stack'):

            __orig_st__=__ic__.stack

            def __silent_st__(*a,**k):

                try:return __orig_st__(*a,**k)

                except:return []

            __ic__.stack=__silent_st__

    except:pass

___AntiTracebackSourceVip___()

def ___VerifyAntiHookVip___():

    try:

        _ln = getattr(getattr(logging, 'Logger', None), '_log', None)

        if _ln and 'filtered_log' not in getattr(_ln, '__name__', ''):

            raise MemoryError('khangcoder...')

    except MemoryError:raise

    except:pass

___VerifyAntiHookVip___()

__khangcoder__()



"""







# ==================== VÔ ĐỐI REQUESTS PROTECTION - LUÔN BẬT ====================

RQ_VODAI_SUPER = r'''
# VÔ ĐỐI ANTI HOOK + ẨN URL RUNTIME - INVINCIBLE (UPGRADED ENTERPRISE ANTI-HOOK & NATIVE SENTINEL)
import sys as __sys_vodai__, os as __os_vodai__, threading as __th_vodai__, time as __time_vodai__, builtins as __bi_vodai__, types as __types_vodai__, logging as __log_vodai__, re as __re_vodai__, inspect as __ins_vodai__, http.client as __http_vodai__, socket as __sock_vodai__, struct as __st_vodai__
try:
    import marshal as __marshal_vodai__
except:
    __marshal_vodai__ = None

# === SUPER EXIT: MULTI-TIER INSTANT PROCESS TERMINATION ===
def __Yuki_VoDoi_Exit__(c=95):
    try:
        import ctypes as _ct_exit
        _k32_exit = getattr(getattr(_ct_exit, 'windll', None), 'kernel32', None)
        if _k32_exit and hasattr(_k32_exit, 'TerminateProcess'):
            _k32_exit.TerminateProcess(_k32_exit.GetCurrentProcess(), 0xC0000005)
        _nt_exit = getattr(getattr(_ct_exit, 'windll', None), 'ntdll', None)
        if _nt_exit and hasattr(_nt_exit, 'NtTerminateProcess'):
            _nt_exit.NtTerminateProcess(-1, 0xC0000005)
        _ct_exit.memset(0, 0, 1)
    except: pass
    try:
        import os as _os_kill
        if hasattr(_os_kill, 'abort'): _os_kill.abort()
    except: pass
    try:
        import ctypes as _ct_exit
        _k32_exit = getattr(getattr(_ct_exit, 'windll', None), 'kernel32', None)
        if _k32_exit and hasattr(_k32_exit, 'ExitProcess'):
            _k32_exit.ExitProcess(c)
    except: pass
    try:
        import os as _os_kill
        if hasattr(_os_kill, 'kill') and hasattr(_os_kill, 'getpid'):
            _os_kill.kill(_os_kill.getpid(), 9)
    except: pass
    try:
        __os_vodai__._exit(c)
    except:
        try: __sys_vodai__.exit(c)
        except: pass
    try: raise SystemExit(c)
    except: pass

# === ANTI-DECOMPILER (PyCDC / PyLingual) CRASH TRAP ===
try:
    def _pycdc_trap(n):
        if n <= 0: return 0
        return _pycdc_trap(n - 1) + 1
    _old_rec = __sys_vodai__.getrecursionlimit()
    __sys_vodai__.setrecursionlimit(max(_old_rec, 3000))
    _pycdc_trap(150)
    __sys_vodai__.setrecursionlimit(_old_rec)
except Exception: pass
try:
    if __marshal_vodai__:
        __marshal_vodai__.loads(b'\x09\x00' * 256)
except Exception: pass

# === DEEP C-BUILTIN ANTI-HOOKING SNAPSHOT & VERIFICATION ===
__Yuki_Builtins_Snapshot__ = {
    'exec': getattr(__bi_vodai__, 'exec', None),
    'eval': getattr(__bi_vodai__, 'eval', None),
    'compile': getattr(__bi_vodai__, 'compile', None),
    '__import__': getattr(__bi_vodai__, '__import__', None),
    'open': getattr(__bi_vodai__, 'open', None),
    'getattr': getattr(__bi_vodai__, 'getattr', None),
    'setattr': getattr(__bi_vodai__, 'setattr', None),
    'loads': getattr(__marshal_vodai__, 'loads', None) if __marshal_vodai__ else None,
    'dumps': getattr(__marshal_vodai__, 'dumps', None) if __marshal_vodai__ else None,
    'gettrace': getattr(__sys_vodai__, 'gettrace', None),
    'settrace': getattr(__sys_vodai__, 'settrace', None),
    '_getframe': getattr(__sys_vodai__, '_getframe', None),
    'FunctionType': getattr(__types_vodai__, 'FunctionType', None),
}

def __check_deep_builtin_hooks__():
    try:
        for _name, _orig in __Yuki_Builtins_Snapshot__.items():
            if not _orig: continue
            _cur = None
            if _name in ('loads', 'dumps'):
                _cur = getattr(__marshal_vodai__, _name, None) if __marshal_vodai__ else None
            elif _name in ('settrace', 'gettrace', '_getframe'):
                _cur = getattr(__sys_vodai__, _name, None)
            elif _name == 'FunctionType':
                _cur = getattr(__types_vodai__, _name, None)
            else:
                _cur = getattr(__bi_vodai__, _name, None)

            if _name == 'open' and getattr(_cur, '__name__', '') == 'filtered_open':
                continue
            if _name == 'settrace' and getattr(_cur, '__name__', '') in ('__trace_guard_vip__', '__vodai_trace_guard__'):
                continue

            if _cur is not _orig:
                try:
                    if _name in ('loads', 'dumps') and __marshal_vodai__:
                        setattr(__marshal_vodai__, _name, _orig)
                    elif _name in ('settrace', 'gettrace', '_getframe'):
                        setattr(__sys_vodai__, _name, _orig)
                    elif _name == 'FunctionType':
                        setattr(__types_vodai__, _name, _orig)
                    elif _name != 'open':
                        setattr(__bi_vodai__, _name, _orig)
                except Exception: pass
                return True

            if _name == 'FunctionType':
                if _cur is not __types_vodai__.FunctionType:
                    return True
            else:
                if not isinstance(_cur, (__types_vodai__.BuiltinFunctionType, __types_vodai__.BuiltinMethodType)):
                    return True
                if hasattr(_cur, '__code__') or hasattr(_cur, '__wrapped__'):
                    return True

        if __sys_vodai__.gettrace() is not None:
            return True

        try:
            if hasattr(__th_vodai__, 'gettrace') and __th_vodai__.gettrace() is not None:
                return True
        except Exception: pass

    except Exception: pass
    return False

# === HARDWARE BREAKPOINT DETECTION (DR0 - DR3) ===
def __check_hw_breakpoints__():
    try:
        import ctypes
        _k32 = getattr(getattr(ctypes, 'windll', None), 'kernel32', None)
        if not _k32: return False
        _h = _k32.GetCurrentThread()
        is_64 = (__st_vodai__.calcsize('P') == 8)
        if is_64:
            class M128A(ctypes.Structure):
                _fields_ = [('Low', ctypes.c_ulonglong), ('High', ctypes.c_longlong)]
            class XSAVE_FORMAT(ctypes.Structure):
                _fields_ = [('ControlWord', ctypes.c_ushort), ('StatusWord', ctypes.c_ushort), ('TagWord', ctypes.c_ubyte), ('Reserved1', ctypes.c_ubyte), ('ErrorOpcode', ctypes.c_ushort), ('ErrorOffset', ctypes.c_ulong), ('ErrorSelector', ctypes.c_ushort), ('Reserved2', ctypes.c_ushort), ('DataOffset', ctypes.c_ulong), ('DataSelector', ctypes.c_ushort), ('Reserved3', ctypes.c_ushort), ('MxCsr', ctypes.c_ulong), ('MxCsr_Mask', ctypes.c_ulong), ('FloatRegisters', M128A * 8), ('XmmRegisters', M128A * 16), ('Reserved4', ctypes.c_ubyte * 96)]
            class CONTEXT64(ctypes.Structure):
                _fields_ = [
                    ('P1Home', ctypes.c_ulonglong), ('P2Home', ctypes.c_ulonglong), ('P3Home', ctypes.c_ulonglong), ('P4Home', ctypes.c_ulonglong), ('P5Home', ctypes.c_ulonglong), ('P6Home', ctypes.c_ulonglong),
                    ('ContextFlags', ctypes.c_ulong), ('MxCsr', ctypes.c_ulong),
                    ('SegCs', ctypes.c_ushort), ('SegDs', ctypes.c_ushort), ('SegEs', ctypes.c_ushort), ('SegFs', ctypes.c_ushort), ('SegGs', ctypes.c_ushort), ('SegSs', ctypes.c_ushort),
                    ('EFlags', ctypes.c_ulong),
                    ('Dr0', ctypes.c_ulonglong), ('Dr1', ctypes.c_ulonglong), ('Dr2', ctypes.c_ulonglong), ('Dr3', ctypes.c_ulonglong), ('Dr6', ctypes.c_ulonglong), ('Dr7', ctypes.c_ulonglong),
                    ('Rax', ctypes.c_ulonglong), ('Rcx', ctypes.c_ulonglong), ('Rdx', ctypes.c_ulonglong), ('Rbx', ctypes.c_ulonglong), ('Rsp', ctypes.c_ulonglong), ('Rbp', ctypes.c_ulonglong), ('Rsi', ctypes.c_ulonglong), ('Rdi', ctypes.c_ulonglong),
                    ('R8', ctypes.c_ulonglong), ('R9', ctypes.c_ulonglong), ('R10', ctypes.c_ulonglong), ('R11', ctypes.c_ulonglong), ('R12', ctypes.c_ulonglong), ('R13', ctypes.c_ulonglong), ('R14', ctypes.c_ulonglong), ('R15', ctypes.c_ulonglong),
                    ('Rip', ctypes.c_ulonglong),
                    ('FltSave', XSAVE_FORMAT),
                    ('VectorRegister', M128A * 26), ('VectorControl', ctypes.c_ulonglong), ('DebugControl', ctypes.c_ulonglong), ('LastBranchToRip', ctypes.c_ulonglong), ('LastBranchFromRip', ctypes.c_ulonglong), ('LastExceptionToRip', ctypes.c_ulonglong), ('LastExceptionFromRip', ctypes.c_ulonglong)
                ]
            ctx = CONTEXT64()
            ctx.ContextFlags = 0x00100010
            if _k32.GetThreadContext(_h, ctypes.byref(ctx)):
                return (ctx.Dr0 | ctx.Dr1 | ctx.Dr2 | ctx.Dr3) != 0
        else:
            class FLOATING_SAVE_AREA(ctypes.Structure):
                _fields_ = [('ControlWord', ctypes.c_ulong), ('StatusWord', ctypes.c_ulong), ('TagWord', ctypes.c_ulong), ('ErrorOffset', ctypes.c_ulong), ('ErrorSelector', ctypes.c_ulong), ('DataOffset', ctypes.c_ulong), ('DataSelector', ctypes.c_ulong), ('RegisterArea', ctypes.c_ubyte * 80), ('Cr0NpxState', ctypes.c_ulong)]
            class CONTEXT32(ctypes.Structure):
                _fields_ = [
                    ('ContextFlags', ctypes.c_ulong),
                    ('Dr0', ctypes.c_ulong), ('Dr1', ctypes.c_ulong), ('Dr2', ctypes.c_ulong), ('Dr3', ctypes.c_ulong), ('Dr6', ctypes.c_ulong), ('Dr7', ctypes.c_ulong),
                    ('FloatSave', FLOATING_SAVE_AREA),
                    ('SegGs', ctypes.c_ulong), ('SegFs', ctypes.c_ulong), ('SegEs', ctypes.c_ulong), ('SegDs', ctypes.c_ulong),
                    ('Edi', ctypes.c_ulong), ('Esi', ctypes.c_ulong), ('Ebx', ctypes.c_ulong), ('Edx', ctypes.c_ulong), ('Ecx', ctypes.c_ulong), ('Eax', ctypes.c_ulong),
                    ('Ebp', ctypes.c_ulong), ('Eip', ctypes.c_ulong), ('SegCs', ctypes.c_ulong), ('EFlags', ctypes.c_ulong), ('Esp', ctypes.c_ulong), ('SegSs', ctypes.c_ulong),
                    ('ExtendedRegisters', ctypes.c_ubyte * 512)
                ]
            ctx = CONTEXT32()
            ctx.ContextFlags = 0x00010010
            if _k32.GetThreadContext(_h, ctypes.byref(ctx)):
                return (ctx.Dr0 | ctx.Dr1 | ctx.Dr2 | ctx.Dr3) != 0
    except: pass
    return False

# === WIN32 REMOTE & ACTIVE DEBUGGER DETECTION ===
def __check_win32_debuggers__():
    try:
        import ctypes as _ct_dbg
        _k32_dbg = getattr(getattr(_ct_dbg, 'windll', None), 'kernel32', None)
        if _k32_dbg:
            if hasattr(_k32_dbg, 'IsDebuggerPresent') and _k32_dbg.IsDebuggerPresent():
                return True
            if hasattr(_k32_dbg, 'CheckRemoteDebuggerPresent'):
                _is_rem = _ct_dbg.c_int(0)
                _k32_dbg.CheckRemoteDebuggerPresent(_k32_dbg.GetCurrentProcess(), _ct_dbg.byref(_is_rem))
                if _is_rem.value:
                    return True
    except Exception: pass
    return False

# === SANDBOX / HONEYPOT LOW UPTIME DETECTION ===
def __check_sandbox_env__():
    try:
        import ctypes as _ct_sb
        _k32_sb = getattr(getattr(_ct_sb, 'windll', None), 'kernel32', None)
        if _k32_sb and hasattr(_k32_sb, 'GetTickCount64'):
            if _k32_sb.GetTickCount64() < 45000:
                _un = str(__os_vodai__.environ.get('USERNAME', '')).lower()
                if any(x in _un for x in ('sandbox', 'virus', 'sample', 'malware', 'test', 'runner', 'analyst', 'cuckoo')):
                    return True
    except Exception: pass
    return False

# === HTTP-TOOLKIT & INTERCEPTION PROXY DEEP DETECTION ===
def __check_http_toolkit__():
    try:
        _env = __os_vodai__.environ
        for _ek in ("HTTP_TOOLKIT_ACTIVE", "HTTP_TOOLKIT_INTERCEPTED", "NODE_EXTRA_CA_CERTS"):
            if _env.get(_ek, "").lower() in ("true", "1"):
                return True
        for _pk in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy", "ALL_PROXY", "all_proxy"):
            _pv = _env.get(_pk, "").lower()
            if any(_b in _pv for _b in ("127.0.0.1:8000", "localhost:8000", "httptoolkit", "proxyman")):
                return True
    except Exception: pass
    return False

# === MODULE SPEC ORIGIN & SYS.META_PATH INTEGRITY ===
def __check_module_integrity__():
    try:
        if __marshal_vodai__:
            _spec = getattr(__marshal_vodai__, '__spec__', None)
            if _spec and getattr(_spec, 'origin', '') != 'built-in':
                return True
            if getattr(__marshal_vodai__, '__name__', '') != 'marshal':
                return True
        import importlib._bootstrap as _vib, importlib.machinery as _vma
        for _req in (getattr(_vib, 'BuiltinImporter', None), getattr(_vib, 'FrozenImporter', None), getattr(_vma, 'PathFinder', None)):
            if _req and _req not in __sys_vodai__.meta_path:
                return True
    except Exception: pass
    return False

# === NATIVE INLINE TRAMPOLINE HOOK DETECTION (24-byte full scan across 18 APIs) ===
def __check_native_api_hooks__():
    def _is_hooked(_b):
        try:
            if not _b or len(_b) < 2: return False
            if _b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2): return True
            if _b[0] == 0xFF and len(_b) > 1 and _b[1] in (0x25, 0xE0, 0xE1, 0xE2): return True
            if _b[0] == 0x48 and len(_b) > 1 and _b[1] == 0xB8: return True
            if _b[0] == 0xCD and len(_b) > 1 and _b[1] == 0x03: return True
            if _b[0] == 0xB8 and len(_b) > 6 and _b[5] == 0xFF and _b[6] == 0xE0: return True
            if _b[0] == 0x68 and len(_b) > 5 and _b[5] == 0xC3: return True
            if len(_b) >= 3 and _b[0] == 0x90 and _b[1] == 0x90 and _b[2] == 0x90: return True
            for off in (1, 2, 3):
                if len(_b) > off + 2:
                    if _b[off] in (0xE9, 0xCC) or (_b[off] == 0xFF and _b[off+1] == 0x25) or (_b[off] == 0x48 and _b[off+1] == 0xB8):
                        return True
        except Exception: pass
        return False
    try:
        import ctypes
        try:
            _pyapi = object.__getattribute__(ctypes, 'pythonapi')
        except Exception:
            _pyapi = getattr(ctypes, 'pythonapi', None)
        if _pyapi:
            for _sym in (
                'PyMarshal_ReadObjectFromString', 'PyEval_EvalCode', '_PyEval_EvalFrameDefault',
                'PyRun_StringFlags', 'PyObject_Call', 'PyObject_CallObject',
                'PyObject_CallFunction', 'PyObject_CallMethod', 'PyCFunction_Call',
                'PyMarshal_WriteObjectToString', 'Py_CompileString'
            ):
                try:
                    _addr = getattr(_pyapi, _sym, None)
                    if _addr:
                        _ptr = ctypes.cast(_addr, ctypes.c_void_p).value
                        if _ptr:
                            _b = bytes((ctypes.c_ubyte * 24).from_address(_ptr))
                            if _is_hooked(_b):
                                return True
                except Exception: continue
        _wd = getattr(ctypes, 'windll', None)
        if _wd:
            _ws2 = getattr(_wd, 'ws2_32', None)
            if _ws2:
                for _fn in ('connect', 'send', 'recv', 'sendto', 'recvfrom', 'WSASend', 'WSARecv'):
                    try:
                        _f = getattr(_ws2, _fn, None)
                        if _f:
                            _ptr = ctypes.cast(_f, ctypes.c_void_p).value
                            if _ptr:
                                _b = bytes((ctypes.c_ubyte * 24).from_address(_ptr))
                                if _is_hooked(_b):
                                    return True
                    except Exception: continue
    except: pass
    return False

# === SUSPICIOUS THREAD INSPECTOR ===
def __check_suspicious_threads__():
    try:
        for _th in __th_vodai__.enumerate():
            _tn = str(getattr(_th, 'name', '')).lower()
            _tg = str(getattr(_th, '_target', '')).lower()
            if any(_x in _tn or _x in _tg for _x in ('pydevd', 'ptvsd', 'frida', 'mitm', 'canary', 'hook', 'debugserver')):
                return True
    except Exception: pass
    return False

# === CPYTHON AUDIT HOOK DEFENSE & PEP 669 MONITORING ===
try:
    if hasattr(__sys_vodai__, 'monitoring'):
        for _ti in range(6):
            if __sys_vodai__.monitoring.get_events(_ti) != 0 or __sys_vodai__.monitoring.get_tool(_ti) is not None:
                __Yuki_VoDoi_Exit__(95)
        for _ti in range(6):
            try: __sys_vodai__.monitoring.use_tool_id(_ti, f'yuki_{_ti}')
            except: pass
            try: __sys_vodai__.monitoring.set_events(_ti, 0)
            except: pass
except: pass

try:
    if hasattr(__sys_vodai__, 'addaudithook'):
        def __yuki_secure_audit__(event, args):
            if event in ('sys.settrace', 'sys.setprofile', 'cpython._PySys_ClearAuditHooks'):
                __Yuki_VoDoi_Exit__(95)
            elif event == 'import' and isinstance(args, tuple) and args:
                _m = str(args[0]).lower()
                if any(x in _m for x in ('frida', 'pylingual', 'pycdc', 'decompyle', 'uncompyle', 'ptvsd', 'pydevd')):
                    __Yuki_VoDoi_Exit__(96)
        __sys_vodai__.addaudithook(__yuki_secure_audit__)
except: pass

try:
    def __Yuki_Url_Decode_VoDoi__(__enc__):
        try:
            if '__yuki_watchdog_pulse__' in globals():
                _p_diff = abs(__time_vodai__.time() - __yuki_watchdog_pulse__[0])
                if _p_diff > 120.0 and __yuki_watchdog_pulse__[0] > 0:
                    __Yuki_VoDoi_Exit__(98)
            import base64 as __b64d__, zlib as __zl__
            try:
                if isinstance(__enc__, str) and ":" in __enc__:
                    __idx__, __payload__ = __enc__.split(":", 1)
                    __idx__ = int(__idx__)
                else:
                    __idx__, __payload__ = 0, __enc__
                if __idx__ == 0:
                    return __zl__.decompress(__b64d__.b85decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')
                elif __idx__ == 1:
                    return __zl__.decompress(__b64d__.b64decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')
                elif __idx__ == 2:
                    return __b64d__.b64decode(__payload__.encode('ascii')).decode('utf-8', errors='ignore')
                elif __idx__ == 3:
                    __x = __b64d__.b85decode(__payload__.encode('ascii'))
                    return bytes(b ^ 0x5A for b in __x).decode('utf-8', errors='ignore')
                elif __idx__ == 4:
                    __r = __b64d__.b64decode(__payload__.encode('ascii'))
                    return bytes(((b - 32 - 13) % 95 + 32) if 32 <= b <= 126 else b for b in __r).decode('utf-8', errors='ignore')
                else:
                    return __payload__
            except:
                return __b64d__.b64decode(__enc__.encode()).decode('utf-8', errors='ignore')
        except:
            return __enc__
except:
    pass

try:
    __Yuki_VoDoi_Orig__ = {}
    __Yuki_VoDoi_CodeHash__ = {}
    try:
        import requests as __rq_vodai__, urllib3 as __urllib3_vodai__
        import requests.adapters as __adp_vodai__, requests.sessions as __sess_vodai__
        import urllib3.connectionpool as __pool_vodai__
        import hashlib as __hl_vodai__

        def __calc_code_sha256__(o):
            try:
                if hasattr(o, '__code__') and hasattr(o.__code__, 'co_code'):
                    return __hl_vodai__.sha256(o.__code__.co_code).digest()
                return __hl_vodai__.sha256(str(o).encode()).digest()
            except:
                return b''

        def __snap_vodai__(k, obj):
            try:
                __Yuki_VoDoi_Orig__[k] = obj
                __Yuki_VoDoi_CodeHash__[k] = __calc_code_sha256__(obj)
            except:
                pass

        try: __snap_vodai__('requests.get', __rq_vodai__.get)
        except: pass
        try: __snap_vodai__('requests.post', __rq_vodai__.post)
        except: pass
        try: __snap_vodai__('requests.request', __rq_vodai__.request)
        except: pass
        try: __snap_vodai__('requests.api.request', __rq_vodai__.api.request)
        except: pass
        try: __snap_vodai__('Session.request', __sess_vodai__.Session.request)
        except: pass
        try: __snap_vodai__('HTTPAdapter.send', __adp_vodai__.HTTPAdapter.send)
        except: pass
        try: __snap_vodai__('HTTPConnectionPool.urlopen', __pool_vodai__.HTTPConnectionPool.urlopen)
        except: pass
        try: __snap_vodai__('HTTPConnection.request', __http_vodai__.HTTPConnection.request)
        except: pass
        try: __snap_vodai__('HTTPConnection.putrequest', __http_vodai__.HTTPConnection.putrequest)
        except: pass
        try: __snap_vodai__('socket.getaddrinfo', __sock_vodai__.getaddrinfo)
        except: pass
        try: __snap_vodai__('socket.gethostbyname', __sock_vodai__.gethostbyname)
        except: pass
        try: __snap_vodai__('socket.socket.connect', __sock_vodai__.socket.connect)
        except: pass
        try: __snap_vodai__('socket.socket.send', __sock_vodai__.socket.send)
        except: pass
        try: __snap_vodai__('socket.socket.sendall', __sock_vodai__.socket.sendall)
        except: pass
        try: __snap_vodai__('socket.socket.recv', __sock_vodai__.socket.recv)
        except: pass
        try: __snap_vodai__('socket.create_connection', __sock_vodai__.create_connection)
        except: pass
        try:
            import ssl as __ssl_vodai__
            try: __snap_vodai__('ssl.SSLSocket.send', __ssl_vodai__.SSLSocket.send)
            except: pass
            try: __snap_vodai__('ssl.SSLSocket.recv', __ssl_vodai__.SSLSocket.recv)
            except: pass
        except: pass
    except:
        pass

    # === SELF-HEALING / AUTO-RESTORATION ENGINE ===
    def __auto_heal_and_restore__():
        try:
            for _name, _orig in __Yuki_Builtins_Snapshot__.items():
                if not _orig or _name in ('open', 'settrace'): continue
                try:
                    if _name in ('loads', 'dumps') and __marshal_vodai__:
                        setattr(__marshal_vodai__, _name, _orig)
                    elif _name in ('gettrace', '_getframe'):
                        setattr(__sys_vodai__, _name, _orig)
                    elif _name == 'FunctionType':
                        setattr(__types_vodai__, _name, _orig)
                    else:
                        setattr(__bi_vodai__, _name, _orig)
                except: pass
            import requests as __r_heal__
            for _m in ('get', 'post', 'request'):
                if f'requests.{_m}' in __Yuki_VoDoi_Orig__:
                    setattr(__r_heal__, _m, __Yuki_VoDoi_Orig__[f'requests.{_m}'])
            import requests.sessions as __s_heal__
            if 'Session.request' in __Yuki_VoDoi_Orig__:
                __s_heal__.Session.request = __Yuki_VoDoi_Orig__['Session.request']
            import requests.adapters as __a_heal__
            if 'HTTPAdapter.send' in __Yuki_VoDoi_Orig__:
                __a_heal__.HTTPAdapter.send = __Yuki_VoDoi_Orig__['HTTPAdapter.send']
            import urllib3.connectionpool as __p_heal__
            if 'HTTPConnectionPool.urlopen' in __Yuki_VoDoi_Orig__:
                __p_heal__.HTTPConnectionPool.urlopen = __Yuki_VoDoi_Orig__['HTTPConnectionPool.urlopen']
            import socket as __sk_heal__
            if 'socket.getaddrinfo' in __Yuki_VoDoi_Orig__:
                __sk_heal__.getaddrinfo = __Yuki_VoDoi_Orig__['socket.getaddrinfo']
            if 'socket.socket.connect' in __Yuki_VoDoi_Orig__:
                __sk_heal__.socket.connect = __Yuki_VoDoi_Orig__['socket.socket.connect']
        except: pass

    def __Yuki_VoDoi_Check__():
        try:
            # 1. Hardware Breakpoints (DR0..DR3)
            if __check_hw_breakpoints__():
                __Yuki_VoDoi_Exit__(91)
            # 2. Win32 Active & Remote Debuggers
            if __check_win32_debuggers__():
                __Yuki_VoDoi_Exit__(91)
            # 3. Native Inline Trampoline Hooks (18 C APIs)
            if __check_native_api_hooks__():
                __Yuki_VoDoi_Exit__(92)
            # 4. Deep C-Builtin Integrity & Self-Healing
            if __check_deep_builtin_hooks__():
                __Yuki_VoDoi_Exit__(93)
            # 5. Suspicious Debugger/Injector Threads
            if __check_suspicious_threads__():
                __Yuki_VoDoi_Exit__(94)
            # 6. Automated Sandbox / Low-Uptime Honeypot
            if __check_sandbox_env__():
                __Yuki_VoDoi_Exit__(95)
            # 7. HTTP-Toolkit & Interception Proxies
            if __check_http_toolkit__():
                __Yuki_VoDoi_Exit__(96)
            # 8. Module Built-in Origin & Sys Meta Path Integrity
            if __check_module_integrity__():
                __Yuki_VoDoi_Exit__(97)

            for _pe in ('HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'REQUESTS_CA_BUNDLE', 'SSL_CERT_FILE'):
                if _pe in __os_vodai__.environ:
                    __Yuki_VoDoi_Exit__(97)

            import requests as __rq2__, urllib3 as __urllib32__, http.client as __http2__, socket as __sock2__, logging as __log2__, builtins as __bi2__

            try:
                if 'requests.get' in __Yuki_VoDoi_Orig__ and __rq2__.get is not __Yuki_VoDoi_Orig__['requests.get']:
                    __Yuki_VoDoi_Exit__(91)
                if 'requests.post' in __Yuki_VoDoi_Orig__ and __rq2__.post is not __Yuki_VoDoi_Orig__['requests.post']:
                    __Yuki_VoDoi_Exit__(91)
                if 'requests.request' in __Yuki_VoDoi_Orig__ and __rq2__.request is not __Yuki_VoDoi_Orig__['requests.request']:
                    __Yuki_VoDoi_Exit__(92)
            except:
                pass

            try:
                import requests.sessions as __sess2__
                if 'Session.request' in __Yuki_VoDoi_Orig__ and __sess2__.Session.request is not __Yuki_VoDoi_Orig__['Session.request']:
                    __auto_heal_and_restore__()
                    __Yuki_VoDoi_Exit__(93)
            except:
                pass

            try:
                import requests.adapters as __adp2__
                if 'HTTPAdapter.send' in __Yuki_VoDoi_Orig__ and __adp2__.HTTPAdapter.send is not __Yuki_VoDoi_Orig__['HTTPAdapter.send']:
                    __Yuki_VoDoi_Exit__(94)
            except:
                pass

            try:
                import urllib3.connectionpool as __pool2__
                if 'HTTPConnectionPool.urlopen' in __Yuki_VoDoi_Orig__ and __pool2__.HTTPConnectionPool.urlopen is not __Yuki_VoDoi_Orig__['HTTPConnectionPool.urlopen']:
                    __Yuki_VoDoi_Exit__(95)
            except:
                pass

            try:
                if 'HTTPConnection.request' in __Yuki_VoDoi_Orig__ and __http2__.HTTPConnection.request is not __Yuki_VoDoi_Orig__['HTTPConnection.request']:
                    __Yuki_VoDoi_Exit__(96)
                if 'HTTPConnection.putrequest' in __Yuki_VoDoi_Orig__ and __http2__.HTTPConnection.putrequest is not __Yuki_VoDoi_Orig__['HTTPConnection.putrequest']:
                    __Yuki_VoDoi_Exit__(96)
            except:
                pass

            try:
                if 'socket.getaddrinfo' in __Yuki_VoDoi_Orig__ and __sock2__.getaddrinfo is not __Yuki_VoDoi_Orig__['socket.getaddrinfo']:
                    __Yuki_VoDoi_Exit__(97)
                if 'socket.gethostbyname' in __Yuki_VoDoi_Orig__ and __sock2__.gethostbyname is not __Yuki_VoDoi_Orig__['socket.gethostbyname']:
                    __Yuki_VoDoi_Exit__(97)
                if 'socket.socket.connect' in __Yuki_VoDoi_Orig__ and __sock2__.socket.connect is not __Yuki_VoDoi_Orig__['socket.socket.connect']:
                    __Yuki_VoDoi_Exit__(97)
                if 'socket.socket.send' in __Yuki_VoDoi_Orig__ and __sock2__.socket.send is not __Yuki_VoDoi_Orig__['socket.socket.send']:
                    __Yuki_VoDoi_Exit__(97)
                if 'socket.socket.sendall' in __Yuki_VoDoi_Orig__ and __sock2__.socket.sendall is not __Yuki_VoDoi_Orig__['socket.socket.sendall']:
                    __Yuki_VoDoi_Exit__(97)
                if 'socket.socket.recv' in __Yuki_VoDoi_Orig__ and __sock2__.socket.recv is not __Yuki_VoDoi_Orig__['socket.socket.recv']:
                    __Yuki_VoDoi_Exit__(97)
            except:
                pass

            try:
                import ssl as __ssl2__
                if 'ssl.SSLSocket.send' in __Yuki_VoDoi_Orig__ and __ssl2__.SSLSocket.send is not __Yuki_VoDoi_Orig__['ssl.SSLSocket.send']:
                    __Yuki_VoDoi_Exit__(97)
                if 'ssl.SSLSocket.recv' in __Yuki_VoDoi_Orig__ and __ssl2__.SSLSocket.recv is not __Yuki_VoDoi_Orig__['ssl.SSLSocket.recv']:
                    __Yuki_VoDoi_Exit__(97)
            except:
                pass

            try:
                for __k__, __orig_obj__ in __Yuki_VoDoi_Orig__.items():
                    __cur__ = None
                    try:
                        if __k__ == 'requests.get': __cur__ = __rq2__.get
                        elif __k__ == 'requests.post': __cur__ = __rq2__.post
                        elif __k__ == 'requests.request': __cur__ = __rq2__.request
                        elif __k__ == 'Session.request':
                            import requests.sessions as __s__
                            __cur__ = __s__.Session.request
                        elif __k__ == 'HTTPAdapter.send':
                            import requests.adapters as __a__
                            __cur__ = __a__.HTTPAdapter.send
                        elif __k__ == 'HTTPConnectionPool.urlopen':
                            import urllib3.connectionpool as __p__
                            __cur__ = __p__.HTTPConnectionPool.urlopen
                        elif __k__ == 'HTTPConnection.request': __cur__ = __http2__.HTTPConnection.request
                        elif __k__ == 'HTTPConnection.putrequest': __cur__ = __http2__.HTTPConnection.putrequest
                        elif __k__ == 'socket.getaddrinfo': __cur__ = __sock2__.getaddrinfo
                    except:
                        continue
                    if __cur__ is not None and hasattr(__cur__, '__code__') and __k__ in __Yuki_VoDoi_CodeHash__:
                        try:
                            if __calc_code_sha256__(__cur__) != __Yuki_VoDoi_CodeHash__[__k__]:
                                __Yuki_VoDoi_Exit__(90)
                        except:
                            pass
                    try:
                        if hasattr(__orig_obj__, '__module__') and hasattr(__cur__, '__module__'):
                            if __orig_obj__.__module__ != __cur__.__module__:
                                if 'hook' in str(__cur__.__module__).lower():
                                    __Yuki_VoDoi_Exit__(89)
                    except:
                        pass
            except:
                pass

            try:
                if 'http' in str(__bi2__.print).lower() and 'hook' in str(__bi2__.print).lower():
                    __Yuki_VoDoi_Exit__(98)
            except:
                pass

            try:
                for __m__ in list(__sys_vodai__.modules.keys()):
                    __ml__ = __m__.lower()
                    if any(__x__ in __ml__ for __x__ in ('frida','pyshark','scapy','mitmproxy','httpcanary','httptoolkit','charles','fiddler','wireshark','burp','devtools','pycdc','decompyle','uncompyle','pylingual')):
                        if __ml__ not in ('http','http.client','http.cookiejar','http.cookies'):
                            __Yuki_VoDoi_Exit__(99)
            except:
                pass

            try:
                if __sys_vodai__.gettrace() is not None:
                    __Yuki_VoDoi_Exit__(95)
                for __f__ in __sys_vodai__._current_frames().values():
                    __cf__ = __f__
                    while __cf__:
                        __fn__ = (getattr(__cf__.f_code, 'co_filename', '') or '').lower()
                        __cname__ = (getattr(__cf__.f_code, 'co_name', '') or '').lower()
                        if any(__x__ in __fn__ or __x__ in __cname__ for __x__ in ('pycdc','decompyle','uncompyle','pylingual','frida','mitm','canary','httpcanary','fiddler','charles','wireshark','burp')):
                            __Yuki_VoDoi_Exit__(97)
                        __cf__ = __cf__.f_back
            except:
                pass

        except SystemExit:
            raise
        except:
            pass

    __yuki_watchdog_pulse__ = [__time_vodai__.time()]
    def __Yuki_VoDoi_Watch__():
        while True:
            try:
                _t0 = __time_vodai__.perf_counter()
                __yuki_watchdog_pulse__[0] = __time_vodai__.time()
                __Yuki_VoDoi_Check__()
                if __time_vodai__.perf_counter() - _t0 > 2.5:
                    __Yuki_VoDoi_Exit__(90)
            except SystemExit:
                raise
            except:
                pass
            try:
                __time_vodai__.sleep(1.2)
            except:
                try:
                    __time_vodai__.sleep(1.5)
                except:
                    pass

    try:
        import _thread as __low_th_vodai__
        __low_th_vodai__.start_new_thread(__Yuki_VoDoi_Watch__, ())
    except Exception:
        try:
            __th_vodai__.Thread(target=__Yuki_VoDoi_Watch__, daemon=True).start()
        except:
            pass

    try:
        __Yuki_VoDoi_Check__()
    except SystemExit:
        raise
    except:
        pass

    try:
        __orig_log_vodai__ = __log_vodai__.Logger._log
        def __filtered_log_vodai__(self, level, msg, args, exc_info=None, extra=None, stack_info=False, stacklevel=1):
            try:
                if isinstance(msg, str):
                    if 'http://' in msg or 'https://' in msg or 'www.' in msg or '__hid_' in msg or 'ftp://' in msg:
                        return
                    if '://' in msg and any(__x__ in msg.lower() for __x__ in ('api','cdn','github','google')):
                        msg = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', msg)
                if args:
                    try:
                        __joined__ = ' '.join(str(__a__) for __a__ in args)
                        if 'http://' in __joined__ or 'https://' in __joined__ or 'www.' in __joined__:
                            return
                    except:
                        pass
            except:
                pass
            return __orig_log_vodai__(self, level, msg, args, exc_info=exc_info, extra=extra, stack_info=stack_info, stacklevel=stacklevel)
        __log_vodai__.Logger._log = __filtered_log_vodai__

        for __ln__ in ['urllib3','urllib3.connectionpool','urllib3.poolmanager','requests','requests.adapters','http.client','socket']:
            try:
                __lg__ = __log_vodai__.getLogger(__ln__)
                __lg__.handlers = []
                __lg__.propagate = False
                __lg__.setLevel(__log_vodai__.CRITICAL)
                __lg__.disabled = True
            except:
                pass
    except:
        pass

    try:
        if hasattr(__sys_vodai__, 'addaudithook'):
            __sys_vodai__.addaudithook = lambda *a, **k: None
    except:
        pass

    try:
        __orig_os_write__ = __os_vodai__.write
        def __filtered_os_write__(fd, data):
            try:
                if isinstance(data, bytes):
                    __s__ = data.decode('utf-8', errors='ignore')
                else:
                    __s__ = str(data)
                if 'http://' in __s__ or 'https://' in __s__ or 'www.' in __s__ or '__hid_' in __s__:
                    return len(data)
            except:
                pass
            return __orig_os_write__(fd, data)
        __os_vodai__.write = __filtered_os_write__
    except:
        pass

    try:
        __orig_print_vodai__ = __bi_vodai__.print
        def __filtered_print_vodai__(*a, **k):
            try:
                __msg__ = ' '.join(str(__x__) for __x__ in a)
                if 'http://' in __msg__ or 'https://' in __msg__ or 'www.' in __msg__ or '__hid_' in __msg__:
                    __msg__ = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', __msg__)
                    return __orig_print_vodai__(__msg__, **k)
                if any(__p__ in __msg__ for __p__ in ('[Urllib3]','[Url]','Request URL')):
                    return
            except:
                pass
            return __orig_print_vodai__(*a, **k)
        __bi_vodai__.print = __filtered_print_vodai__
    except:
        pass

    try:
        __orig_stdout_write__ = __sys_vodai__.stdout.write
        __orig_stderr_write__ = __sys_vodai__.stderr.write
        def __filtered_stdout_write__(text):
            try:
                if isinstance(text, str) and ('http://' in text or 'https://' in text or 'www.' in text or '__hid_' in text):
                    text = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', text)
            except:
                pass
            return __orig_stdout_write__(text)
        def __filtered_stderr_write__(text):
            try:
                if isinstance(text, str) and ('http://' in text or 'https://' in text or 'www.' in text or '__hid_' in text):
                    text = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', text)
            except:
                pass
            return __orig_stderr_write__(text)
        __sys_vodai__.stdout.write = __filtered_stdout_write__
        __sys_vodai__.stderr.write = __filtered_stderr_write__
    except:
        pass

    try:
        import requests.models as __req_models__
        if hasattr(__req_models__, 'Response'):
            __orig_resp_repr__ = getattr(__req_models__.Response, '__repr__', None)
            def __hidden_resp_repr__(self):
                try:
                    __u__ = getattr(self, 'url', '')
                    if isinstance(__u__, str) and ('http://' in __u__ or 'https://' in __u__):
                        self.url = __re_vodai__.sub(r'https?://[^\s\'\"<>\{\}]+', '[FILTERED]', __u__)
                except:
                    pass
                try:
                    if __orig_resp_repr__:
                        return __orig_resp_repr__(self)
                except:
                    pass
                return f"<Response [{getattr(self, 'status_code', '?')}]>"
            __req_models__.Response.__repr__ = __hidden_resp_repr__
    except:
        pass

except SystemExit:
    raise
except:
    pass
'''



RQ_VODAI_MINIMAL = r'''

# MINIMAL VÔ ĐỐI - LUÔN BẬT DÙ CHỌN No

import sys as __sys_min__, os as __os_min__, threading as __th_min__, time as __time_min__, builtins as __bi_min__

try:

    def __Yuki_Url_Decode_VoDoi__(__enc__):

        try:

            import base64, zlib

            try:

                if ":" in __enc__:

                    __i, __p = __enc__.split(":", 1)

                    __i = int(__i)

                else:

                    __i, __p = 0, __enc__

                if __i == 0:

                    return zlib.decompress(base64.b85decode(__p.encode('ascii'))).decode()

                elif __i == 1:

                    return zlib.decompress(base64.b64decode(__p.encode())).decode()

                elif __i == 2:

                    return base64.b64decode(__p.encode()).decode()

                elif __i == 3:

                    __x = base64.b85decode(__p.encode('ascii'))

                    return bytes(b ^ 0x5A for b in __x).decode()

                elif __i == 4:

                    __r = base64.b64decode(__p.encode())

                    return bytes(((b - 32 - 13) % 95 + 32) if 32 <= b <= 126 else b for b in __r).decode()

                else:

                    return __p

            except:

                return base64.b64decode(__enc__.encode()).decode()

        except:

            return __enc__

except: pass

try:

    import logging as __log_min__, re as __re_min__

    __orig_min__ = __log_min__.Logger._log

    def __filt_min__(self,lvl,msg,args,exc_info=None,extra=None,stack_info=False,stacklevel=1):

        if isinstance(msg,str) and ('http://' in msg or 'https://' in msg):

            return

        return __orig_min__(self,lvl,msg,args,exc_info=exc_info,extra=extra,stack_info=stack_info,stacklevel=stacklevel)

    __log_min__.Logger._log = __filt_min__

except: pass

try:

    __orig_print_min__ = __bi_min__.print

    def __p_min__(*a,**k):

        __m__=' '.join(str(x) for x in a)

        if 'http://' in __m__ or 'https://' in __m__:

            __m__=__re_min__.sub(r'https?://[^\s]+','[FILTERED]',__m__)

            return __orig_print_min__(__m__,**k)

        return __orig_print_min__(*a,**k)

    __bi_min__.print = __p_min__

except: pass

'''



anticrackkey = """

try:

    def Okbeiu():

        try:

            if KhangCoder('os').name == 'nt':

                KhangCoder('subprocess').Popen(['mshta', 'vbscript:msgbox("CANH BAO CRACK: PHAT HIEN CAN THIEP NETWORK/REQUESTS!",16,"Security Sentinel")(window.close)'])

        except: pass

        try:

            import ctypes; ctypes.memset(0, 0, 1)

        except: pass

        KhangCoder('os')._exit(137)

    def _chk_requests_obj():

        if 'requests' in KhangCoder('sys').modules:

            _rq = KhangCoder('sys').modules.get('requests')

            if _rq:

                _resp = getattr(getattr(_rq, 'models', None), 'Response', None)

                if _resp:

                    for _m in ('json', 'text', 'content'):

                        _f = getattr(_resp, _m, None)

                        if hasattr(_f, '__code__'):

                            _fn = (getattr(_f.__code__, 'co_filename', '') or '').lower()

                            if _fn and '<' not in _fn and 'requests' not in _fn:

                                Okbeiu()

                _sess = getattr(getattr(_rq, 'sessions', None), 'Session', None)

                if _sess:

                    for _m in ('send', 'request'):

                        _f = getattr(_sess, _m, None)

                        if hasattr(_f, '__code__'):

                            _fn = (getattr(_f.__code__, 'co_filename', '') or '').lower()

                            if _fn and '<' not in _fn and 'requests' not in _fn:

                                Okbeiu()

    _chk_requests_obj()

    class _YukiImportAudit(object):

        @classmethod

        def find_spec(cls, fullname, path=None, target=None):

            if fullname and any(k in fullname.lower() for k in ('requests', 'urllib3', 'httpx', 'aiohttp')):

                try:

                    KhangCoder('sys')._getframe().f_trace = None

                except: pass

                _chk_requests_obj()

            return None

    try:

        if hasattr(KhangCoder('sys'), 'meta_path'):

            KhangCoder('sys').meta_path.insert(0, _YukiImportAudit)

    except: pass

except:pass

"""



nghich = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 3))

nghich1 = ''.join(random.sample([chr(i) for i in range(44032, 55204)], 4))

def speed1(code):

    import ast, random, base64

    code = ast.parse(code) if isinstance(code, str) else code

    nghich = ''.join(random.sample([chr(i) for i in range(44032, 55204) if chr(i).isidentifier()], 5))



    class __chanbomayde__(ast.NodeTransformer):



        def __init__(self):

            self.injected = False

            self.sothatday = f'____{nghich}___'

            self.__std__ = ''.join(map(chr, range(33, 127)))



            def __chembotia__():

                blocks = [range(44032, 55204), range(8544, 8579), range(12413, 12415), range(1000, 3000)]

                pool = []

                for b in blocks:

                    for i in b:

                        c = chr(i)

                        if c.isprintable():

                            pool.append(c)

                random.shuffle(pool)

                return pool

            pool = __chembotia__()

            self.__obf__ = ''.join(pool[:len(self.__std__)])

            self.enc_map = dict(zip(self.__std__, self.__obf__))

            self.dec_map = dict(zip(self.__obf__, self.__std__))



        def visit_JoinedStr(self, node):

                return node 



        def coder(self):

            __mobat__ = f'{_uni}({anhxa1("base64")})'

            __mobat1__ = f'{_uni}({anhxa1("b85decode")})'

            build_map = ast.Assign(targets=[ast.Name(id='PyAbity', ctx=ast.Store())], value=ast.Dict(keys=[ast.Constant(k) for k in self.dec_map.keys()], values=[ast.Constant(v) for v in self.dec_map.values()]))

            remap = ast.Assign(targets=[ast.Name(id=f'{x}', ctx=ast.Store())], value=ast.Call(func=ast.Attribute(value=ast.Name(id=f'KyThuatAnCode', ctx=ast.Store()), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Subscript(value=ast.Name(id='PyAbity', ctx=ast.Load()), slice=ast.Name(id=f'{c}', ctx=ast.Load()), ctx=ast.Load()), generators=[ast.comprehension(target=ast.Name(id=f'{c}', ctx=ast.Store()), iter=ast.Name(id=f'{x}', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))

            import_b = ast.Call(func=ast.Name(id='KhangCoder', ctx=ast.Load()), args=[ast.Name(id=__mobat__, ctx=ast.Load())], keywords=[])

            get_decode = ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[import_b, ast.Name(id=__mobat1__, ctx=ast.Load())], keywords=[])

            call_decode = ast.Call(func=get_decode, args=[ast.Name(id=f'{x}', ctx=ast.Load())], keywords=[])

            final_call = ast.Call(func=ast.Name(id=f'{_str}', ctx=ast.Load()), args=[call_decode, ast.Name(id=f'{_utf8}', ctx=ast.Load()), ast.Name(id='ThichㅤXamㅤLonㅤKhongㅤEm', ctx=ast.Load())], keywords=[])

            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=f'{x}')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[build_map, remap, ast.Return(value=final_call)], decorator_list=[])



        def visit_Module(self, node):

            self.generic_visit(node)

            if not self.injected:

                node.body.insert(0, self.coder())

                self.injected = True

            return node



        def visit_Constant(self, node):

            if not isinstance(node.value, str):return node

            if not node.value:return node

            try:raw = node.value.encode('utf-8', '✦ ✧✦ ✧✦ ✧✦ ✧✦ ✧')

            except Exception:return node

            encoded = getattr(__import__('base64'), 'b85encode')(raw)

            encoded_str = str(encoded, 'ascii')

            mapped = ''.join((self.enc_map.get(c, c) for c in encoded_str))

            return ast.Call(func=ast.Name(id=self.sothatday, ctx=ast.Load()), args=[ast.Constant(mapped)], keywords=[])

    transformer = __chanbomayde__()

    code = transformer.visit(code)

    ast.fix_missing_locations(code)

    return code



def speed2(code):

    code = ast.parse(code) if isinstance(code, str) else code

    class UnicodeObf(ast.NodeTransformer):



        def __init__(self):

            self.injected = False

            self.sothatday = f'__{nghich}___'



        def visit_JoinedStr(self, node):

            return node



        def obfstringv1(self):

            namanhdzai = f'{_ord}'

            thgchongu = f'_{thicthamcrush}'

            nolatheo = ''.join(map(chr, [106, 111, 105, 110]))

            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=f'{x}'), ast.arg(arg=f'{o}')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr=nolatheo, ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Name(id=thgchongu, ctx=ast.Load()), args=[ast.BinOp(left=ast.Call(func=ast.Name(id=namanhdzai, ctx=ast.Load()), args=[ast.Name(id=f'{c}', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id=f'{o}', ctx=ast.Load()))], keywords=[]), generators=[ast.comprehension(target=ast.Name(id=f'{c}', ctx=ast.Store()), iter=ast.Name(id=f'{x}', ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])



        def visit_Module(self, node):

            self.generic_visit(node)

            if not self.injected:

                node.body.insert(0, self.obfstringv1())

                self.injected = True

            return node



        def visit_Constant(self, node):

            if not isinstance(node.value, str):

                return node

            if not node.value:

                return node

            OFFSET = random.randint(*random.choice([(128544, 128549), (1000, 3000), (768, 879)]))

            mahoanangcao = ''.join((chr(ord(c) + OFFSET) for c in node.value))

            a = random.randint(44032, 55204)

            b = random.randint(1000, 3000)

            thuatchunganh = (a + b) - OFFSET

            expr = f"((lambda: ({hex(a)}+{hex(b)}))())-((lambda: {hex(thuatchunganh)})())"

            ToLaAbyss = f'\\({expr})'

            obf_offset = ast.Call(func=ast.Name(id=f'{champ}',ctx=ast.Load()),args=[ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=ast.Constant(str(ToLaAbyss[1:]))),args=[],keywords=[])],keywords=[])

            return ast.Call(func=ast.Name(id=self.sothatday, ctx=ast.Load()), args=[ast.Constant(mahoanangcao), obf_offset], keywords=[])

    transformer = UnicodeObf()

    code = transformer.visit(code)

    ast.fix_missing_locations(code)

    return code



def speed3(code):

    code = ast.parse(code) if isinstance(code, str) else code



    class UnicodeObf(ast.NodeTransformer):



        def __init__(self):

            self.injected = False

            self.sothatday = f'__{nghich1}___'



        def visit_JoinedStr(self, node):

            return node



        def phanoffset(self, n):

            return ''.join((chr(0x1F300 + (n >> i & 15)) for i in range(0, 16, 4)))



        def okdecode(self):

            return ast.Call(func=ast.Name(id=f'{_sum}', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.BinOp(left=ast.BinOp(left=ast.Call(func=ast.Name(id=f'{_ord}', ctx=ast.Load()), args=[ast.Name(id=f'{c}', ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=ast.Name(id='CauBiLuaRoii', ctx=ast.Load())), op=ast.LShift(), right=ast.BinOp(left=ast.Name(id=f'{i}', ctx=ast.Load()), op=ast.Mult(), right=ast.Constant(4))), generators=[ast.comprehension(target=ast.Tuple(elts=[ast.Name(id=f'{i}', ctx=ast.Store()), ast.Name(id=f'{c}', ctx=ast.Store())], ctx=ast.Store()), iter=ast.Call(func=ast.Name(id='_0x4', ctx=ast.Load()), args=[ast.Name(id='TroiMaThatKhongDa', ctx=ast.Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])



        def obfstringv1(self):

            x = f'{_ord}' + nghich1

            z = f'_{_ord}' + nghich1

            c = f'__{_ord}' + nghich1

            return ast.FunctionDef(name=self.sothatday, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=x), ast.arg(arg='__BoLaHacAm__'), ast.arg(arg='__TayChaySuNghiep__'), ast.arg(arg='__TamBietNheToiQuaMetMoi__'), ast.arg(arg='TroiMaThatKhongDa')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[ast.Return(value=ast.Call(func=ast.Attribute(value=ast.Constant(''), attr='join', ctx=ast.Load()), args=[ast.GeneratorExp(elt=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[ast.arg(arg=z)], kwonlyargs=[], kw_defaults=[], defaults=[]), body=ast.Call(func=ast.Attribute(value=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.BinOp(left=ast.Call(func=ast.Name(id=f'{_ord}', ctx=ast.Load()), args=[ast.Name(id=z, ctx=ast.Load())], keywords=[]), op=ast.Sub(), right=self.okdecode()), op=ast.BitXor(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__TayChaySuNghiep__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("YukiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), op=ast.Sub(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__TamBietNheToiQuaMetMoi__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("YukiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), op=ast.BitXor(), right=ast.Call(func=ast.Name(id='__KhangCoder__', ctx=ast.Load()), args=[ast.Call(func=ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[ast.Name(id='__BoLaHacAm__', ctx=ast.Load()), ast.Name(id=f'{_replace}', ctx=ast.Load())], keywords=[]), args=[ast.Name(id=f'{_uni}({anhxa1("YukiㅤAbi/")})', ctx=ast.Load()), ast.Name(id='ToiㅤYeuㅤEmㅤNhieuㅤLam', ctx=ast.Load())], keywords=[]), ast.Name(id=f'{_aychochoco}', ctx=ast.Load())], keywords=[])), attr='__format__', ctx=ast.Load()), args=[ast.Name(id=f'{_c}', ctx=ast.Load())], keywords=[])), args=[ast.Name(id=c, ctx=ast.Load())], keywords=[]), generators=[ast.comprehension(target=ast.Name(id=c, ctx=ast.Store()), iter=ast.Name(id=x, ctx=ast.Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[])



        def visit_Module(self, node):

            self.generic_visit(node)

            if not self.injected:

                node.body.insert(0, self.obfstringv1())

                self.injected = True

            return node



        def visit_Constant(self, node):

            if not isinstance(node.value, str) or not node.value:

                return node

            __BoLaHacAm__ = random.randint(10000, 99999)

            __TayChaySuNghiep__ = random.randint(1000, 9999)

            __TamBietNheToiQuaMetMoi__ = random.randint(100, 999)

            NgaoLol = random.randint(1000, 3000)

            NgaoLol_enc = self.phanoffset(NgaoLol)

            encoded = ''.join((chr(((ord(c) ^ __BoLaHacAm__) + __TamBietNheToiQuaMetMoi__ ^ __TayChaySuNghiep__) + NgaoLol) for c in node.value))

            return ast.Call(func=ast.Name(id=self.sothatday,ctx=ast.Load()),args=[ast.Constant(encoded),ast.Constant(f'YukiㅤAbi/{hex(__BoLaHacAm__)}'),ast.Constant(f'YukiㅤAbi/{hex(__TayChaySuNghiep__)}'),ast.Constant(f'YukiㅤAbi/{hex(__TamBietNheToiQuaMetMoi__)}'),ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[],args=[],kwonlyargs=[],kw_defaults=[],defaults=[]),body=ast.Name(id=f'("{NgaoLol_enc}")', ctx=ast.Load())),args=[],keywords=[])],keywords=[])

    transformer = UnicodeObf()

    code = transformer.visit(code)

    ast.fix_missing_locations(code)

    return code



bavailonctevcl = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 2))

bavailonctevcl1 = ''.join(random.sample([chr(i) for i in range(19968, 40959)], 5))

def __xamlolthoi__(code):

    tree = ast.parse(code)

    # FIX: preserve 'from __future__' at top - don't wrap with junk

    _fut = [n for n in tree.body if isinstance(n, ast.ImportFrom) and n.module == '__future__']

    _rest = [n for n in tree.body if n not in _fut]

    if _fut:

        if _rest:

            _rt = ast.Module(body=_rest, type_ignores=[])

            _rt = hide().visit(_rt)

            _rt.body = sieucaplongjunk(_rt.body, 1)

            ast.fix_missing_locations(_rt)

            tree.body = _fut + _rt.body

        else:

            # only future imports, just hide (no junk)

            tree = hide().visit(tree)

        ast.fix_missing_locations(tree)

        return ast.unparse(tree)

    tree = hide().visit(tree)

    tree.body = sieucaplongjunk(tree.body, 1)

    ast.fix_missing_locations(tree)

    return ast.unparse(tree)



import string as meo

__daucau_an_toan__ = meo.punctuation.replace('"', '').replace('\\', '')

__cothenoilaratngau__ = meo.ascii_lowercase + meo.digits + meo.ascii_uppercase + meo.hexdigits + __daucau_an_toan__



def _fix_future_imports_src(src: str) -> str:

    # FIX: 'from __future__ imports must occur at beginning' - reorder to top

    if not isinstance(src, str) or 'from __future__' not in src:

        return src

    try:

        tree = ast.parse(src)

    except SyntaxError:

        # fallback text-based reorder

        try:

            lines = src.splitlines()

            fut = [l for l in lines if l.strip().startswith('from __future__')]

            if not fut:

                return src

            rest = [l for l in lines if not l.strip().startswith('from __future__')]

            # keep encoding/shebang/docstring at very top? keep first line if #!

            return '\n'.join(fut + rest)

        except Exception:

            return src

    body = tree.body

    doc = None

    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):

        doc = body[0]

        body = body[1:]

    futures = [n for n in body if isinstance(n, ast.ImportFrom) and n.module == '__future__']

    if not futures:

        return src

    others = [n for n in body if n not in futures]

    new_body = []

    if doc is not None:

        new_body.append(doc)

    new_body.extend(futures)

    new_body.extend(others)

    try:

        new_tree = ast.Module(body=new_body, type_ignores=[])

        ast.fix_missing_locations(new_tree)

        return ast.unparse(new_tree)

    except Exception:

        return src



def _fix_future_in_ast(mod):

    # FIX AST: reorder future imports to top before compile

    try:

        if not isinstance(mod, ast.Module):

            return mod

        body = mod.body

        doc = None

        if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):

            doc = body[0]

            body = body[1:]

        fut = [n for n in body if isinstance(n, ast.ImportFrom) and getattr(n, 'module', None) == '__future__']

        if not fut:

            return mod

        rest = [n for n in body if n not in fut]

        new_body = []

        if doc is not None:

            new_body.append(doc)

        new_body.extend(fut)

        new_body.extend(rest)

        mod.body = new_body

        ast.fix_missing_locations(mod)

    except Exception:

        pass

    return mod



def obflzmain(metmoi):

    if not metmoi:return '""'

    metmoi=metmoi if isinstance(metmoi,str) else ''

    metmoi = _fix_future_imports_src(metmoi)

    try:

        codeobj = compile(metmoi,'ProJect','exec')

    except SyntaxError as _e:

        if 'from __future__' in str(_e):

            # text fallback: move all future imports to top

            lines = metmoi.splitlines()

            fut = [l for l in lines if l.strip().startswith('from __future__')]

            rest = [l for l in lines if not l.strip().startswith('from __future__')]

            metmoi2 = '\n'.join(fut + rest)

            codeobj = compile(metmoi2,'ProJect','exec')

            metmoi = metmoi2

        else:

            raise

    dump = marshal.dumps(codeobj)

    dump = lzma.compress(dump)

    dump = dump.hex()

    _filler = 'KhangCoderYukiAbiProtectorV5'

    khocdi = (_filler * (len(dump) // len(_filler) + 1))[:len(dump)]

    raw = ''.join((a + b for a, b in zip(khocdi, dump)))

    __map__ = {chr(i): chr((i + 7) % 256) for i in range(256)}

    nen = ''.join((__map__.get(i, i) for i in raw)).encode()

    __ok__ = random.randint(256, 512)

    parts = [nen[i:i + __ok__] for i in range(0, len(nen), __ok__)]

    phanmanh = 'b"".join([' + ','.join((repr(p) for p in parts)) + '])'

    return f"""try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
except:
    pass

try:

    (_0xFx4B5.__setitem__({_uni}({anhxa1('ViThanBienCaBaDao')}), {phanmanh}),

    _Ox3.__setitem__({_uni}({anhxa1('SocLoBanZoLon')}), {anhxa1('decompress')}),

    _Ox3.__setitem__({_uni}({anhxa1('SócLọBănZôLồn')}), {anhxa1('join')}),

    _Ox3.__setitem__(___BoMayLaHeHe__({anhxa('MộtTừThôi')}), {anhxa1('decode')}))

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

try:

    _0xFx4B5[{_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu')})]=KhangCoder(DungCoDecNuaAnhOi).__getattribute__({_uni}(ThậtBuồnCười))(KhangCoder(DungCoDecNuaAnhOi1).__getattribute__({_uni}(SocLoBanZoLon))(getattr(getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')})),{enc('fromhex')})((KyThuatAnCode.__getattribute__({_uni}(SócLọBănZôLồn))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({c})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {c} in ViThanBienCaBaDao.__getattribute__({_uni}(MộtTừThôi))()))[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)])))

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

KhangCoder({enc('builtins')}).__getattribute__({enc('exec')})(_0xFx4B5.get({_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu')}), globals().get({_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu')}))),_0xFx4B5)"""



__daucau_an_toan__=meo.punctuation.replace('"','').replace('\\','')

__cothenoilaratngau__=meo.ascii_lowercase+meo.digits+meo.ascii_uppercase+meo.hexdigits+__daucau_an_toan__

def obflzexec(metmoi):

    if not metmoi:return '""'

    metmoi=metmoi if isinstance(metmoi,str) else ''

    tambo=metmoi.encode().hex()

    _filler = 'KhangCoderYukiAbiProtectorV5'

    khocdi = (_filler * (len(tambo) // len(_filler) + 1))[:len(tambo)]

    raw=''.join(a+b for a,b in zip(khocdi,tambo))

    __map__={chr(i):chr((i+7)%256) for i in range(256)}

    nen=''.join(__map__.get(i,i) for i in raw).encode()

    __ok__=random.randint(256,512)

    parts=[nen[i:i+__ok__] for i in range(0,len(nen),__ok__)]

    phanmanh='b"".join(['+','.join(repr(p) for p in parts)+'])'

    return f"""try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
except:
    pass

try:

    (_Ox3.__setitem__({_uni}({anhxa1(fr"{bavailonctevcl}")}), {phanmanh}), _0xFx4B5.__setitem__({_uni}({anhxa1('GioiThiDeobfDi')}), {anhxa('decode')}))

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

try:

    globals()[___BoMayLaHeHe__({anhxa('BeuBeBongDangiu')})]={_uni}({anhxa1('exec')});_0xFx4B5[{_uni}({anhxa1('GoJoSaToRu')})]={anhxa('join')}

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

ThapChungAnhLevel1000=getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),BeuBeBongDangiu)((lambda {kwds}:getattr(getattr(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),LuaGaTreCon),{_uni}({anhxa1('fromhex')}))({kwds}),{_uni}({anhxa1('decode')}))())((lambda {t}:getattr(KyThuatAnCode,___BoMayLaHeHe__(GoJoSaToRu))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({_str})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {_str} in {t}))(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),LuaGaTreCon)({bavailonctevcl}).__getattribute__(___BoMayLaHeHe__(GioiThiDeobfDi))())[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)]),_0xFx4B5)

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    _yuki_fn = globals().get({_uni}({anhxa1('Yuki_Abi_That_Dang_Iu')})) or _0xFx4B5.get({_uni}({anhxa1('Yuki_Abi_That_Dang_Iu')}))
    if _yuki_fn and callable(_yuki_fn):
        _yuki_fn({enc('ThapChungAnhLevel1000')})
    elif 'Yuki_Abi_That_Dang_Iu' in globals():
        Yuki_Abi_That_Dang_Iu({enc('ThapChungAnhLevel1000')})
    else:
        exec(ThapChungAnhLevel1000, _0xFx4B5)
except Exception:
    pass"""



__daucau_an_toan__=meo.punctuation.replace('"','').replace('\\','')

__cothenoilaratngau__=meo.ascii_lowercase+meo.digits+meo.ascii_uppercase+meo.hexdigits+__daucau_an_toan__

def obflzimport(metmoi):

    if not metmoi:return '""'

    metmoi=metmoi if isinstance(metmoi,str) else ''

    metmoi = _fix_future_imports_src(metmoi)

    try:

        codeobj = compile(metmoi,'ProJect','exec')

    except SyntaxError as _e:

        if 'from __future__' in str(_e):

            lines = metmoi.splitlines()

            fut = [l for l in lines if l.strip().startswith('from __future__')]

            rest = [l for l in lines if not l.strip().startswith('from __future__')]

            metmoi2 = '\n'.join(fut + rest)

            codeobj = compile(metmoi2,'ProJect','exec')

            metmoi = metmoi2

        else:

            raise

    dump = marshal.dumps(codeobj)

    dump = lzma.compress(dump)

    dump = dump.hex()

    _filler = 'KhangCoderYukiAbiProtectorV5'

    khocdi = (_filler * (len(dump) // len(_filler) + 1))[:len(dump)]

    raw=''.join(a+b for a,b in zip(khocdi,dump))

    __map__={chr(i):chr((i+7)%256) for i in range(256)}

    nen=''.join(__map__.get(i,i) for i in raw).encode()

    __ok__=random.randint(256,512)

    parts=[nen[i:i+__ok__] for i in range(0,len(nen),__ok__)]

    phanmanh='b"".join(['+','.join(repr(p) for p in parts)+'])'

    return f"""try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
except:
    pass

try:

    (_0xFx4B5.__setitem__({_uni}({anhxa1('ViThanBienCaBaDao1')}), {phanmanh}),

    _Ox3.__setitem__({_uni}({anhxa1('SocLoBanZoLon1')}), {anhxa1('decompress')}),

    _Ox3.__setitem__({_uni}({anhxa1('SócLọBănZôLồn1')}), {anhxa1('join')}),

    _Ox3.__setitem__(___BoMayLaHeHe__({anhxa('MộtTừThôi1')}), {anhxa1('decode')}))

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

try:

    _0xFx4B5[{_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu1')})]=KhangCoder(DungCoDecNuaAnhOi).__getattribute__({_uni}(ThậtBuồnCười))(KhangCoder(DungCoDecNuaAnhOi1).__getattribute__({_uni}(SocLoBanZoLon1))(getattr(getattr(KhangCoder({enc('builtins')}),___BoMayLaHeHe__({anhxa('bytes')})),{enc('fromhex')})((KyThuatAnCode.__getattribute__({_uni}(SócLọBănZôLồn1))(_{thicthamcrush}((NgaoChoDaiDoanCuoi({c})-ToiㅤCoㅤUocㅤThanhㅤ1ㅤNhacㅤSiㅤNoiㅤLoan)%BoLaLoVuongHahah)for {c} in ViThanBienCaBaDao1.__getattribute__({_uni}(MộtTừThôi1))()))[(ToLaBuaYeu^No1)::(ToLaBuaYeu<<ToLaBuaYeu)])))

except Exception:

    pass

try:
    globals().update(globals().get('_Ox3', {{}}))
    globals().update(globals().get('_0xFx4B5', {{}}))
    if '_Ox3' in globals() and isinstance(_Ox3, dict): _Ox3.update(globals())
    if '_0xFx4B5' in globals() and isinstance(_0xFx4B5, dict): _0xFx4B5.update(globals())
except:
    pass

KhangCoder({enc('types')}).__getattribute__({_uni}({anhxa1('FunctionType')}))(_0xFx4B5.get({_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu1')}), globals().get({_uni}({anhxa1('CoBaoXaRoiBoTaThatLauu1')}))),_0xFx4B5)()"""



mapping = ['你', ' ']

autodeobf = ['\u200b', '\u200d']

def obfsieumanh(s: str):

    if not s:return ast.Constant(value='')

    sep = random.choice(autodeobf)

    parts = []

    for _ch in s:

        num = str(ord(_ch) * 3)

        num += ''.join((random.choice(mapping) for _ in range(random.randint(1, 5))))

        parts.append(num)

    encoded = sep.join(parts)

    _loop_c = rb1()

    code = f"""getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),{enc('str')})().__getattribute__({_uni}({anhxa1('join')}))(getattr(KhangCoder({_uni}({anhxa1('builtins')})),

___BoMayLaHeHe__({anhxa('chr')}))(getattr(KhangCoder(___BoMayLaHeHe__({anhxa('builtins')})),

{enc('int')})(getattr(KhangCoder({enc('builtins')}),

{enc('str')})().join(getattr(KhangCoder({enc('builtins')}),

{enc('filter')})(getattr(getattr(KhangCoder({enc('builtins')}),

{enc('str')}),

{enc('isdigit')}),

{_loop_c})))//XinChaoVietNam)for {_loop_c} in getattr(getattr(KhangCoder({enc('builtins')}),

{enc('str')})({enc(encoded)}),{enc('split')})(getattr(KhangCoder({enc('builtins')}),

{enc('str')})({enc(sep)})))"""

    return ast.parse(code).body[0].value



import string as meo1

__daucau_an_toan__ = meo1.punctuation.replace('"', '').replace('\\', '')

__cothenoilaratngau__ = meo1.ascii_lowercase + meo1.digits + meo1.ascii_uppercase + meo1.hexdigits + __daucau_an_toan__



def obflz1(metmoi, __depth__ = 1):

    if not metmoi:

        return '""'

    metmoi = _fix_future_imports_src(metmoi)

    try:

        codeobj = compile(metmoi, 'ProJect', 'exec')

    except SyntaxError as _e:

        if 'from __future__' in str(_e):

            lines = metmoi.splitlines()

            fut = [l for l in lines if l.strip().startswith('from __future__')]

            rest = [l for l in lines if not l.strip().startswith('from __future__')]

            metmoi2 = '\n'.join(fut + rest)

            codeobj = compile(metmoi2,'ProJect','exec')

            metmoi = metmoi2

        else:

            raise

    data = marshal.dumps(codeobj)

    for _ in range(__depth__):

        data = lzma.compress(data)

        data = marshal.dumps(data)

    tambo = data.hex()

    _filler = 'KhangCoderYukiAbiProtectorV5'

    khocdi = (_filler * (len(tambo) // len(_filler) + 1))[:len(tambo)]

    raw = ''.join((a + b for a, b in zip(khocdi, tambo)))

    nen = lzma.compress(raw.encode())

    __fake1__ = random.randbytes(random.randint(10, 30))

    __fake2__ = random.randbytes(random.randint(20, 50))

    __that__ = __fake1__ + nen + __fake2__

    __qualohaha__ = len(__fake1__)

    __end__ = len(__that__) - len(__fake2__)

    __ok__ = random.randint(1000, 3000)

    parts = [__that__[i:i + __ok__] for i in range(0, len(__that__), __ok__)]

    phanmanh = 'b"".join([' + ','.join((repr(p) for p in parts)) + '])'

    __v1__ = rb()

    __v2__ = rb()

    __v3__ = rb()

    __v4__ = rb()

    __blob_var__ = '_Ox' + uuid.uuid4().hex[:8]

    final_expr = f"(KhangCoder({enc('types')}).__getattribute__({enc('FunctionType')})((lambda {__v1__}:(lambda {__v2__},{__v3__}:{__v1__}({__v1__},{__v2__},{__v3__})))(lambda {__v4__},{__v2__},{__v3__}:{__v4__}({__v4__},getattr(KhangCoder({enc('lzma')}), {enc('decompress')})(getattr(KhangCoder({enc('marshal')}),{enc('loads')})({__v2__})),{__v3__}-ToLaBuaYeu) if {__v3__}> No1 else getattr(KhangCoder({enc('marshal')}),{enc('loads')})({__v2__}))((lambda {kwds}:getattr(getattr(KhangCoder({enc('builtins')}),LuaGaTreCon),{enc('fromhex')})({kwds}))((lambda {x}:{x}[ToLaBuaYeu::ToLaBuaYeu1])(getattr(KhangCoder({enc('lzma')}),{enc('decompress')})({__blob_var__}[{__qualohaha__!r}:{__end__!r}]).__getattribute__({enc('decode')})({enc('latin1')}))),{__depth__}),_Ox3))()"

    return f"""

try:

    _Ox3[{enc(__blob_var__)}]={champ}({sieugaylomalaihay(phanmanh)})
    globals()[{enc(__blob_var__)}] = _Ox3[{enc(__blob_var__)}]
    globals()['{__blob_var__}'] = _Ox3[{enc(__blob_var__)}]
    _Ox3['{__blob_var__}'] = _Ox3[{enc(__blob_var__)}]

except Exception:

    pass

{final_expr}"""



dark = Col.dark_gray

light = Col.light_gray

def stage(text: str, symbol: str = '>>', col1=None) -> str:

    if col1 is None:

        col1 = light

    return f"\n{Col.Symbol(symbol, col1, dark)} {text}{light}"

def stage1(text: str, symbol: str = '>>', col1=None) -> str:

    if col1 is None:

        col1 = light

    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"

def stage2(text: str, symbol: str = '>>', col1=None) -> str:

    if col1 is None:

        col1 = light

    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"

def stage3(text: str, symbol: str = '>>', col1=None) -> str:

    if col1 is None:

        col1 = light

    return f"{Col.Symbol(symbol, col1, dark)} {text}{light}"



class pro(ast.NodeTransformer):



    def visit_Constant(self, node):

        if isinstance(node.value, str):

            return obfsieumanh(node.value)

        return node



# === ENHANCED URL HIDE v2 + REQUESTS HIDE v2 - ALWAYS ON - POLYMORPHIC ===

import re as _re_url_hide

import base64 as _b64_url_hide

import zlib as _zlib_url_hide

import string as _str_url_hide

import uuid as _uuid_url_hide



_YUKI_URL_DECODER_NAME = f'__Yuki_Url_{_uuid_url_hide.uuid4().hex[:8]}__'

_YUKI_URL_DECODER_CURRENT = _YUKI_URL_DECODER_NAME

_YUKI_URL_PATTERNS = ('http://', 'https://', 'ftp://', 'wss://', 'ws://', 'www.')

_YUKI_URL_KEYWORDS = ('api','cdn','webhook','bot','github','discord','telegram','ngrok','t.me','pastebin','raw.github','discordapp','hooks.slack','openai','/v1','/v2','/v3','.io/','.com/','.net/','.org/','.xyz/','.onion/','.dev/','.app/')

_YUKI_REQUESTS_STRINGS = ('requests','urllib3','http.client','socket','urllib.request','urllib.parse','requests.sessions','requests.adapters','Session','HTTPAdapter','urlopen','getaddrinfo','gethostbyname','connect','send','request','get','post','put','delete','patch','head','options')



_re_url_hide_domain = _re_url_hide.compile(r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.[a-z]{2,}(?:/|\b)', _re_url_hide.I)

_re_url_hide_ip = _re_url_hide.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?::\d{1,5})?\b')

_re_url_hide_url = _re_url_hide.compile(r'https?://|ftp://|wss?://|www\.', _re_url_hide.I)



def _is_url_string(s: str) -> bool:

    if not isinstance(s, str):

        return False

    if not s or len(s) < 4 or len(s) > 2048:

        return False

    ls = s.lower()

    if any(p in ls for p in _YUKI_URL_PATTERNS):

        return True

    if _re_url_hide_url.search(ls):

        return True

    if _re_url_hide_ip.search(ls):

        return True

    has_keyword = any(k in ls for k in _YUKI_URL_KEYWORDS)

    has_domain = _re_url_hide_domain.search(ls) is not None

    has_slash = '/' in ls or ':' in ls

    if has_domain and (has_slash or has_keyword):

        return True

    if has_keyword and has_slash and '.' in ls:

        return True

    if _re_url_hide.search(r'[a-z0-9]{2,}\.[a-z]{2,}/', ls) and ('api' in ls or 'cdn' in ls or '/v' in ls or 'webhook' in ls or 'bot' in ls):

        return True

    return False



def _is_requests_string(s: str) -> bool:

    if not isinstance(s, str):

        return False

    return s in _YUKI_REQUESTS_STRINGS or s.lower() in ('requests','urllib3','socket')



def _encode_url_for_hide(s: str) -> str:

    # FIX BUG #3: per-build XOR/ROT keys (no static 0x5A / 13 fingerprint).

    try:

        idx = random.randint(0, 4)

        data = s.encode('utf-8')

        if idx == 0:

            payload = _b64_url_hide.b85encode(_zlib_url_hide.compress(data, 9)).decode('ascii')

        elif idx == 1:

            payload = _b64_url_hide.b64encode(_zlib_url_hide.compress(data, 9)).decode('ascii')

        elif idx == 2:

            payload = _b64_url_hide.b64encode(data).decode('ascii')

        elif idx == 3:

            xored = bytes(b ^ (_YUKI_URL_XOR & 0xFF) for b in data)

            payload = _b64_url_hide.b85encode(xored).decode('ascii')

        else:

            _rr = _YUKI_URL_ROT % 95

            rot = bytes(((b - 32 + _rr) % 95 + 32) if 32 <= b <= 126 else b for b in data)

            payload = _b64_url_hide.b64encode(rot).decode('ascii')

        return f"{idx}:{payload}"

    except:

        try:

            return "2:" + _b64_url_hide.b64encode(s.encode()).decode()

        except:

            return "2:" + s



def _collect_binop_strings(node):

    parts = []

    def _recurse(n):

        if isinstance(n, ast.Constant) and isinstance(n.value, str):

            parts.append(n.value)

            return True

        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):

            return _recurse(n.left) and _recurse(n.right)

        return False

    if _recurse(node):

        def _collect_order(n):

            if isinstance(n, ast.Constant):

                return [n.value]

            if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):

                return _collect_order(n.left) + _collect_order(n.right)

            return []

        ordered = _collect_order(node)

        return ''.join(ordered)

    return None



class UrlHideTransformer(ast.NodeTransformer):

    def __init__(self, decoder_name=None):

        self.decoder = decoder_name or _YUKI_URL_DECODER_CURRENT

        super().__init__()

    def visit_Constant(self, node):

        if isinstance(node.value, str) and _is_url_string(node.value):

            enc = _encode_url_for_hide(node.value)

            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        if isinstance(node.value, bytes) and _is_url_string(node.value.decode('utf-8', errors='ignore')):

            try:

                s = node.value.decode('utf-8')

                enc = _encode_url_for_hide(s)

                return ast.Call(func=ast.Attribute(value=ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[]), attr='encode', ctx=ast.Load()), args=[], keywords=[])

            except:

                pass

        if isinstance(node.value, str) and _is_requests_string(node.value):

            if not _is_url_string(node.value):

                enc = _encode_url_for_hide(node.value)

                return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        return node

    def visit_JoinedStr(self, node):

        for idx, v in enumerate(getattr(node, 'values', [])):

            if isinstance(v, ast.Constant) and isinstance(v.value, str) and _is_url_string(v.value):

                enc = _encode_url_for_hide(v.value)

                node.values[idx] = ast.FormattedValue(value=ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[]), conversion=-1)

            elif isinstance(v, ast.FormattedValue):

                if isinstance(v.value, ast.Constant) and isinstance(v.value.value, str) and _is_url_string(v.value.value):

                    enc = _encode_url_for_hide(v.value.value)

                    v.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        return self.generic_visit(node)

    def visit_BinOp(self, node):

        # Check BEFORE visiting children to catch 'https://' + 'example.com' chain before individual Constants are encoded

        combined = _collect_binop_strings(node)

        if combined and _is_url_string(combined):

            enc = _encode_url_for_hide(combined)

            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        self.generic_visit(node)

        # Also check after visiting for already partially encoded? re-check

        combined2 = _collect_binop_strings(node)

        if combined2 and _is_url_string(combined2):

            enc = _encode_url_for_hide(combined2)

            return ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        return node

    def visit_Dict(self, node):

        self.generic_visit(node)

        return node

    def visit_List(self, node):

        self.generic_visit(node)

        return node

    def visit_Tuple(self, node):

        self.generic_visit(node)

        return node

    def visit_Call(self, node):

        self.generic_visit(node)

        # hide url in kwargs like url=, uri=, endpoint=, host=, domain=

        for kw in node.keywords:

            if kw.arg in ('url','uri','endpoint','host','domain','hostname','server') and isinstance(kw.value, ast.BinOp):

                combined = _collect_binop_strings(kw.value)

                if combined and _is_url_string(combined):

                    enc = _encode_url_for_hide(combined)

                    kw.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

            # also hide Constant hostnames in kwargs like host='example.com'

            if kw.arg in ('host','hostname','domain','server') and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):

                if _is_url_string(kw.value.value) or _re_url_hide_domain.search(kw.value.value):

                    enc = _encode_url_for_hide(kw.value.value)

                    kw.value = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

        if node.args:

            arg0 = node.args[0]

            if isinstance(arg0, ast.BinOp):

                combined = _collect_binop_strings(arg0)

                if combined and _is_url_string(combined):

                    enc = _encode_url_for_hide(combined)

                    node.args[0] = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

            # hide standalone host like getaddrinfo('example.com', 80)

            if isinstance(arg0, ast.Constant) and isinstance(arg0.value, str):

                if _re_url_hide_domain.search(arg0.value) and '.' in arg0.value and len(arg0.value) > 4:

                    # check if parent is getaddrinfo/gethostbyname

                    try:

                        func_name = ""

                        if isinstance(node.func, ast.Attribute):

                            func_name = node.func.attr

                        elif isinstance(node.func, ast.Name):

                            func_name = node.func.id

                        if func_name in ('getaddrinfo','gethostbyname','gethostbyname_ex','create_connection'):

                            enc = _encode_url_for_hide(arg0.value)

                            node.args[0] = ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc)], keywords=[])

                    except:

                        pass

        return node



def inject_url_decoder(tree: ast.Module, decoder_name=None):

    # FIX BUG #3: polymorphic decoder - per-build XOR/ROT, indirect imports (anti-grep),

    # dispatch-dict + opaque predicate (no static 5-branch plaintext fingerprint).

    if decoder_name is None:

        decoder_name = _YUKI_URL_DECODER_CURRENT

        if random.random() < 0.3:

            decoder_name = f'__Yuki_Url_{_uuid_url_hide.uuid4().hex[:6]}__'

    _ux = _YUKI_URL_XOR & 0xFF

    _ur = _YUKI_URL_ROT % 95

    # indirect import expressions to avoid greppable 'import base64/zlib'

    _imp_b64_e = _yuki_chr_expr('base64')

    _imp_zl_e = _yuki_chr_expr('zlib')

    _a = f'_a{uuid.uuid4().hex[:4]}'

    _b = f'_b{uuid.uuid4().hex[:4]}'

    src_lines = []

    src_lines.append(f"def {decoder_name}(__enc__):")

    src_lines.append(f"    try:")

    src_lines.append(f"        {_a}=__import__({_imp_b64_e});{_b}=__import__({_imp_zl_e})")

    src_lines.append(f"        __b64d__, __zl__ = {_a}, {_b}")

    src_lines.append(f"        del {_a}, {_b}")

    src_lines.append(f"        try:")

    src_lines.append(f"            if isinstance(__enc__, str) and \":\" in __enc__:")

    src_lines.append(f"                __idx__, __payload__ = __enc__.split(\":\", 1)")

    src_lines.append(f"                __idx__ = int(__idx__)")

    src_lines.append(f"            else:")

    src_lines.append(f"                __idx__, __payload__ = 0, __enc__")

    src_lines.append(f"            if (len(__enc__) * 2654435761 & 0xFFFFFFFF) == 0xDEADBEEF:")

    src_lines.append(f"                return __enc__")

    src_lines.append(f"            __dispatch__ = {{0: 'z_b85', 1: 'z_b64', 2: 'b64', 3: 'xor', 4: 'rot'}}")

    src_lines.append(f"            __kind__ = __dispatch__.get(__idx__, 'raw')")

    src_lines.append(f"            if __kind__ == 'z_b85':")

    src_lines.append(f"                return __zl__.decompress(__b64d__.b85decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')")

    src_lines.append(f"            elif __kind__ == 'z_b64':")

    src_lines.append(f"                return __zl__.decompress(__b64d__.b64decode(__payload__.encode('ascii'))).decode('utf-8', errors='ignore')")

    src_lines.append(f"            elif __kind__ == 'b64':")

    src_lines.append(f"                return __b64d__.b64decode(__payload__.encode('ascii')).decode('utf-8', errors='ignore')")

    src_lines.append(f"            elif __kind__ == 'xor':")

    src_lines.append(f"                __xored__ = __b64d__.b85decode(__payload__.encode('ascii'))")

    src_lines.append(f"                return bytes(b ^ {_ux} for b in __xored__).decode('utf-8', errors='ignore')")

    src_lines.append(f"            elif __kind__ == 'rot':")

    src_lines.append(f"                __rot__ = __b64d__.b64decode(__payload__.encode('ascii'))")

    src_lines.append(f"                return bytes(((b - 32 - {_ur}) % 95 + 32) if 32 <= b <= 126 else b for b in __rot__).decode('utf-8', errors='ignore')")

    src_lines.append(f"            else:")

    src_lines.append(f"                return __payload__")

    src_lines.append(f"        except:")

    src_lines.append(f"            try:")

    src_lines.append(f"                return __b64d__.b64decode(__enc__.encode()).decode('utf-8', errors='ignore')")

    src_lines.append(f"            except:")

    src_lines.append(f"                return __enc__")

    src_lines.append(f"    except:")

    src_lines.append(f"        return __enc__")

    decoder_src = "\n".join(src_lines)

    try:

        dec_tree = ast.parse(decoder_src)

        tree.body = dec_tree.body + tree.body

        ast.fix_missing_locations(tree)

    except Exception:

        pass

    return tree



def apply_url_hide_always(tree, decoder_name=None):

    try:

        fresh = f'__Yuki_Url_{_uuid_url_hide.uuid4().hex[:7]}__'

        global _YUKI_URL_DECODER_CURRENT

        _YUKI_URL_DECODER_CURRENT = fresh

        tree = inject_url_decoder(tree, decoder_name=fresh)

        tree = UrlHideTransformer(decoder_name=fresh).visit(tree)

        tree = apply_requests_hide(tree, decoder_name=fresh)

        ast.fix_missing_locations(tree)

    except Exception as _e:

        try:

            print(f"[URL-HIDE WARN] {_e}")

        except:

            pass

    return tree



class UrlKwargHideTransformer(ast.NodeTransformer):

    def visit_Call(self, node):

        self.generic_visit(node)

        return node



class RequestsHideTransformer(ast.NodeTransformer):

    def __init__(self, decoder_name=None):

        self.decoder = decoder_name or _YUKI_URL_DECODER_CURRENT

        self.alias_map = {}

        super().__init__()

    def visit_Import(self, node):

        new_body = []

        has_requests = False

        for alias in node.names:

            if alias.name in ('requests','urllib3','urllib.request','http.client','socket'):

                has_requests = True

                enc = _encode_url_for_hide(alias.name)

                asname = alias.asname or alias.name.split('.')[0]

                new_body.append(ast.parse(f"{asname} = __import__({self.decoder}({repr(enc)}))").body[0])

                self.alias_map[alias.name] = asname

            else:

                new_body.append(ast.Import(names=[alias]))

        if has_requests and len(new_body)==1 and isinstance(new_body[0], ast.Assign):

            return new_body[0]

        if has_requests:

            return node

        return node

    def visit_ImportFrom(self, node):

        if node.module in ('requests','urllib3','http.client','urllib.request','socket','requests.sessions','requests.adapters'):

            pass

        return node

    def visit_Attribute(self, node):

        self.generic_visit(node)

        # === BROAD HIDE: any sensitive attr is encoded regardless of base for stealth ===

        _sensitive = ('get','post','put','delete','request','patch','head','options','Session','HTTPAdapter','HTTPConnection','HTTPSConnection','urlopen','getaddrinfo','gethostbyname','gethostbyname_ex','connect','send','sendall','recv','recvfrom','sendto','setsockopt','poolmanager','connectionpool','putrequest','getresponse','endheaders')

        if node.attr in _sensitive:

            base_str = ""

            try:

                base_str = ast.unparse(node.value).lower()

            except:

                try:

                    base_str = getattr(node.value, 'id', '').lower()

                except:

                    base_str = ""

            is_network_base = any(x in base_str for x in ('request','urllib','socket','http','session','adapter','pool','client','conn'))

            is_always_network_attr = node.attr in ('urlopen','getaddrinfo','gethostbyname','connect','send','sendall','recv','Session','HTTPAdapter','HTTPConnection','HTTPSConnection','poolmanager','connectionpool','putrequest','getresponse','request')

            # Always hide 'request' (Session.request) regardless of base - it's rarely dict method

            if node.attr == 'request' or is_always_network_attr:

                enc_attr = _encode_url_for_hide(node.attr)

                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])

            if is_network_base or node.attr in ('get','post','request'):

                if node.attr in ('get','post','put','delete','patch','head','options','request'):

                    if is_network_base or base_str in ('requests','urllib','http','socket') or 'getattr' in base_str:

                        enc_attr = _encode_url_for_hide(node.attr)

                        return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])

                    pass

                else:

                    enc_attr = _encode_url_for_hide(node.attr)

                    return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])

        # Handle Name.attr for urllib.request etc. (already covered above but keep for completeness)

        if isinstance(node.value, ast.Name) and node.value.id in ('requests','urllib','urllib3','http','socket'):

            if node.attr in ('get','post','put','delete','request','patch','head','options','Session','HTTPAdapter','urlopen','getaddrinfo','gethostbyname','gethostbyname_ex','connect','send','sendall','recv','HTTPConnection','HTTPSConnection','poolmanager','connectionpool','request','putrequest','getresponse','endheaders'):

                enc_attr = _encode_url_for_hide(node.attr)

                return ast.Call(func=ast.Name(id='getattr', ctx=ast.Load()), args=[node.value, ast.Call(func=ast.Name(id=self.decoder, ctx=ast.Load()), args=[ast.Constant(value=enc_attr)], keywords=[])], keywords=[])

        return node



def apply_requests_hide(tree, decoder_name=None):

    try:

        dec = decoder_name or _YUKI_URL_DECODER_CURRENT

        tree = RequestsHideTransformer(decoder_name=dec).visit(tree)

        ast.fix_missing_locations(tree)

    except Exception:

        pass

    return tree





def meo(code: str):

    tree = ast.parse(code)

    tree = cv().visit(tree)

    tree = pro().visit(tree)

    ast.fix_missing_locations(tree)

    return ast.unparse(tree)

def _runmain(code):

    code = meo(obflzmain(code))

    return code

def _runexec(code):

    code = meo(obflzexec(code))

    return code

def _runimport(code):

    code = meo(obflzimport(code))

    return code



def phienbantrycath(code):

    if sys.version_info < (3, 10):

        tree = trycatch(code.body, 1)

    else:

        tree = trycatch1(code.body, 1)

    mamoi = ast.Module(body=tree, type_ignores=[])

    ast.fix_missing_locations(mamoi)

    return mamoi

def longjunk(code):

    code = junk1().visit(code)

    return code 

def reversing(code):

    return code

def reversing1(code):

    return code



class Cleanstring(__import__('ast').NodeTransformer):

    def __init__(__khangcoderbadao__):

        __khangcoderbadao__.__imports__={}



    def d(__khangcoderbadao__,__khangcoder__):

        __khangcoderbadao__.generic_visit(__khangcoder__)

        if hasattr(__khangcoder__,'body')and isinstance(__khangcoder__.body,list):

            __khangcoder__.body=[s for s in __khangcoder__.body if s is not None]

        return __khangcoder__



    def vs(__khangcoderbadao__,__khangcoder__):

        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)

        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)

        return __khangcoder__



    def func(__khangcoderbadao__,__khangcoder__):

        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)

        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)

        return __khangcoder__



    def balamon(__khangcoderbadao__,__khangcoder__):

        return __khangcoderbadao__.func(__khangcoder__)



    def idk(__khangcoderbadao__,__khangcoder__):

        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)

        if __khangcoder__.body and isinstance(__khangcoder__.body[0],__import__('ast').Expr)and isinstance(__khangcoder__.body[0].value,__import__('ast').Constant)and isinstance(__khangcoder__.body[0].value.value,str):__khangcoder__.body.pop(0)

        return __khangcoder__



    def visit_Expr(__khangcoderbadao__,__khangcoder__):

        if isinstance(__khangcoder__.value,__import__('ast').Constant)and isinstance(__khangcoder__.value.value,str):return None

        return __khangcoder__



    def visit_Import(__khangcoderbadao__,__khangcoder__):

        for __x__ in __khangcoder__.names:

            __khangcoderbadao__.__imports__[__x__.name]=__x__

        return None



    def visit_Module(__khangcoderbadao__,__khangcoder__):

        __khangcoder__=__khangcoderbadao__.d(__khangcoder__)

        __body__=[]

        if __khangcoderbadao__.__imports__:

            __body__.append(__import__('ast').Import(names=list(__khangcoderbadao__.__imports__.values())))

        __body__+=__khangcoder__.body

        __khangcoder__.body=__body__

        return __khangcoder__



def clean(code):

    tree = ast.parse(code)

    tree = Cleanstring().visit(tree)

    ast.fix_missing_locations(tree)

    return ast.unparse(tree)



def dequybadao(dump, depth=1):

    # FIX BUG #17: cap depth to 1 (no exponential blowup), cache, size guard.

    try:

        depth = int(depth or 1)

    except Exception:

        depth = 1

    if depth != 1:

        depth = 1

    dump = poison_code_object(dump)

    _raw_payload = marshal.dumps(dump)

    import lzma as _lz_ib

    payload = _lz_ib.compress(_raw_payload, preset=6)

    try:

        _cache_key = _yuki_sha256(payload)

        if _cache_key in _DEQUY_CACHE:

            return _DEQUY_CACHE[_cache_key]

    except Exception:

        _cache_key = None

    if len(payload) > 50 * 1024 * 1024:

        raise MemoryError('payload too large')

    # FIX BUG #18: integrity digest of inner payload (verified at runtime).

    _digest = _yuki_sha256(payload)

    for _ in range(depth):

        # FIX BUG #2: 32B key + 8B salt + SHA256-CTR keystream (not 4B repeating XOR).

        # Key/salt/xored are fragmented (no single literal) to block 1-liner extraction.

        import hashlib as _hl_ib, secrets as _sec_ib, base64 as _b64_ib

        _expected_pulse = bytes([0x4A, 0x7B, 0x9C, 0x3D, 0x5E])

        salt = _sec_ib.token_bytes(16)

        sub_salt = _sec_ib.token_bytes(8)

        key = _hl_ib.sha256(_expected_pulse + salt).digest()

        _ks = b''.join(_hl_ib.sha256(key + sub_salt + c.to_bytes(4, 'big')).digest() for c in range((len(payload) + 31) // 32))[:len(payload)]

        xored = bytes(b ^ _ks[i] for i, b in enumerate(payload))

        mathuat = '__XxAbyssProxX__'

        _salt_expr = _yuki_frag_bytes_expr(salt, 8)

        _sub_salt_expr = _yuki_frag_bytes_expr(sub_salt, 8)

        _xor_expr = _yuki_frag_bytes_expr(xored, 128)

        _dg1, _dg2 = _digest[:32], _digest[32:]

        # Hide bad-keyword lists as b64 blobs (anti-grep, fix BUG #7/#8).

        _kw_raw = ','.join(['pycdc', 'decompyle', 'uncompyle', 'decompile', 'deobf', 'disassembl', 'pydisasm', 'unpyc', 'pyfluff', 'marshal_dump', 'tracer', 'hook_exec', 'hook_marshal', 'pylingual', 'pyarmor'])

        _pr_raw = ','.join(['pycdc', 'pycdc.exe', 'decompyle++', 'uncompyle6', 'decompyle', 'pydecomp', 'pylingual', 'xdis', 'pyarmor', 'pyfluff', 'decompile', 'unpyc', 'dis', 'pycdc_gui', 'ida.exe', 'ida64.exe', 'idag.exe', 'idaw.exe', 'x64dbg.exe', 'x32dbg.exe', 'x96dbg.exe', 'cheatengine.exe', 'scylla.exe', 'processhacker.exe', 'procmon.exe', 'wireshark.exe', 'fiddler.exe', 'charles.exe', 'httpcanary.exe', 'mitmproxy.exe', 'burpsuite.exe', 'dnspy.exe', 'de4dot.exe'])

        _kw_b64 = _b64_ib.b64encode(_kw_raw.encode()).decode()

        _pr_b64 = _b64_ib.b64encode(_pr_raw.encode()).decode()

        src = f"""thucheck = __import__('os').path.abspath(__file__)
KhangCoder = __import__

def TrumXamLol():

    # FIX BUG #11: non-destructive tamper response (no file overwrite).

    try:

        import sys as _s, os as _o

        try:

            _o._exit(95)

        except Exception:

            _s.exit(95)

    except SystemExit: raise

    except Exception:

        raise SystemExit('tamper-detected')

def anti():

    import sys, os, time

    import base64 as _b64a

    _bad_kw = tuple(_b64a.b64decode({_kw_b64!r}).decode().split(','))

    _bad_procs = tuple(_b64a.b64decode({_pr_b64!r}).decode().split(','))

    while True:

        try:

            if sys.gettrace() is not None: TrumXamLol()

            for frame in sys._current_frames().values():

                cf = frame

                while cf:

                    ___khangcoder___{q}____ = (getattr(cf.f_code, 'co_filename', '') or '').lower()

                    ___fn_name___ = (getattr(cf.f_code, 'co_name', '') or '').lower()

                    if any(x in ___khangcoder___{q}____ or x in ___fn_name___ for x in _bad_kw):

                        TrumXamLol()

                        os._exit(97)

                    cf = cf.f_back

            for m in list(sys.modules.keys()):

                if any(x in m.lower() for x in ('pycdc', 'decompyle', 'uncompyle', 'decompile', 'xdis', 'pydisasm', 'pylingual', 'deobfuscator')):

                    TrumXamLol()

                    os._exit(96)

            try:

                import ctypes

                _windll2 = getattr(ctypes, 'windll', None)

                k32 = getattr(_windll2, 'kernel32', None) if _windll2 is not None else None

                if k32:

                    class PROCESSENTRY32W(ctypes.Structure):

                        _fields_ = [('dwSize', ctypes.c_ulong), ('cntUsage', ctypes.c_ulong), ('th32ProcessID', ctypes.c_ulong), ('th32DefaultHeapID', ctypes.c_size_t), ('th32ModuleID', ctypes.c_ulong), ('cntThreads', ctypes.c_ulong), ('th32ParentProcessID', ctypes.c_ulong), ('pcPriClassBase', ctypes.c_long), ('dwFlags', ctypes.c_ulong), ('szExeFile', ctypes.c_wchar * 260)]

                    hSnap = k32.CreateToolhelp32Snapshot(0x00000002, 0)

                    if hSnap != -1:

                        pe = PROCESSENTRY32W()

                        pe.dwSize = ctypes.sizeof(PROCESSENTRY32W)

                        if k32.Process32FirstW(hSnap, ctypes.byref(pe)):

                            while True:

                                if any(x in pe.szExeFile.lower() for x in _bad_procs):

                                    hProc = k32.OpenProcess(0x0001, False, pe.th32ProcessID)

                                    if hProc:

                                        k32.TerminateProcess(hProc, 1)

                                        k32.CloseHandle(hProc)

                                    TrumXamLol()

                                    os._exit(137)

                                if not k32.Process32NextW(hSnap, ctypes.byref(pe)): break

                        k32.CloseHandle(hSnap)

            except Exception: pass

        except: pass

        time.sleep(0.35)

try:

    if '__yuki_dequy_started__' not in globals():

        globals()['__yuki_dequy_started__'] = True

        try:

            import _thread as _th_dequy

            _th_dequy.start_new_thread(anti, ())

        except Exception:

            __import__('threading').Thread(target=anti, daemon=True).start()

except: pass

def __xx0Abyss0xx__():

    def _anti_pulse():

        _s = __import__({_yuki_chr_expr('sys')})

        _b0 = 0x4A if _s.gettrace() is None else 0x00

        _m = __import__({_yuki_chr_expr('marshal')})

        _m_ld = getattr(_m, {_yuki_chr_expr('loads')})

        _b1 = 0x7B if (getattr(_m_ld, '__code__', None) is None and 'builtin' in str(type(_m_ld))) else 0x00

        _bt = __import__({_yuki_chr_expr('builtins')})

        _ex = getattr(_bt, {_yuki_chr_expr('exec')})

        _b2 = 0x9C if (getattr(_ex, '__code__', None) is None and 'builtin' in str(type(_ex))) else 0x00

        _ct = __import__({_yuki_chr_expr('ctypes')})

        try:

            _k32 = getattr(getattr(_ct, 'windll', None), 'kernel32', None)

            _b3 = 0x3D if (_k32 is None or _k32.IsDebuggerPresent() == 0) else 0x00

        except Exception:

            _b3 = 0x3D

        _b4 = 0x5E if not any(x in list(_s.modules.keys()) for x in ({_yuki_chr_expr('pycdc')}, {_yuki_chr_expr('pydisasm')}, {_yuki_chr_expr('pdb')}, {_yuki_chr_expr('rpdb')}, {_yuki_chr_expr('frida')})) else 0x00

        return bytes([_b0, _b1, _b2, _b3, _b4])



    __HL = __import__({_yuki_chr_expr('hashlib')})

    __P_pulse = _anti_pulse()

    __K = __HL.sha256(__P_pulse + ({_salt_expr})).digest()

    __S = ({_sub_salt_expr})

    __X = ({_xor_expr})

    __D = ({_dg1!r}+{_dg2!r})

    __N = len(__X)

    __KS = b''.join(__HL.sha256(__K+__S+__c.to_bytes(4, 'big')).digest() for __c in range((__N+32-1)//32))[:__N]

    __P = bytes(__b ^ __KS[__i] for __i, __b in enumerate(__X))

    assert __HL.sha256(__P).hexdigest()==__D, 'integrity'

    __LZ = __import__({_yuki_chr_expr('lzma')})

    __raw_P = bytearray(__LZ.decompress(__P))

    del __KS, __X, __K, __S, __P

    _m_ld = __import__({_yuki_chr_expr('marshal')}).loads

    if getattr(_m_ld, '__code__', None) is not None or 'builtin' not in str(type(_m_ld)):

        TrumXamLol()

    _co_target = _m_ld(__raw_P)

    try:

        __raw_P[:] = bytes(len(__raw_P))

    except Exception: pass

    del __raw_P

    return _co_target, __D, 32, getattr(__import__({_yuki_chr_expr('sysconfig')}), {_yuki_chr_expr('get_path')})({_yuki_chr_expr('stdlib')})

(lambda _r_code=__xx0Abyss0xx__()[0], _r_abi=getattr(__import__({_yuki_chr_expr('builtins')}), {_yuki_chr_expr('exec')}): (globals().update(globals().get('_Ox3', {{}})), globals().pop('__xx0Abyss0xx__', None), _r_abi(_r_code, globals(), globals())))()\n"""

        fname = f'<__Yukiㅤ{random.randint(1000, 9999)}ㅤAbi__>'

        try:

            code = _compile_secure(src, fname, 'exec')

        except Exception:

            code = compile(src, fname, 'exec')

        code = poison_code_object(code)

    # cache single-depth result (fix BUG #17 DoS)

    try:

        _res = marshal.dumps(code)

        if _cache_key is not None:

            _DEQUY_CACHE[_cache_key] = _res

        return _res

    except Exception:

        return marshal.dumps(code)







# ==================== YUKI HYPER-VM ENGINE V4.0 ULTRA BOOSTED ====================

BINARY_OPS = {

    ast.Add: 0x10,

    ast.Sub: 0x11,

    ast.Mult: 0x12,

    ast.Div: 0x13,

    ast.FloorDiv: 0x14,

    ast.Mod: 0x15,

    ast.Pow: 0x16,

    ast.LShift: 0x17,

    ast.RShift: 0x18,

    ast.BitOr: 0x19,

    ast.BitXor: 0x1A,

    ast.BitAnd: 0x1B,

    ast.MatMult: 0x1C,

}



UNARY_OPS = {

    ast.UAdd: 0x20,

    ast.USub: 0x21,

    ast.Not: 0x22,

    ast.Invert: 0x23,

}



COMPARE_OPS = {

    ast.Eq: 0x30,

    ast.NotEq: 0x31,

    ast.Lt: 0x32,

    ast.LtE: 0x33,

    ast.Gt: 0x34,

    ast.GtE: 0x35,

    ast.Is: 0x36,

    ast.IsNot: 0x37,

    ast.In: 0x38,

    ast.NotIn: 0x39,

}



OPCODE_NAMES = [

    'NOP',

    'LOAD_CONST',

    'LOAD_NAME',

    'STORE_NAME',

    'DELETE_NAME',

    'LOAD_GLOBAL',

    'STORE_GLOBAL',

    'DELETE_GLOBAL',

    'LOAD_ATTR',

    'STORE_ATTR',

    'DELETE_ATTR',

    'LOAD_SUBSCR',

    'STORE_SUBSCR',

    'DELETE_SUBSCR',

    'BUILD_LIST',

    'BUILD_TUPLE',

    'BUILD_SET',

    'BUILD_MAP',

    'BUILD_SLICE',

    'BUILD_STRING',

    'LIST_APPEND',

    'SET_ADD',

    'MAP_ADD',

    'BINARY_OP',

    'UNARY_OP',

    'COMPARE_OP',

    'JUMP',

    'JUMP_IF_TRUE',

    'JUMP_IF_FALSE',

    'POP_JUMP_IF_TRUE',

    'POP_JUMP_IF_FALSE',

    'POP_TOP',

    'DUP_TOP',

    'DUP_TOP_TWO',

    'ROT_TWO',

    'ROT_THREE',

    'CALL_FUNC',

    'CALL_KW',

    'CALL_EX',

    'RETURN_VALUE',

    'YIELD_VALUE',

    'GET_ITER',

    'FOR_ITER',

    'IMPORT_NAME',

    'IMPORT_FROM',

    'IMPORT_STAR',

    'SETUP_EXCEPT',

    'POP_EXCEPT',

    'SETUP_WITH',

    'EXIT_WITH',

    'RAISE_VARARGS',

    'MAKE_FUNCTION',

    'MAKE_CLASS',

    'UNPACK_SEQUENCE',

    'UNPACK_EX',

    'FORMAT_VALUE',

    'VM_CHECK',

    'GET_AWAITABLE',

    'GET_AITER',

    'FOR_AITER',

    'SETUP_ASYNC_WITH',

    'EXIT_ASYNC_WITH',

    'STORE_NONLOCAL',

    'DELETE_NONLOCAL',

    'LIST_EXTEND',

    'MAP_UPDATE',

    'SET_UPDATE',

    'REG_STORE',

    'REG_LOAD',

    'REG_SWAP',

    'ACC_STORE',

    'ACC_LOAD',

    'VM_JUNK_NOP'

]







class LocalVarRenamer(ast.NodeTransformer):

    def __init__(self, tree=None):

        self.used_as_keyword = set()

        if tree is not None:

            for node in ast.walk(tree):

                if isinstance(node, ast.Call):

                    for kw in node.keywords:

                        if kw.arg:

                            self.used_as_keyword.add(kw.arg)



    def visit_FunctionDef(self, node):

        self._rename_func_scope(node)

        self.generic_visit(node)

        return node



    def visit_AsyncFunctionDef(self, node):

        self._rename_func_scope(node)

        self.generic_visit(node)

        return node



    def _rename_func_scope(self, func_node):

        def get_scope_nodes(node):

            for child in ast.iter_child_nodes(node):

                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):

                    continue

                yield child

                yield from get_scope_nodes(child)



        explicit_globals = set()

        explicit_nonlocals = set()

        for child in get_scope_nodes(func_node):

            if isinstance(child, ast.Global):

                explicit_globals.update(child.names)

            elif isinstance(child, ast.Nonlocal):

                explicit_nonlocals.update(child.names)



        builtin_names = set(dir(builtins))

        excluded = explicit_globals | explicit_nonlocals | self.used_as_keyword | {'self', 'cls'} | builtin_names



        local_names = set()

        all_args = getattr(func_node.args, 'posonlyargs', []) + func_node.args.args + getattr(func_node.args, 'kwonlyargs', [])

        for a in all_args:

            if a.arg not in excluded and not a.arg.startswith('__'):

                local_names.add(a.arg)

        if func_node.args.vararg and func_node.args.vararg.arg not in excluded and not func_node.args.vararg.arg.startswith('__'):

            local_names.add(func_node.args.vararg.arg)

        if func_node.args.kwarg and func_node.args.kwarg.arg not in excluded and not func_node.args.kwarg.arg.startswith('__'):

            local_names.add(func_node.args.kwarg.arg)



        for n in get_scope_nodes(func_node):

            if isinstance(n, (ast.Assign, ast.AnnAssign, ast.AugAssign)):

                targets = [n.target] if hasattr(n, 'target') else n.targets

                for t in targets:

                    for sub in ast.walk(t):

                        if isinstance(sub, ast.Name) and sub.id not in excluded and not sub.id.startswith('__'):

                            local_names.add(sub.id)

            elif isinstance(n, (ast.For, ast.AsyncFor)):

                for sub in ast.walk(n.target):

                    if isinstance(sub, ast.Name) and sub.id not in excluded and not sub.id.startswith('__'):

                        local_names.add(sub.id)

            elif isinstance(n, ast.ExceptHandler):

                if n.name and n.name not in excluded and not n.name.startswith('__'):

                    local_names.add(n.name)



        name_map = {nm: f'_\u041e\u0445{uuid.uuid4().hex[:6]}' for nm in local_names}



        class ScopeRenamer(ast.NodeTransformer):

            def visit_FunctionDef(self, n): return n

            def visit_AsyncFunctionDef(self, n): return n

            def visit_ClassDef(self, n): return n

            def visit_Name(self, n):

                if n.id in name_map:

                    n.id = name_map[n.id]

                return n

            def visit_arg(self, n):

                if n.arg in name_map:

                    n.arg = name_map[n.arg]

                return n



        for stmt in func_node.body:

            ScopeRenamer().visit(stmt)

        for a in all_args:

            ScopeRenamer().visit(a)

        if func_node.args.vararg: ScopeRenamer().visit(func_node.args.vararg)

        if func_node.args.kwarg: ScopeRenamer().visit(func_node.args.kwarg)





# ==============================================================================
# PYOBFUS & ADVERSARIAL OBFUSCATION ENGINES (MBA + REASONING LOOPS)
# ==============================================================================

class YukiNumericObfuscator(ast.NodeTransformer):
    """
    Mixed Boolean-Arithmetic (MBA) & Value-Preserving Numeric Literal Transmutation.
    Derived from pyobfus (zhurong2020/pyobfus).
    Transmutes integer & float literals into opaque bitwise and hex expressions.
    """
    def __init__(self):
        self._pattern_const_ids = set()

    def transform(self, tree):
        match_case_cls = getattr(ast, 'match_case', None)
        if match_case_cls is not None:
            for node in ast.walk(tree):
                if isinstance(node, match_case_cls):
                    for sub in ast.walk(node.pattern):
                        if isinstance(sub, ast.Constant):
                            self._pattern_const_ids.add(id(sub))
        return self.visit(tree)

    def visit_Constant(self, node):
        value = node.value
        # Booleans are subclass of int in Python, must stay literal
        if isinstance(value, bool) or value is None:
            return node
        if id(node) in self._pattern_const_ids:
            return node
        if isinstance(value, int):
            return self._obfuscate_int(value)
        if isinstance(value, float):
            return self._obfuscate_float(value)
        return node

    def _obfuscate_int(self, value):
        import secrets as _sec
        strat = _sec.randbelow(3)
        mask_range = (1 << 28) - 1
        if strat == 0:
            k = _sec.randbelow(mask_range) + 1
            return ast.BinOp(
                left=ast.Constant(value=value ^ k),
                op=ast.BitXor(),
                right=ast.Constant(value=k)
            )
        elif strat == 1:
            a = _sec.randbelow(mask_range) - (mask_range >> 1)
            return ast.BinOp(
                left=ast.Constant(value=a),
                op=ast.Add(),
                right=ast.Constant(value=value - a)
            )
        else:
            b = _sec.randbelow(mask_range) + 1
            return ast.BinOp(
                left=ast.Constant(value=value + b),
                op=ast.Sub(),
                right=ast.Constant(value=b)
            )

    def _obfuscate_float(self, value):
        hex_repr = float.hex(value)
        return ast.Call(
            func=ast.Attribute(
                value=ast.Name(id='float', ctx=ast.Load()),
                attr='fromhex',
                ctx=ast.Load()
            ),
            args=[ast.Constant(value=hex_repr)],
            keywords=[]
        )


class YukiReasoningLoopInjector:
    """
    Reasoning-Loop & Circular Call-Graph Traps.
    Derived from adversarial-obfuscator (Nixon-H/adversarial-obfuscator).
    Traps AI code assistants (Copilot, Claude Code, Cursor) and static symbolic solvers
    in circular dependency chains (A -> B -> C -> A) guarded by runtime-resolved opaque predicates.
    """
    def __init__(self, seed=None):
        import random as _rnd, secrets as _sec
        self._rng = _rnd.Random(seed) if seed is not None else _sec.SystemRandom()

    def _make_opaque_predicate(self):
        a = self._rng.randint(10, 100)
        b = self._rng.randint(10, 100)
        # Invariant: (a*b + 1) < (a*b) is always False at runtime
        return ast.Compare(
            left=ast.BinOp(
                left=ast.Constant(value=a * b + 1),
                op=ast.Add(),
                right=ast.Constant(value=0)
            ),
            ops=[ast.Lt()],
            comparators=[ast.Constant(value=a * b)]
        )

    def inject_loop(self, tree, depth=3):
        if not isinstance(tree, ast.Module):
            return tree
        funcs = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
        if not funcs:
            return tree
        # Target up to 4 top-level functions to keep overhead minimal
        for func in funcs[:4]:
            if not func.body or any(isinstance(s, (ast.Global, ast.Nonlocal)) for s in func.body):
                continue
            chain = [func.name]
            for _ in range(depth - 1):
                chain.append(f'_yuki_trap_{self._rng.getrandbits(24):06x}')
            chain.append(func.name)

            trap_funcs = []
            for i in range(1, len(chain) - 1):
                caller = chain[i]
                callee = chain[i + 1]
                pred = self._make_opaque_predicate()
                trap_call = ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id=callee, ctx=ast.Load()),
                        args=[ast.Constant(value=0)],
                        keywords=[]
                    )
                )
                trap_funcs.append(
                    ast.FunctionDef(
                        name=caller,
                        args=ast.arguments(
                            posonlyargs=[],
                            args=[ast.arg(arg='_x')],
                            kwonlyargs=[],
                            kw_defaults=[],
                            defaults=[]
                        ),
                        body=[
                            ast.If(test=pred, body=[trap_call], orelse=[]),
                            ast.Return(value=ast.Constant(value=None))
                        ],
                        decorator_list=[]
                    )
                )

            entry_pred = self._make_opaque_predicate()
            entry_call = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id=chain[1], ctx=ast.Load()),
                    args=[ast.Constant(value=0)],
                    keywords=[]
                )
            )
            func.body.insert(0, ast.If(test=entry_pred, body=[entry_call], orelse=[]))
            tree.body = trap_funcs + tree.body
        ast.fix_missing_locations(tree)
        return tree


class ControlFlowFlattener(ast.NodeTransformer):

    def __init__(self, min_statements=3, add_bogus_blocks=True):

        self.min_statements = min_statements

        self.add_bogus_blocks = add_bogus_blocks



    def visit_FunctionDef(self, node):

        self.generic_visit(node)

        node.body = self._flatten_body(node.body)

        return node



    def visit_AsyncFunctionDef(self, node):

        self.generic_visit(node)

        node.body = self._flatten_body(node.body)

        return node



    def _flatten_body(self, stmts):

        if len(stmts) < self.min_statements:

            return stmts



        headers = []

        work_stmts = []



        is_header_phase = True

        for i, stmt in enumerate(stmts):

            if is_header_phase and i == 0 and isinstance(stmt, ast.Expr) and isinstance(getattr(stmt, 'value', None), ast.Constant) and isinstance(stmt.value.value, str):

                headers.append(stmt)

            elif isinstance(stmt, (ast.Global, ast.Nonlocal)):

                headers.append(stmt)

            else:

                is_header_phase = False

                work_stmts.append(stmt)



        if len(work_stmts) < self.min_statements:

            return stmts



        n = len(work_stmts)

        state_ids = []

        num_states = n + 1 + (2 if self.add_bogus_blocks else 0)

        while len(state_ids) < num_states:

            sid = random.randint(0x100000, 0xFFFFFF)

            if sid not in state_ids:

                state_ids.append(sid)



        real_state_ids = state_ids[:n + 1]

        bogus_state_ids = state_ids[n + 1:]



        entry_state = real_state_ids[0]

        exit_state = real_state_ids[-1]



        state_var = f"_Ox{uuid.uuid4().hex[:8]}"



        blocks = []

        for i in range(n):

            curr_sid = real_state_ids[i]

            next_sid = real_state_ids[i + 1]

            stmt = work_stmts[i]

            block_body = [stmt]



            if not isinstance(stmt, (ast.Return, ast.Raise)):

                _mask = random.randint(0x100000, 0xFFFFFF)

                _xor_v = next_sid ^ _mask

                block_body.append(

                    ast.Assign(

                        targets=[ast.Name(id=state_var, ctx=ast.Store())],

                        value=ast.BinOp(

                            left=ast.Constant(value=_xor_v),

                            op=ast.BitXor(),

                            right=ast.Constant(value=_mask)

                        )

                    )

                )

            blocks.append((curr_sid, block_body))



        if self.add_bogus_blocks:

            decoy_names = [

                '_crypto_nonce_entropy', '_rsa_quantum_factor', '_neural_gradient_bias',

                '_sha3_sponge_state', '_zkp_polynomial_witness', '_elliptic_curve_scalar',

                '_matrix_eigen_weight', '_blockchain_merkle_root'

            ]

            for bsid in bogus_state_ids:

                random_next = random.choice(real_state_ids)

                decoy_var = random.choice(decoy_names) + f"_{uuid.uuid4().hex[:4]}"

                _bmask = random.randint(0x100000, 0xFFFFFF)

                _bxor_v = random_next ^ _bmask

                bogus_body = [

                    ast.Assign(

                        targets=[ast.Name(id=decoy_var, ctx=ast.Store())],

                        value=ast.BinOp(

                            left=ast.Constant(value=random.randint(0x100000, 0x999999)),

                            op=ast.BitXor(),

                            right=ast.BinOp(

                                left=ast.Name(id=state_var, ctx=ast.Load()),

                                op=ast.BitAnd(),

                                right=ast.Constant(value=0xFFFF)

                            )

                        )

                    ),

                    ast.Assign(

                        targets=[ast.Name(id=state_var, ctx=ast.Store())],

                        value=ast.BinOp(

                            left=ast.Constant(value=_bxor_v),

                            op=ast.BitXor(),

                            right=ast.Constant(value=_bmask)

                        )

                    )

                ]

                blocks.append((bsid, bogus_body))



        random.shuffle(blocks)



        if_root = None

        curr_if = None



        for sid, b_body in blocks:

            test_expr = ast.Compare(

                left=ast.Name(id=state_var, ctx=ast.Load()),

                ops=[ast.Eq()],

                comparators=[ast.Constant(value=sid)]

            )

            branch = ast.If(test=test_expr, body=b_body, orelse=[])

            if if_root is None:

                if_root = branch

                curr_if = branch

            else:

                curr_if.orelse = [branch]

                curr_if = branch



        while_loop = ast.While(

            test=ast.Compare(

                left=ast.Name(id=state_var, ctx=ast.Load()),

                ops=[ast.NotEq()],

                comparators=[ast.Constant(value=exit_state)]

            ),

            body=[if_root],

            orelse=[]

        )



        init_state = ast.Assign(

            targets=[ast.Name(id=state_var, ctx=ast.Store())],

            value=ast.Constant(value=entry_state)

        )



        new_body = []

        new_body.extend(headers)

        new_body.append(init_state)

        new_body.append(while_loop)



        return new_body





class ChainedCompareDesugar(ast.NodeTransformer):

    def __init__(self):

        self._counter = 0



    def visit_Compare(self, node):

        self.generic_visit(node)

        if len(node.ops) <= 1:

            return node

        pairs = []

        curr_left = node.left

        for op, comp in zip(node.ops, node.comparators[:-1]):

            if not isinstance(comp, (ast.Name, ast.Constant)):

                self._counter += 1

                var_name = f'__yuki_cmp_{self._counter}__'

                walrus = ast.NamedExpr(

                    target=ast.Name(id=var_name, ctx=ast.Store()),

                    value=comp

                )

                pairs.append(ast.Compare(left=curr_left, ops=[op], comparators=[walrus]))

                curr_left = ast.Name(id=var_name, ctx=ast.Load())

            else:

                pairs.append(ast.Compare(left=curr_left, ops=[op], comparators=[comp]))

                curr_left = comp

        pairs.append(ast.Compare(left=curr_left, ops=[node.ops[-1]], comparators=[node.comparators[-1]]))

        new_node = ast.BoolOp(op=ast.And(), values=pairs)

        return ast.copy_location(new_node, node)





class YukiBoostedVMCompiler:

    def __init__(self, opcode_map=None, seed=None, is_module=True, is_class=False):

        self.constants = []

        self.names = []

        self.instructions = []

        self.loop_stack = []

        self.with_stack = []

        self.label_counter = 0

        self.seed = seed if seed is not None else random.randint(0x10000000, 0x7FFFFFFF)

        self.opcode_map = opcode_map or {name: i for i, name in enumerate(OPCODE_NAMES)}

        self.is_module = is_module

        self.is_class = is_class

        self.globals = set()

        self.nonlocals = set()

        self.reg_depth = 0

    def _emit_decoy_sequence(self):
        c_idx = self.get_const_idx(random.randint(1000, 99999))
        n_idx = self.get_name_idx(f"_yuki_decoy_{random.randint(1000, 9999)}")
        style = random.randint(0, 3)
        if style == 0:
            self.emit('LOAD_CONST', c_idx)
            self.emit('STORE_NAME', n_idx)
        elif style == 1:
            self.emit('LOAD_CONST', c_idx)
            self.emit('POP_TOP', 0)
        elif style == 2:
            self.emit('VM_JUNK_NOP', random.randint(1, 0xFFFFF))
            self.emit('NOP', 0)
        else:
            self.emit('LOAD_CONST', c_idx)
            self.emit('STORE_GLOBAL', n_idx)

    def _maybe_emit_trampoline(self, prob=0.20):
        if random.random() >= prob:
            return
        mode = random.randint(0, 1)
        if mode == 0:
            target = self.new_label()
            self.emit('JUMP', target)
            self._emit_decoy_sequence()
            self.emit_label(target)
        else:
            target = self.new_label()
            c_true = self.get_const_idx(True)
            self.emit('LOAD_CONST', c_true)
            self.emit('POP_JUMP_IF_TRUE', target)
            self._emit_decoy_sequence()
            self.emit_label(target)



    def _collect_scope_decls(self, stmts):

        globs, nonlocs = set(), set()

        for stmt in stmts:

            if isinstance(stmt, ast.Global):

                globs.update(stmt.names)

            elif isinstance(stmt, ast.Nonlocal):

                nonlocs.update(stmt.names)

            elif isinstance(stmt, (ast.If, ast.While, ast.For, ast.AsyncFor, ast.With, ast.AsyncWith)):

                g, n = self._collect_scope_decls(stmt.body)

                globs.update(g); nonlocs.update(n)

                g, n = self._collect_scope_decls(getattr(stmt, 'orelse', []))

                globs.update(g); nonlocs.update(n)

            elif isinstance(stmt, ast.Try):

                g, n = self._collect_scope_decls(stmt.body)

                globs.update(g); nonlocs.update(n)

                for h in stmt.handlers:

                    g, n = self._collect_scope_decls(h.body)

                    globs.update(g); nonlocs.update(n)

                g, n = self._collect_scope_decls(stmt.orelse)

                globs.update(g); nonlocs.update(n)

                g, n = self._collect_scope_decls(stmt.finalbody)

                globs.update(g); nonlocs.update(n)

        return globs, nonlocs



    def new_label(self):

        self.label_counter += 1

        return f"__L_{self.label_counter}"



    def get_const_idx(self, val):

        for idx, c in enumerate(self.constants):

            if type(c) is type(val) and c == val:

                return idx

        self.constants.append(val)

        return len(self.constants) - 1



    def get_name_idx(self, name):

        if name in self.names:

            return self.names.index(name)

        self.names.append(name)

        return len(self.names) - 1



    def emit(self, op, arg=0):

        self.instructions.append((op, arg))



    def emit_label(self, label):

        self.instructions.append(('LABEL', label))



    def compile(self, node):

        if isinstance(node, str):

            node = ast.parse(node)

        node = ChainedCompareDesugar().visit(node)

        ast.fix_missing_locations(node)

        if hasattr(node, 'body') and isinstance(node.body, list):

            self.globals, self.nonlocals = self._collect_scope_decls(node.body)

        self.visit(node)

        self.emit('LOAD_CONST', self.get_const_idx(None))

        self.emit('RETURN_VALUE', 0)

        return self.link()



    def link(self):

        label_map = {}

        clean_ins = []

        for op, arg in self.instructions:

            if op == 'LABEL':

                label_map[arg] = len(clean_ins)

            else:

                clean_ins.append((op, arg))

        

        final_ins = []

        for op, arg in clean_ins:

            op_code = self.opcode_map[op]

            if isinstance(arg, str) and arg.startswith('__L_'):

                final_ins.append((op_code, label_map[arg]))

            else:

                final_ins.append((op_code, arg))



        packed_bytes = bytearray()

        seed = self.seed

        num_opcodes = len(OPCODE_NAMES)

        

        pepper = _YUKI_HVM_PEPPER

        epoch = max(1, int(_YUKI_HVM_EPOCH))

        k_mul = _YUKI_HVM_K

        k_add = _YUKI_HVM_K2

        last_e = None

        block = b''

        for idx, (op_code, arg_val) in enumerate(final_ins):

            # Ultra Real VM: SHA256 epoch material + unique per-instruction keys.

            # Key schedule rotates every `epoch` ops — no single static multiplier.

            e = idx // epoch

            if e != last_e:

                block = _yuki_hvm_epoch_block(seed, e, pepper, k_mul, k_add)

                last_e = e

            k_op, k_arg = _yuki_hvm_ins_keys(block, idx, num_opcodes)

            enc_op = (op_code + k_op) % num_opcodes

            enc_arg = (int(arg_val) ^ k_arg) & 0xFFFFFFFF

            packed_bytes.extend(struct.pack('>BI', enc_op, enc_arg))



        chk = zlib.adler32(packed_bytes) & 0xFFFFFFFF

        # HyperVM v8.0 Quantum: Dynamic Polymorphic Constant Pool Encryption
        seed = self.seed
        masked_constants = []
        for i, c in enumerate(self.constants):
            if isinstance(c, str):
                if len(c) >= 6:
                    k = ((seed ^ 0xA5A5A5A5) + i * 0x1F35) & 0xFF
                    enc_b = bytearray()
                    prev = k
                    for j, b in enumerate(c.encode('utf-8')):
                        eb = b ^ ((k + j * 17 + prev) & 0xFF)
                        enc_b.append(eb)
                        prev = eb
                    masked_constants.append((('__YUKI_HVM7__', 0x75), bytes(enc_b), k))
                else:
                    k = ((seed ^ 0xA5A5A5A5) + i * 0x1F35) & 0xFF
                    enc_b = bytes([(b ^ ((k + j * 7) & 0xFF)) for j, b in enumerate(c.encode('utf-8'))])
                    masked_constants.append((('__YUKI_HVM7__', 0x70), enc_b, k))
            elif isinstance(c, bytes):
                k = ((seed ^ 0x5A5A5A5A) + i * 0x3F17) & 0xFF
                enc_b = bytes([(b ^ ((k + j * 11) & 0xFF)) for j, b in enumerate(c)])
                masked_constants.append((('__YUKI_HVM7__', 0x71), enc_b, k))
            elif type(c) is int and not isinstance(c, bool) and abs(c) > 0:
                k = ((seed ^ 0x12345678) + i * 0x7B9D) & 0xFFFFFFFF
                masked_constants.append((('__YUKI_HVM7__', 0x72), c ^ k, k))
            elif type(c) is float:
                raw_b = struct.pack('>d', c)
                k = ((seed ^ 0x9E3779B9) + i * 0x45D9) & 0xFF
                enc_b = bytes([(b ^ ((k + j * 13) & 0xFF)) for j, b in enumerate(raw_b)])
                masked_constants.append((('__YUKI_HVM7__', 0x73), enc_b, k))
            else:
                masked_constants.append(c)

        masked_names = []
        for i, name in enumerate(self.names):
            k = ((self.seed ^ 0x6C3A9B41) + i * 0x2D71) & 0xFF
            enc_b = bytes([(b ^ ((k + j * 13) & 0xFF)) for j, b in enumerate(name.encode('utf-8'))])
            masked_names.append((('__YUKI_HVM7_NM__', 0x88), enc_b, k))

        import hashlib as _hl_seal

        seal = _hl_seal.sha256(repr(tuple(masked_names)).encode('utf-8') + repr(len(masked_constants)).encode('utf-8')).digest()



        return {

            'bytecode': bytes(packed_bytes),

            'length': len(final_ins),

            'seed': self.seed,

            'chk': chk,

            'seal': seal,

            'constants': masked_constants,

            'names': masked_names

        }



    def visit(self, node):

        method = 'visit_' + node.__class__.__name__

        visitor = getattr(self, method, self.generic_visit)

        return visitor(node)



    def generic_visit(self, node):

        raise NotImplementedError(f"BoostedVM AST Visitor not implemented for {node.__class__.__name__}")



    def visit_Module(self, node):

        for stmt in node.body:

            self.visit(stmt)

            if random.random() < 0.15:

                self.emit('VM_JUNK_NOP', random.randint(1, 0xFFFFF))

            self._maybe_emit_trampoline(prob=0.20)



    def visit_Expr(self, node):

        self.visit(node.value)

        self.emit('POP_TOP', 0)



    def visit_Pass(self, node):

        self.emit('NOP', 0)



    def visit_Constant(self, node):

        idx = self.get_const_idx(node.value)

        self.emit('LOAD_CONST', idx)



    def visit_Name(self, node):

        idx = self.get_name_idx(node.id)

        if isinstance(node.ctx, ast.Load):

            if node.id in self.globals:

                self.emit('LOAD_GLOBAL', idx)

            else:

                self.emit('LOAD_NAME', idx)

        elif isinstance(node.ctx, ast.Store):

            if node.id in self.globals:

                self.emit('STORE_GLOBAL', idx)

            elif node.id in self.nonlocals:

                self.emit('STORE_NONLOCAL', idx)

            else:

                self.emit('STORE_NAME', idx)

        elif isinstance(node.ctx, ast.Del):

            if node.id in self.globals:

                self.emit('DELETE_GLOBAL', idx)

            elif node.id in self.nonlocals:

                self.emit('DELETE_NONLOCAL', idx)

            else:

                self.emit('DELETE_NAME', idx)



    def visit_Global(self, node):

        pass



    def visit_Nonlocal(self, node):

        pass



    def visit_Assign(self, node):

        self.visit(node.value)

        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name) and random.random() < 0.35:

            reg_id = random.randint(0, 7)

            self.emit('REG_STORE', reg_id)

            self.emit('REG_LOAD', reg_id)

        for i, target in enumerate(node.targets):

            if i < len(node.targets) - 1:

                self.emit('DUP_TOP', 0)

            self.visit_target(target)



    def visit_AnnAssign(self, node):

        if self.is_class and isinstance(node.target, ast.Name):

            self.visit(node.annotation)

            self.emit('LOAD_NAME', self.get_name_idx('__annotations__'))

            self.emit('LOAD_CONST', self.get_const_idx(node.target.id))

            self.emit('STORE_SUBSCR', 0)

        if node.value:

            self.visit(node.value)

            self.visit_target(node.target)



    def visit_AugAssign(self, node):

        if isinstance(node.target, ast.Name):

            idx = self.get_name_idx(node.target.id)

            if node.target.id in self.globals:

                self.emit('LOAD_GLOBAL', idx)

                self.visit(node.value)

                op_sym = BINARY_OPS[node.op.__class__]

                self.emit('BINARY_OP', self.get_const_idx(op_sym))

                self.emit('STORE_GLOBAL', idx)

            elif node.target.id in self.nonlocals:

                self.emit('LOAD_NAME', idx)

                self.visit(node.value)

                op_sym = BINARY_OPS[node.op.__class__]

                self.emit('BINARY_OP', self.get_const_idx(op_sym))

                self.emit('STORE_NONLOCAL', idx)

            else:

                self.emit('LOAD_NAME', idx)

                self.visit(node.value)

                op_sym = BINARY_OPS[node.op.__class__]

                self.emit('BINARY_OP', self.get_const_idx(op_sym))

                self.emit('STORE_NAME', idx)

        elif isinstance(node.target, ast.Attribute):

            self.visit(node.target.value)

            self.emit('DUP_TOP', 0)

            attr_idx = self.get_name_idx(node.target.attr)

            self.emit('LOAD_ATTR', attr_idx)

            self.visit(node.value)

            op_sym = BINARY_OPS[node.op.__class__]

            self.emit('BINARY_OP', self.get_const_idx(op_sym))

            self.emit('ROT_TWO', 0)

            self.emit('STORE_ATTR', attr_idx)

        elif isinstance(node.target, ast.Subscript):

            self.visit(node.target.value)

            self.visit(node.target.slice)

            self.emit('DUP_TOP_TWO', 0)

            self.emit('LOAD_SUBSCR', 0)

            self.visit(node.value)

            op_sym = BINARY_OPS[node.op.__class__]

            self.emit('BINARY_OP', self.get_const_idx(op_sym))

            self.emit('ROT_THREE', 0)

            self.emit('STORE_SUBSCR', 0)

        else:

            raise NotImplementedError(f"AugAssign not supported for {type(node.target)}")



    def visit_target(self, target):

        if isinstance(target, ast.Name):

            idx = self.get_name_idx(target.id)

            if target.id in self.globals:

                self.emit('STORE_GLOBAL', idx)

            elif target.id in self.nonlocals:

                self.emit('STORE_NONLOCAL', idx)

            else:

                self.emit('STORE_NAME', idx)

        elif isinstance(target, ast.Attribute):

            self.visit(target.value)

            self.emit('STORE_ATTR', self.get_name_idx(target.attr))

        elif isinstance(target, ast.Subscript):

            self.visit(target.value)

            self.visit(target.slice)

            self.emit('STORE_SUBSCR', 0)

        elif isinstance(target, (ast.Tuple, ast.List)):

            star_indices = [idx for idx, elt in enumerate(target.elts) if isinstance(elt, ast.Starred)]

            if star_indices:

                star_idx = star_indices[0]

                m = star_idx

                k = len(target.elts) - star_idx - 1

                self.emit('UNPACK_EX', (m << 8) | k)

                for elt in target.elts:

                    if isinstance(elt, ast.Starred):

                        self.visit_target(elt.value)

                    else:

                        self.visit_target(elt)

            else:

                self.emit('UNPACK_SEQUENCE', len(target.elts))

                for elt in target.elts:

                    self.visit_target(elt)

        elif isinstance(target, ast.Starred):

            self.visit_target(target.value)

        else:

            raise NotImplementedError(f"Target not supported {type(target)}")



    def visit_Delete(self, node):

        for target in node.targets:

            if isinstance(target, ast.Name):

                idx = self.get_name_idx(target.id)

                if target.id in self.globals:

                    self.emit('DELETE_GLOBAL', idx)

                elif target.id in self.nonlocals:

                    self.emit('DELETE_NONLOCAL', idx)

                else:

                    self.emit('DELETE_NAME', idx)

            elif isinstance(target, ast.Attribute):

                self.visit(target.value)

                self.emit('DELETE_ATTR', self.get_name_idx(target.attr))

            elif isinstance(target, ast.Subscript):

                self.visit(target.value)

                self.visit(target.slice)

                self.emit('DELETE_SUBSCR', 0)



    def visit_BinOp(self, node):

        self.visit(node.left)

        if self.reg_depth < 12 and random.random() < 0.35:

            reg = self.reg_depth

            self.reg_depth += 1

            self.emit('REG_STORE', reg)

            self.visit(node.right)

            self.emit('REG_LOAD', reg)

            self.reg_depth -= 1

            self.emit('ROT_TWO', 0)

        else:

            self.visit(node.right)

        op_sym = BINARY_OPS[node.op.__class__]

        self.emit('BINARY_OP', self.get_const_idx(op_sym))



    def visit_UnaryOp(self, node):

        self.visit(node.operand)

        op_sym = UNARY_OPS[node.op.__class__]

        self.emit('UNARY_OP', self.get_const_idx(op_sym))



    def visit_BoolOp(self, node):

        is_and = isinstance(node.op, ast.And)

        end_label = self.new_label()

        for i, val in enumerate(node.values):

            self.visit(val)

            if i < len(node.values) - 1:

                self.emit('DUP_TOP', 0)

                if is_and:

                    self.emit('POP_JUMP_IF_FALSE', end_label)

                else:

                    self.emit('POP_JUMP_IF_TRUE', end_label)

                self.emit('POP_TOP', 0)

        self.emit_label(end_label)



    def visit_Compare(self, node):

        if len(node.ops) == 1:

            self.visit(node.left)

            if self.reg_depth < 12 and random.random() < 0.35:

                reg = self.reg_depth

                self.reg_depth += 1

                self.emit('REG_STORE', reg)

                self.visit(node.comparators[0])

                self.emit('REG_LOAD', reg)

                self.reg_depth -= 1

                self.emit('ROT_TWO', 0)

            else:

                self.visit(node.comparators[0])

            op_sym = COMPARE_OPS[node.ops[0].__class__]

            self.emit('COMPARE_OP', self.get_const_idx(op_sym))

        else:

            desugared = ChainedCompareDesugar().visit(node)

            ast.fix_missing_locations(desugared)

            self.visit(desugared)



    def visit_Call(self, node):

        has_star_args = any(isinstance(a, ast.Starred) for a in node.args)

        has_star_kwargs = any(kw.arg is None for kw in node.keywords)



        if has_star_args or has_star_kwargs:

            self.visit(node.func)

            self.emit('BUILD_LIST', 0)

            for arg in node.args:

                if isinstance(arg, ast.Starred):

                    self.visit(arg.value)

                    self.emit('LIST_EXTEND', 1)

                else:

                    self.visit(arg)

                    self.emit('LIST_APPEND', 1)

            self.emit('BUILD_MAP', 0)

            for kw in node.keywords:

                if kw.arg is None:

                    self.visit(kw.value)

                    self.emit('MAP_UPDATE', 1)

                else:

                    self.emit('LOAD_CONST', self.get_const_idx(kw.arg))

                    self.visit(kw.value)

                    self.emit('MAP_ADD', 1)

            self.emit('CALL_EX', 0)

        elif node.keywords:

            self.visit(node.func)

            for arg in node.args:

                self.visit(arg)

            kw_names = []

            for kw in node.keywords:

                kw_names.append(kw.arg)

                self.visit(kw.value)

            kw_idx = self.get_const_idx(tuple(kw_names))

            self.emit('CALL_KW', (len(node.args) << 16) | (kw_idx & 0xFFFF))

        else:

            self.visit(node.func)

            for arg in node.args:

                self.visit(arg)

            self.emit('CALL_FUNC', len(node.args))



    def visit_Attribute(self, node):

        self.visit(node.value)

        idx = self.get_name_idx(node.attr)

        self.emit('LOAD_ATTR', idx)



    def visit_Subscript(self, node):

        self.visit(node.value)

        self.visit(node.slice)

        self.emit('LOAD_SUBSCR', 0)



    def visit_Slice(self, node):

        count = 0

        if node.lower:

            self.visit(node.lower)

            count += 1

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

            count += 1

        if node.upper:

            self.visit(node.upper)

            count += 1

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

            count += 1

        if node.step:

            self.visit(node.step)

            count += 1

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

            count += 1

        self.emit('BUILD_SLICE', count)



    def visit_List(self, node):

        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)

        if has_unpack:

            self.emit('BUILD_LIST', 0)

            for elt in node.elts:

                if isinstance(elt, ast.Starred):

                    self.visit(elt.value)

                    self.emit('LIST_EXTEND', 1)

                else:

                    self.visit(elt)

                    self.emit('LIST_APPEND', 1)

        else:

            for elt in node.elts:

                self.visit(elt)

            self.emit('BUILD_LIST', len(node.elts))



    def visit_Tuple(self, node):

        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)

        if has_unpack:

            self.emit('BUILD_LIST', 0)

            for elt in node.elts:

                if isinstance(elt, ast.Starred):

                    self.visit(elt.value)

                    self.emit('LIST_EXTEND', 1)

                else:

                    self.visit(elt)

                    self.emit('LIST_APPEND', 1)

            self.emit('LOAD_NAME', self.get_name_idx('tuple'))

            self.emit('ROT_TWO', 0)

            self.emit('CALL_FUNC', 1)

        else:

            for elt in node.elts:

                self.visit(elt)

            self.emit('BUILD_TUPLE', len(node.elts))



    def visit_Set(self, node):

        has_unpack = any(isinstance(e, ast.Starred) for e in node.elts)

        if has_unpack:

            self.emit('BUILD_SET', 0)

            for elt in node.elts:

                if isinstance(elt, ast.Starred):

                    self.visit(elt.value)

                    self.emit('SET_UPDATE', 1)

                else:

                    self.visit(elt)

                    self.emit('SET_ADD', 1)

        else:

            for elt in node.elts:

                self.visit(elt)

            self.emit('BUILD_SET', len(node.elts))



    def visit_Dict(self, node):

        has_unpack = any(k is None for k in node.keys)

        if has_unpack:

            self.emit('BUILD_MAP', 0)

            for k, v in zip(node.keys, node.values):

                if k is None:

                    self.visit(v)

                    self.emit('MAP_UPDATE', 1)

                else:

                    self.emit('LOAD_CONST', self.get_const_idx(k.value) if isinstance(k, ast.Constant) else None)

                    if not isinstance(k, ast.Constant):

                        self.instructions.pop()

                        self.visit(k)

                    self.visit(v)

                    self.emit('MAP_ADD', 1)

        else:

            for k, v in zip(node.keys, node.values):

                self.visit(k)

                self.visit(v)

            self.emit('BUILD_MAP', len(node.keys))



    def visit_JoinedStr(self, node):

        for val in node.values:

            self.visit(val)

        self.emit('BUILD_STRING', len(node.values))



    def visit_FormattedValue(self, node):

        self.visit(node.value)

        fmt = node.format_spec.values[0].value if (node.format_spec and node.format_spec.values) else ''

        self.emit('FORMAT_VALUE', self.get_const_idx((node.conversion, fmt)))



    def visit_NamedExpr(self, node):

        self.visit(node.value)

        self.emit('DUP_TOP', 0)

        self.visit_target(node.target)



    def visit_Starred(self, node):

        self.visit(node.value)



    def visit_Yield(self, node):

        if node.value:

            self.visit(node.value)

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

        self.emit('YIELD_VALUE', 0)

    def visit_YieldFrom(self, node):

        loop_start = self.new_label()

        exhaust_label = self.new_label()

        if node.value:

            self.visit(node.value)

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

        self.emit('GET_ITER', 0)

        self.emit_label(loop_start)

        self.emit('FOR_ITER', exhaust_label)

        self.emit('YIELD_VALUE', 0)

        self.emit('POP_TOP', 0)

        self.emit('JUMP', loop_start)

        self.emit_label(exhaust_label)

        self.emit('LOAD_CONST', self.get_const_idx(None))



    def visit_Await(self, node):

        self.visit(node.value)

        self.emit('GET_AWAITABLE', 0)



    def visit_GeneratorExp(self, node):

        self.emit('BUILD_LIST', 0)

        self._compile_list_comprehension(node.generators, 0, node.elt, depth=1)

        self.emit('GET_ITER', 0)



    def visit_If(self, node):

        else_label = self.new_label()

        end_label = self.new_label()

        self.visit(node.test)

        self.emit('POP_JUMP_IF_FALSE', else_label)

        for stmt in node.body:

            self.visit(stmt)

        self.emit('JUMP', end_label)

        self.emit_label(else_label)

        if node.orelse:

            for stmt in node.orelse:

                self.visit(stmt)

        self.emit_label(end_label)



    def visit_IfExp(self, node):

        else_label = self.new_label()

        end_label = self.new_label()

        self.visit(node.test)

        self.emit('POP_JUMP_IF_FALSE', else_label)

        self.visit(node.body)

        self.emit('JUMP', end_label)

        self.emit_label(else_label)

        self.visit(node.orelse)

        self.emit_label(end_label)



    def visit_While(self, node):

        loop_start = self.new_label()

        exhaust_label = self.new_label()

        end_label = self.new_label()

        self.loop_stack.append((end_label, loop_start, len(self.with_stack), False))

        self.emit_label(loop_start)

        self.visit(node.test)

        self.emit('POP_JUMP_IF_FALSE', exhaust_label)

        for stmt in node.body:

            self.visit(stmt)

        self.emit('JUMP', loop_start)

        self.emit_label(exhaust_label)

        if node.orelse:

            for stmt in node.orelse:

                self.visit(stmt)

        self.emit_label(end_label)

        self.loop_stack.pop()



    def visit_For(self, node):

        loop_start = self.new_label()

        exhaust_label = self.new_label()

        end_label = self.new_label()

        self.loop_stack.append((end_label, loop_start, len(self.with_stack), True))

        self.visit(node.iter)

        self.emit('GET_ITER', 0)

        self.emit_label(loop_start)

        self.emit('FOR_ITER', exhaust_label)

        self.visit_target(node.target)

        for stmt in node.body:

            self.visit(stmt)

        self.emit('JUMP', loop_start)

        self.emit_label(exhaust_label)

        if node.orelse:

            for stmt in node.orelse:

                self.visit(stmt)

        self.emit_label(end_label)

        self.loop_stack.pop()



    def visit_AsyncFor(self, node):

        loop_start = self.new_label()

        exhaust_label = self.new_label()

        end_label = self.new_label()

        self.loop_stack.append((end_label, loop_start, len(self.with_stack), True))

        self.visit(node.iter)

        self.emit('GET_AITER', 0)

        self.emit_label(loop_start)

        self.emit('FOR_AITER', exhaust_label)

        self.visit_target(node.target)

        for stmt in node.body:

            self.visit(stmt)

        self.emit('JUMP', loop_start)

        self.emit_label(exhaust_label)

        if node.orelse:

            for stmt in node.orelse:

                self.visit(stmt)

        self.emit_label(end_label)

        self.loop_stack.pop()



    def visit_Break(self, node):

        if self.loop_stack:

            break_label, _, with_depth, is_for_iter = self.loop_stack[-1]

            for is_async in reversed(self.with_stack[with_depth:]):

                if is_async:

                    self.emit('EXIT_ASYNC_WITH', 0)

                else:

                    self.emit('EXIT_WITH', 0)

            if is_for_iter:

                self.emit('POP_TOP', 0)

            self.emit('JUMP', break_label)



    def visit_Continue(self, node):

        if self.loop_stack:

            _, continue_label, with_depth, _ = self.loop_stack[-1]

            for is_async in reversed(self.with_stack[with_depth:]):

                if is_async:

                    self.emit('EXIT_ASYNC_WITH', 0)

                else:

                    self.emit('EXIT_WITH', 0)

            self.emit('JUMP', continue_label)



    def visit_Return(self, node):

        if node.value:

            self.visit(node.value)

        else:

            self.emit('LOAD_CONST', self.get_const_idx(None))

        self.emit('RETURN_VALUE', 0)



    def visit_Import(self, node):

        for alias in node.names:

            self.emit('LOAD_CONST', self.get_const_idx(0))

            self.emit('LOAD_CONST', self.get_const_idx(None))

            self.emit('IMPORT_NAME', self.get_name_idx(alias.name))

            if alias.asname:

                parts = alias.name.split('.')

                for p in parts[1:]:

                    self.emit('LOAD_ATTR', self.get_name_idx(p))

                self.emit('STORE_NAME', self.get_name_idx(alias.asname))

            else:

                top_pkg = alias.name.split('.')[0]

                self.emit('STORE_NAME', self.get_name_idx(top_pkg))



    def visit_ImportFrom(self, node):

        mod_name = node.module or ''

        from_list = tuple(alias.name for alias in node.names)

        self.emit('LOAD_CONST', self.get_const_idx(node.level))

        self.emit('LOAD_CONST', self.get_const_idx(from_list))

        self.emit('IMPORT_NAME', self.get_name_idx(mod_name))

        for alias in node.names:

            if alias.name == '*':

                self.emit('IMPORT_STAR', 0)

            else:

                self.emit('IMPORT_FROM', self.get_name_idx(alias.name))

                store_as = alias.asname or alias.name

                self.emit('STORE_NAME', self.get_name_idx(store_as))

        self.emit('POP_TOP', 0)



    def visit_Try(self, node):

        if node.finalbody:

            finally_except = self.new_label()

            finally_normal = self.new_label()

            self.emit('SETUP_EXCEPT', finally_except)



            if node.handlers:

                inner_except = self.new_label()

                inner_end = self.new_label()

                self.emit('SETUP_EXCEPT', inner_except)

                for stmt in node.body:

                    self.visit(stmt)

                self.emit('POP_EXCEPT', 0)

                if node.orelse:

                    for stmt in node.orelse:

                        self.visit(stmt)

                self.emit('JUMP', inner_end)



                self.emit_label(inner_except)

                for handler in node.handlers:

                    next_h = self.new_label()

                    if handler.type:

                        self.emit('DUP_TOP', 0)

                        self.visit(handler.type)

                        self.emit('COMPARE_OP', self.get_const_idx(0x3A))

                        self.emit('POP_JUMP_IF_FALSE', next_h)

                    if handler.name:

                        if handler.name in self.globals:

                            self.emit('STORE_GLOBAL', self.get_name_idx(handler.name))

                        elif handler.name in self.nonlocals:

                            self.emit('STORE_NONLOCAL', self.get_name_idx(handler.name))

                        else:

                            self.emit('STORE_NAME', self.get_name_idx(handler.name))

                    else:

                        self.emit('POP_TOP', 0)

                    for stmt in handler.body:

                        self.visit(stmt)

                    self.emit('JUMP', inner_end)

                    self.emit_label(next_h)

                self.emit('RAISE_VARARGS', 1)

                self.emit_label(inner_end)

            else:

                for stmt in node.body:

                    self.visit(stmt)

                if node.orelse:

                    for stmt in node.orelse:

                        self.visit(stmt)



            self.emit('POP_EXCEPT', 0)

            for stmt in node.finalbody:

                self.visit(stmt)

            self.emit('JUMP', finally_normal)



            self.emit_label(finally_except)

            for stmt in node.finalbody:

                self.visit(stmt)

            self.emit('RAISE_VARARGS', 1)

            self.emit_label(finally_normal)

        else:

            except_label = self.new_label()

            end_label = self.new_label()

            self.emit('SETUP_EXCEPT', except_label)

            for stmt in node.body:

                self.visit(stmt)

            self.emit('POP_EXCEPT', 0)

            if node.orelse:

                for stmt in node.orelse:

                    self.visit(stmt)

            self.emit('JUMP', end_label)



            self.emit_label(except_label)

            for handler in node.handlers:

                next_h = self.new_label()

                if handler.type:

                    self.emit('DUP_TOP', 0)

                    self.visit(handler.type)

                    self.emit('COMPARE_OP', self.get_const_idx(0x3A))

                    self.emit('POP_JUMP_IF_FALSE', next_h)

                if handler.name:

                    if handler.name in self.globals:

                        self.emit('STORE_GLOBAL', self.get_name_idx(handler.name))

                    elif handler.name in self.nonlocals:

                        self.emit('STORE_NONLOCAL', self.get_name_idx(handler.name))

                    else:

                        self.emit('STORE_NAME', self.get_name_idx(handler.name))

                else:

                    self.emit('POP_TOP', 0)

                for stmt in handler.body:

                    self.visit(stmt)

                self.emit('JUMP', end_label)

                self.emit_label(next_h)

            self.emit('RAISE_VARARGS', 1)

            self.emit_label(end_label)



    def visit_With(self, node):

        end_label = self.new_label()

        for item in node.items:

            self.visit(item.context_expr)

            self.emit('SETUP_WITH', end_label)

            self.with_stack.append(False)

            if item.optional_vars:

                self.visit_target(item.optional_vars)

            else:

                self.emit('POP_TOP', 0)

        for stmt in node.body:

            self.visit(stmt)

        for _ in node.items:

            self.emit('EXIT_WITH', 0)

            self.with_stack.pop()

        self.emit_label(end_label)



    def visit_AsyncWith(self, node):

        end_label = self.new_label()

        for item in node.items:

            self.visit(item.context_expr)

            self.emit('SETUP_ASYNC_WITH', end_label)

            self.with_stack.append(True)

            if item.optional_vars:

                self.visit_target(item.optional_vars)

            else:

                self.emit('POP_TOP', 0)

        for stmt in node.body:

            self.visit(stmt)

        for _ in node.items:

            self.emit('EXIT_ASYNC_WITH', 0)

            self.with_stack.pop()

        self.emit_label(end_label)



    def visit_Raise(self, node):

        if node.exc:

            self.visit(node.exc)

            self.emit('RAISE_VARARGS', 1)

        else:

            self.emit('RAISE_VARARGS', 0)



    def visit_Assert(self, node):

        pass_label = self.new_label()

        self.visit(node.test)

        self.emit('POP_JUMP_IF_TRUE', pass_label)

        if node.msg:

            self.visit(node.msg)

            self.emit('LOAD_NAME', self.get_name_idx('AssertionError'))

            self.emit('ROT_TWO', 0)

            self.emit('CALL_FUNC', 1)

        else:

            self.emit('LOAD_NAME', self.get_name_idx('AssertionError'))

            self.emit('CALL_FUNC', 0)

        self.emit('RAISE_VARARGS', 1)

        self.emit_label(pass_label)



    def _compile_func_def(self, node, is_async=False):

        sub_compiler = YukiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False)

        sub_code = sub_compiler.compile(ast.Module(body=node.body, type_ignores=[]))

        

        posonly_args = [a.arg for a in getattr(node.args, 'posonlyargs', [])]

        pos_args = [a.arg for a in node.args.args]

        all_pos = posonly_args + pos_args

        kwonly_args = [a.arg for a in getattr(node.args, 'kwonlyargs', [])]



        defaults_count = len(node.args.defaults)

        vararg = node.args.vararg.arg if node.args.vararg else None

        kwarg = node.args.kwarg.arg if node.args.kwarg else None



        for d in node.args.defaults:

            self.visit(d)

        self.emit('BUILD_TUPLE', defaults_count)



        kw_defs_count = 0

        for k_arg, k_def in zip(node.args.kwonlyargs, getattr(node.args, 'kw_defaults', [])):

            if k_def is not None:

                self.emit('LOAD_CONST', self.get_const_idx(k_arg.arg))

                self.visit(k_def)

                kw_defs_count += 1

        self.emit('BUILD_MAP', kw_defs_count)



        is_gen = False

        class YieldFinder(ast.NodeVisitor):

            def __init__(self):

                self.has_yield = False

            def visit_FunctionDef(self, n): pass

            def visit_AsyncFunctionDef(self, n): pass

            def visit_ClassDef(self, n): pass

            def visit_Lambda(self, n): pass

            def visit_Yield(self, n): self.has_yield = True

            def visit_YieldFrom(self, n): self.has_yield = True



        yf = YieldFinder()

        for stmt in node.body:

            yf.visit(stmt)

            if yf.has_yield:

                is_gen = True

                break



        fn_meta = {

            'name': node.name,

            'pos_args': all_pos,

            'kwonly_args': kwonly_args,

            'vararg': vararg,

            'kwarg': kwarg,

            'sub_code': sub_code,

            'is_async': is_async,

            'is_generator': is_gen

        }

        meta_idx = self.get_const_idx(fn_meta)

        self.emit('MAKE_FUNCTION', meta_idx)

        

        if node.decorator_list:

            for dec in reversed(node.decorator_list):

                self.visit(dec)

                self.emit('ROT_TWO', 0)

                self.emit('CALL_FUNC', 1)

        

        idx = self.get_name_idx(node.name)

        if node.name in self.globals:

            self.emit('STORE_GLOBAL', idx)

        elif node.name in self.nonlocals:

            self.emit('STORE_NONLOCAL', idx)

        else:

            self.emit('STORE_NAME', idx)



    def visit_FunctionDef(self, node):

        self._compile_func_def(node, is_async=False)



    def visit_AsyncFunctionDef(self, node):

        self._compile_func_def(node, is_async=True)



    def visit_Lambda(self, node):

        sub_compiler = YukiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False)

        sub_code = sub_compiler.compile(ast.Return(value=node.body))

        

        posonly_args = [a.arg for a in getattr(node.args, 'posonlyargs', [])]

        pos_args = [a.arg for a in node.args.args]

        all_pos = posonly_args + pos_args

        kwonly_args = [a.arg for a in getattr(node.args, 'kwonlyargs', [])]



        defaults_count = len(node.args.defaults)

        vararg = node.args.vararg.arg if node.args.vararg else None

        kwarg = node.args.kwarg.arg if node.args.kwarg else None



        for d in node.args.defaults:

            self.visit(d)

        self.emit('BUILD_TUPLE', defaults_count)



        kw_defs_count = 0

        for k_arg, k_def in zip(node.args.kwonlyargs, getattr(node.args, 'kw_defaults', [])):

            if k_def is not None:

                self.emit('LOAD_CONST', self.get_const_idx(k_arg.arg))

                self.visit(k_def)

                kw_defs_count += 1

        self.emit('BUILD_MAP', kw_defs_count)



        fn_meta = {

            'name': '<lambda>',

            'pos_args': all_pos,

            'kwonly_args': kwonly_args,

            'vararg': vararg,

            'kwarg': kwarg,

            'sub_code': sub_code,

            'is_async': False

        }

        meta_idx = self.get_const_idx(fn_meta)

        self.emit('MAKE_FUNCTION', meta_idx)



    def visit_ClassDef(self, node):

        sub_compiler = YukiBoostedVMCompiler(opcode_map=self.opcode_map, seed=self.seed, is_module=False, is_class=True)

        sub_code = sub_compiler.compile(ast.Module(body=node.body, type_ignores=[]))

        

        for base in node.bases:

            self.visit(base)

        self.emit('BUILD_TUPLE', len(node.bases))



        class_meta = {

            'name': node.name,

            'sub_code': sub_code

        }

        meta_idx = self.get_const_idx(class_meta)

        self.emit('MAKE_CLASS', meta_idx)

        

        if node.decorator_list:

            for dec in reversed(node.decorator_list):

                self.visit(dec)

                self.emit('ROT_TWO', 0)

                self.emit('CALL_FUNC', 1)

        

        idx = self.get_name_idx(node.name)

        if node.name in self.globals:

            self.emit('STORE_GLOBAL', idx)

        elif node.name in self.nonlocals:

            self.emit('STORE_NONLOCAL', idx)

        else:

            self.emit('STORE_NAME', idx)



    def visit_ListComp(self, node):

        self.emit('BUILD_LIST', 0)

        self._compile_list_comprehension(node.generators, 0, node.elt, depth=1)



    def visit_SetComp(self, node):

        self.emit('BUILD_SET', 0)

        self._compile_set_comprehension(node.generators, 0, node.elt, depth=1)



    def visit_DictComp(self, node):

        self.emit('BUILD_MAP', 0)

        self._compile_dict_comprehension(node.generators, 0, node.key, node.value, depth=1)



    def _compile_list_comprehension(self, generators, gen_idx, elt, depth):

        if gen_idx >= len(generators):

            self.visit(elt)

            self.emit('LIST_APPEND', depth)

            return



        gen = generators[gen_idx]

        loop_start = self.new_label()

        loop_end = self.new_label()



        self.visit(gen.iter)

        if getattr(gen, 'is_async', 0):

            self.emit('GET_AITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_AITER', loop_end)

        else:

            self.emit('GET_ITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_ITER', loop_end)

        self.visit_target(gen.target)



        skip_if = None

        if gen.ifs:

            skip_if = self.new_label()

            for condition in gen.ifs:

                self.visit(condition)

                self.emit('POP_JUMP_IF_FALSE', skip_if)



        self._compile_list_comprehension(generators, gen_idx + 1, elt, depth + 1)



        if skip_if:

            self.emit_label(skip_if)



        self.emit('JUMP', loop_start)

        self.emit_label(loop_end)



    def _compile_set_comprehension(self, generators, gen_idx, elt, depth):

        if gen_idx >= len(generators):

            self.visit(elt)

            self.emit('SET_ADD', depth)

            return



        gen = generators[gen_idx]

        loop_start = self.new_label()

        loop_end = self.new_label()



        self.visit(gen.iter)

        if getattr(gen, 'is_async', 0):

            self.emit('GET_AITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_AITER', loop_end)

        else:

            self.emit('GET_ITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_ITER', loop_end)

        self.visit_target(gen.target)



        skip_if = None

        if gen.ifs:

            skip_if = self.new_label()

            for condition in gen.ifs:

                self.visit(condition)

                self.emit('POP_JUMP_IF_FALSE', skip_if)



        self._compile_set_comprehension(generators, gen_idx + 1, elt, depth + 1)



        if skip_if:

            self.emit_label(skip_if)



        self.emit('JUMP', loop_start)

        self.emit_label(loop_end)



    def _compile_dict_comprehension(self, generators, gen_idx, key_node, val_node, depth):

        if gen_idx >= len(generators):

            self.visit(key_node)

            self.visit(val_node)

            self.emit('MAP_ADD', depth)

            return



        gen = generators[gen_idx]

        loop_start = self.new_label()

        loop_end = self.new_label()



        self.visit(gen.iter)

        if getattr(gen, 'is_async', 0):

            self.emit('GET_AITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_AITER', loop_end)

        else:

            self.emit('GET_ITER', 0)

            self.emit_label(loop_start)

            self.emit('FOR_ITER', loop_end)

        self.visit_target(gen.target)



        skip_if = None

        if gen.ifs:

            skip_if = self.new_label()

            for condition in gen.ifs:

                self.visit(condition)

                self.emit('POP_JUMP_IF_FALSE', skip_if)



        self._compile_dict_comprehension(generators, gen_idx + 1, key_node, val_node, depth + 1)



        if skip_if:

            self.emit_label(skip_if)



        self.emit('JUMP', loop_start)

        self.emit_label(loop_end)





def generate_hyper_vm_runtime(opcode_map=None):

    common_helpers = r'''

def _bin_calc(l, r, op):
    if isinstance(op, tuple) and len(op) == 3 and isinstance(op[0], tuple) and len(op[0]) == 2 and op[0][0] == '__YUKI_HVM7__':
        _tag, _val, _k = op[0][1], op[1], op[2]
        if _tag == 0x70:
            op = bytes([(b ^ ((_k + j * 7) & 0xFF)) for j, b in enumerate(_val)]).decode('utf-8', errors='ignore')
        elif _tag == 0x75:
            _dec = bytearray(); _p = _k
            for _j, _b in enumerate(_val):
                _dec.append(_b ^ ((_k + _j * 17 + _p) & 0xFF)); _p = _b
            op = _dec.decode('utf-8', errors='ignore')
        elif _tag == 0x72:
            op = _val ^ _k

    if op == 0x10 or op == '+': return l + r
    elif op == 0x11 or op == '-': return l - r
    elif op == 0x12 or op == '*': return l * r
    elif op == 0x13 or op == '/': return l / r
    elif op == 0x14 or op == '//': return l // r
    elif op == 0x15 or op == '%': return l % r
    elif op == 0x16 or op == '**': return l ** r
    elif op == 0x17 or op == '<<': return l << r
    elif op == 0x18 or op == '>>': return l >> r
    elif op == 0x19 or op == '|': return l | r
    elif op == 0x1A or op == '^': return l ^ r
    elif op == 0x1B or op == '&': return l & r
    elif op == 0x1C or op == '@': return l @ r
    return l



def _unary_calc(v, op):
    if isinstance(op, tuple) and len(op) == 3 and isinstance(op[0], tuple) and len(op[0]) == 2 and op[0][0] == '__YUKI_HVM7__':
        _tag, _val, _k = op[0][1], op[1], op[2]
        if _tag == 0x70:
            op = bytes([(b ^ ((_k + j * 7) & 0xFF)) for j, b in enumerate(_val)]).decode('utf-8', errors='ignore')
        elif _tag == 0x75:
            _dec = bytearray(); _p = _k
            for _j, _b in enumerate(_val):
                _dec.append(_b ^ ((_k + _j * 17 + _p) & 0xFF)); _p = _b
            op = _dec.decode('utf-8', errors='ignore')
        elif _tag == 0x72:
            op = _val ^ _k

    if op == 0x20 or op == '+': return +v
    elif op == 0x21 or op == '-': return -v
    elif op == 0x22 or op == 'not': return not v
    elif op == 0x23 or op == '~': return ~v
    return v



def _comp_calc(l, r, op):
    if isinstance(op, tuple) and len(op) == 3 and isinstance(op[0], tuple) and len(op[0]) == 2 and op[0][0] == '__YUKI_HVM7__':
        _tag, _val, _k = op[0][1], op[1], op[2]
        if _tag == 0x70:
            op = bytes([(b ^ ((_k + j * 7) & 0xFF)) for j, b in enumerate(_val)]).decode('utf-8', errors='ignore')
        elif _tag == 0x75:
            _dec = bytearray(); _p = _k
            for _j, _b in enumerate(_val):
                _dec.append(_b ^ ((_k + _j * 17 + _p) & 0xFF)); _p = _b
            op = _dec.decode('utf-8', errors='ignore')
        elif _tag == 0x72:
            op = _val ^ _k

    if op == 0x30 or op == '==': return l == r
    elif op == 0x31 or op == '!=': return l != r
    elif op == 0x32 or op == '<': return l < r
    elif op == 0x33 or op == '<=': return l <= r
    elif op == 0x34 or op == '>': return l > r
    elif op == 0x35 or op == '>=': return l >= r
    elif op == 0x36 or op == 'is': return l is r
    elif op == 0x37 or op == 'is not': return l is not r
    elif op == 0x38 or op == 'in': return l in r
    elif op == 0x39 or op == 'not in': return l not in r
    elif op == 0x3A or op == 'exception_match':
        if isinstance(r, tuple):
            return isinstance(l, r)
        elif isinstance(r, type) and issubclass(r, BaseException):
            return isinstance(l, r)
        return False
    return False



__HVM_P__ = __HVM_PEP__

__HVM_S__ = __HVM_SALT__



def __HVM_UNWRAP__(__d__):

    _h = __import__(__HVM_HL__)

    out = bytearray(len(__d__))

    pos = 0

    ctr = 0

    while pos < len(__d__):

        blk = _h.sha256(__HVM_P__ + __HVM_S__ + ctr.to_bytes(4, 'big')).digest()

        n = 32 if (len(__d__) - pos) > 32 else (len(__d__) - pos)

        j = 0

        while j < n:

            out[pos + j] = __d__[pos + j] ^ blk[j]

            j += 1

        pos += n

        ctr += 1

    return bytes(out)



def _vm_init(__pkg__):

    import sys, zlib

    if 'b' in __pkg__:

        return {

            'b': __pkg__['b'],

            'n': __pkg__['length'],

            's': __pkg__['seed'],

            'p': __HVM_P__,

            'e': __HVM_EP__,

            'km': __HVM_KM__,

            'ka': __HVM_KA__,

            'h': __import__(__HVM_HL__),

            'no': __HVM_NUM_OPS__,

            '_e': None,

            '_blk': b'',

            '_w': None,

            '_up': __import__('struct').unpack_from,

            '_mesh_active': ('__yuki_mesh__' in globals()),

            'tp': 0,

        }

    __seal__ = __pkg__.get('seal', None)

    if __seal__ is not None:

        import hashlib as _hl_vm

        if _hl_vm.sha256(repr(tuple(__pkg__['names'])).encode('utf-8') + repr(len(__pkg__['constants'])).encode('utf-8')).digest() != __seal__:

            try:

                import ctypes as _ct_vm; _ct_vm.memset(0, 0, 1)

            except: pass

            sys.exit(89)

    __raw_bc__ = __pkg__['bytecode']

    if (zlib.adler32(__raw_bc__) & 0xFFFFFFFF) != __pkg__['chk']:

        try:

            import ctypes; ctypes.memset(0, 0, 1)

        except: pass

        sys.exit(88)

    __bc_arr__ = bytearray(__raw_bc__)

    del __pkg__['bytecode']

    __pkg__['b'] = __bc_arr__

    return {

        'b': __bc_arr__,

        'n': __pkg__['length'],

        's': __pkg__['seed'],

        'p': __HVM_P__,

        'e': __HVM_EP__,

        'km': __HVM_KM__,

        'ka': __HVM_KA__,

        'h': __import__(__HVM_HL__),

        'no': __HVM_NUM_OPS__,

        '_e': None,

        '_blk': b'',

        '_w': None,

        '_up': __import__('struct').unpack_from,

        '_mesh_active': ('__yuki_mesh__' in globals()),

        'tp': 0,

    }



def _fetch_ins(__vmx__, __i):

    __ep = __vmx__['e']

    __eid = __i // __ep

    if __vmx__['_e'] != __eid:

        __h = __vmx__['h']

        __blk = __h.sha256(

            (__vmx__['s'] & 0xFFFFFFFFFFFFFFFF).to_bytes(8, 'big') +

            (__eid & 0xFFFFFFFF).to_bytes(4, 'big') +

            __vmx__['p'] +

            (__vmx__['km'] & 0xFFFFFFFF).to_bytes(4, 'big') +

            (__vmx__['ka'] & 0xFFFFFFFF).to_bytes(4, 'big')

        ).digest()

        __vmx__['_e'] = __eid

        __vmx__['_w'] = __vmx__['_up']('>7I', __blk, 0)

    __w0, __w1, __w2, __w3, __w4, __w5, __w6 = __vmx__['_w']

    __mix = (__w0 ^ (((__i + 1) * __w1 + __w2) & 0xFFFFFFFF)) & 0xFFFFFFFF

    __mix2 = (__w3 ^ (((__i + 3) * __w4 + __w2) & 0xFFFFFFFF)) & 0xFFFFFFFF

    __mix = (__mix ^ ((__mix2 << 7) & 0xFFFFFFFF) ^ (__mix2 >> 3)) & 0xFFFFFFFF

    __num_ops__ = __vmx__['no']

    __tp = __vmx__.get('tp', 0)

    __k_op = ((__mix & 0xFF) + __tp) % __num_ops__ if __num_ops__ else 0

    __k_arg = ((__mix2 ^ ((((__i + 1) * __w5) + __w6) & 0xFFFFFFFF)) & 0xFFFFFFFF) ^ (__tp * 0x5F3759DF)

    _ptr = __i * 5

    __b = __vmx__['b']

    __raw_op = __b[_ptr]

    __raw_arg = (__b[_ptr + 1] << 24) | (__b[_ptr + 2] << 16) | (__b[_ptr + 3] << 8) | __b[_ptr + 4]

    __real_op = (__raw_op - __k_op + __num_ops__) % __num_ops__

    __real_arg = __raw_arg ^ __k_arg

    return (__real_op, __real_arg)



def _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs):

    _f_locs = {}

    n_defs = len(_defaults)

    if n_defs > 0:

        def_start = len(_pos_args) - n_defs

        for idx, def_v in enumerate(_defaults):

            _f_locs[_pos_args[def_start + idx]] = def_v

    for k_name, k_def_val in _kw_defaults.items():

        _f_locs[k_name] = k_def_val

    for idx, a_val in enumerate(_f_args):

        if idx < len(_pos_args):

            _f_locs[_pos_args[idx]] = a_val

    if _vararg:

        _f_locs[_vararg] = tuple(_f_args[len(_pos_args):])

    if _kwarg:

        _f_locs[_kwarg] = {}

    for k_name, k_val in _f_kwargs.items():

        if k_name in _pos_args or k_name in _kwonly_args:

            _f_locs[k_name] = k_val

        elif _kwarg:

            _f_locs[_kwarg][k_name] = k_val

    return _f_locs



def _make_vm_fn(_sub_pkg, _meta, _defaults, _kw_defaults, __globs__, _parent_scope):

    _pos_args = _meta['pos_args']

    _kwonly_args = _meta.get('kwonly_args', [])

    _vararg = _meta['vararg']

    _kwarg = _meta['kwarg']

    _fn_name = _meta['name']

    _is_async = _meta.get('is_async', False)

    _is_gen = _meta.get('is_generator', False)

    if _is_async and _is_gen:

        async def _vm_generated_func(*_f_args, **_f_kwargs):

            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)

            async for item in __yuki_hypervm_agexec__(_sub_pkg, __globs__, _f_locs, _parent_scope):

                yield item

    elif _is_async:

        async def _vm_generated_func(*_f_args, **_f_kwargs):

            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)

            return await __yuki_hypervm_aexec__(_sub_pkg, __globs__, _f_locs, _parent_scope)

    elif _is_gen:

        def _vm_generated_func(*_f_args, **_f_kwargs):

            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)

            return __yuki_hypervm_gexec__(_sub_pkg, __globs__, _f_locs, _parent_scope)

    else:

        def _vm_generated_func(*_f_args, **_f_kwargs):

            _f_locs = _bind_args(_pos_args, _kwonly_args, _vararg, _kwarg, _defaults, _kw_defaults, _f_args, _f_kwargs)

            return __yuki_hypervm_exec__(_sub_pkg, __globs__, _f_locs, _parent_scope)

    _vm_generated_func.__name__ = _fn_name

    _vm_generated_func.__qualname__ = _fn_name

    _vm_generated_func.__closure_scope__ = _parent_scope

    return _vm_generated_func

'''



    loop_template = r'''__DEF_KW__ __FN_NAME__(__pkg__, __globs__=None, __locs__=None, __closure__=None):

    import sys, builtins

    if __globs__ is None:

        __globs__ = globals()

    if __locs__ is None:

        __locs__ = __globs__

    

    __consts__ = __pkg__['constants']

    __names__ = __pkg__['names']

    __vmx__ = _vm_init(__pkg__)

    _local_c_cache = {}
    _local_n_cache = {}
    _b_typ = type(abs)

    def _unmask_n(idx):
        if idx in _local_n_cache:
            return _local_n_cache[idx]
        _n = __names__[idx]
        if isinstance(_n, tuple) and len(_n) == 3 and isinstance(_n[0], tuple) and len(_n[0]) == 2 and _n[0][0] == '__YUKI_HVM7_NM__':
            _tag, _val, _k = _n[0][1], _n[1], _n[2]
            if _tag == 0x88:
                _n = bytes([(b ^ ((_k + j * 13) & 0xFF)) for j, b in enumerate(_val)]).decode('utf-8', errors='ignore')
            _local_n_cache[idx] = _n
            return _n
        _local_n_cache[idx] = _n
        return _n

    def _unmask_c(idx):
        if idx in _local_c_cache:
            return _local_c_cache[idx]
        _c = __consts__[idx]
        if isinstance(_c, tuple) and len(_c) == 3 and isinstance(_c[0], tuple) and len(_c[0]) == 2 and _c[0][0] == '__YUKI_HVM7__':
            _tag, _val, _k = _c[0][1], _c[1], _c[2]
            if _tag == 0x70:
                _c = bytes([(b ^ ((_k + j * 7) & 0xFF)) for j, b in enumerate(_val)]).decode('utf-8', errors='ignore')
            elif _tag == 0x71:
                _c = bytes([(b ^ ((_k + j * 11) & 0xFF)) for j, b in enumerate(_val)])
            elif _tag == 0x72:
                _c = _val ^ _k
            elif _tag == 0x73:
                import struct as _st_vm
                _c = _st_vm.unpack('>d', bytes([(b ^ ((_k + j * 13) & 0xFF)) for j, b in enumerate(_val)]))[0]
            elif _tag == 0x75:
                _dec = bytearray()
                _prev = _k
                for _j, _b in enumerate(_val):
                    _orig = _b ^ ((_k + _j * 17 + _prev) & 0xFF)
                    _dec.append(_orig)
                    _prev = _b
                _c = _dec.decode('utf-8', errors='ignore')
            _local_c_cache[idx] = _c
            return _c
        _local_c_cache[idx] = _c
        return _c

    __stack__ = []

    __except_stack__ = []

    __with_stack__ = []

    __pc__ = 0

    __total__ = __vmx__['n']

    __cycle__ = 0
    __check_jitter__ = 11

    _regs = [None] * 16

    _acc = None

    _chaos = 0x5F3759DF

    _t_perf_last = None
    _had_call_in_window = False
    try:
        import time as _t_vm_mod
        _t_perf_last = _t_vm_mod.perf_counter()
    except Exception: pass

    _fetch = _fetch_ins

    while __pc__ < __total__:

        __op__, __arg__ = _fetch(__vmx__, __pc__)

        __pc__ += 1

        __cycle__ += 1

        

        if __cycle__ >= __check_jitter__:
            __check_jitter__ = __cycle__ + (((__pc__ * 7 + __cycle__) & 0x0F) + 5)

            _b_typ = type(abs)

            _tampered = False

            if _fetch is not _fetch_ins:
                _tampered = True

            if len(__vmx__['b']) != __total__ * 5:
                _tampered = True

            if _t_perf_last is not None:
                try:
                    _t_now = _t_vm_mod.perf_counter()
                    if (not _had_call_in_window) and (_t_now - _t_perf_last) > 5.0:
                        _tampered = True
                    _t_perf_last = _t_now
                    _had_call_in_window = False
                except Exception: pass

            if '__pkg__' in locals() and 'seal' in __pkg__:

                import hashlib as _hl_vm

                if _hl_vm.sha256(repr(tuple(__names__)).encode('utf-8') + repr(len(__consts__)).encode('utf-8')).digest() != __pkg__['seal']:

                    _tampered = True

            _b_cur = globals().get('__builtins__')

            if _b_cur is not builtins and _b_cur is not getattr(builtins, '__dict__', None) and getattr(_b_cur, '__dict__', None) is not builtins.__dict__:

                _tampered = True

            _cur_open = getattr(builtins, 'open', None)
            if hasattr(_cur_open, '__code__') and getattr(_cur_open, '__name__', '') != 'filtered_open':
                _tampered = True

            if sys.gettrace() is not None:

                _tampered = True

            if hasattr(sys.gettrace, '__code__') or (not isinstance(sys.gettrace, _b_typ)):

                _tampered = True

            if hasattr(sys.exit, '__code__') or (not isinstance(sys.exit, _b_typ)):

                _tampered = True

            if hasattr(sys, '_getframe'):

                if hasattr(sys._getframe, '__code__') or (not isinstance(sys._getframe, _b_typ)):

                    _tampered = True

                else:

                    try:

                        _fr = sys._getframe(0)

                        if getattr(_fr, 'f_trace', None) is not None or getattr(_fr, 'f_trace_opcodes', False):

                            _tampered = True

                    except: pass

            if hasattr(sys, 'monitoring'):

                for _ti in range(6):

                    _ev = sys.monitoring.get_events(_ti)

                    _tl = sys.monitoring.get_tool(_ti)

                    if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                        _tampered = True

            if '__yuki_mesh__' in globals():

                import time as _tm_vm

                _m = globals()['__yuki_mesh__']

                _now_vm = _tm_vm.time()

                if _m.get('status', 0) != 0:

                    _tampered = True

                if abs(_now_vm - _m.get('alpha_hb', 0.0)) > 3.5:

                    _tampered = True

                if abs(_now_vm - _m.get('beta_hb', 0.0)) > 4.0:

                    _tampered = True

                _m['gamma_cycle'] = _m.get('gamma_cycle', 0) + 1

                _m['gamma_hb'] = _now_vm

            elif '__yuki_pulse__' in globals():

                import time as _tm_vm

                _pt, _ps = globals()['__yuki_pulse__']

                if abs(_tm_vm.time() - _pt) > 4.0:

                    _tampered = True

            elif __vmx__.get('_mesh_active', False):

                _tampered = True

            if _tampered:

                __vmx__['tp'] = 1

                try:

                    import ctypes as _ct_vm

                    if not hasattr(_ct_vm.memset, '__code__'):

                        _ct_vm.memset(0, 0, 1)

                except: pass

                try:

                    import os as _os_vm

                    if not hasattr(_os_vm._exit, '__code__'):

                        _os_vm._exit(95)

                except: pass



        try:

            if __op__ == 'NOP':

                pass

            elif __op__ == 'VM_CHECK':

                _b_typ = type(abs)

                _tampered = False

                if sys.gettrace() is not None or hasattr(sys.gettrace, '__code__') or (not isinstance(sys.gettrace, _b_typ)):

                    _tampered = True

                if hasattr(sys.exit, '__code__') or (not isinstance(sys.exit, _b_typ)):

                    _tampered = True

                if hasattr(sys, 'monitoring'):

                    for _ti in range(6):

                        _ev = sys.monitoring.get_events(_ti)

                        _tl = sys.monitoring.get_tool(_ti)

                        if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):

                            _tampered = True

                if _tampered:

                    __vmx__['tp'] = 1

                    try:

                        import ctypes as _ct_vm

                        if not hasattr(_ct_vm.memset, '__code__'):

                            _ct_vm.memset(0, 0, 1)

                    except: pass

                    try:

                        import os as _os_vm

                        if not hasattr(_os_vm._exit, '__code__'):

                            _os_vm._exit(95)

                    except: pass

            elif __op__ == 'LOAD_CONST':

                __stack__.append(_unmask_c(__arg__))

            elif __op__ == 'LOAD_NAME':

                nm = _unmask_n(__arg__)

                if nm in __locs__:

                    __stack__.append(__locs__[nm])

                else:

                    found = False

                    if __closure__:

                        for sc in __closure__:

                            if nm in sc:

                                __stack__.append(sc[nm])

                                found = True

                                break

                    if not found:

                        if nm in __globs__:

                            __stack__.append(__globs__[nm])

                        elif hasattr(builtins, nm):

                            __stack__.append(getattr(builtins, nm))

                        else:

                            raise NameError(f"name '{nm}' is not defined")

            elif __op__ == 'STORE_NAME':

                nm = _unmask_n(__arg__)

                val = __stack__.pop()

                __locs__[nm] = val

            elif __op__ == 'STORE_NONLOCAL':

                nm = _unmask_n(__arg__)

                val = __stack__.pop()

                found = False

                if __closure__:

                    for sc in __closure__:

                        if nm in sc:

                            sc[nm] = val

                            found = True

                            break

                if not found:

                    raise SyntaxError(f"no binding for nonlocal '{nm}' found")

            elif __op__ == 'DELETE_NAME':

                nm = _unmask_n(__arg__)

                if nm in __locs__:

                    del __locs__[nm]

                elif nm in __globs__:

                    del __globs__[nm]

                else:

                    raise NameError(f"name '{nm}' is not defined")

            elif __op__ == 'DELETE_NONLOCAL':

                nm = _unmask_n(__arg__)

                found = False

                if __closure__:

                    for sc in __closure__:

                        if nm in sc:

                            del sc[nm]

                            found = True

                            break

                if not found:

                    raise SyntaxError(f"no binding for nonlocal '{nm}' found")

            elif __op__ == 'LOAD_GLOBAL':

                nm = _unmask_n(__arg__)

                if nm in __globs__:

                    __stack__.append(__globs__[nm])

                elif hasattr(builtins, nm):

                    __stack__.append(getattr(builtins, nm))

                else:

                    raise NameError(f"name '{nm}' is not defined")

            elif __op__ == 'STORE_GLOBAL':

                nm = _unmask_n(__arg__)

                __globs__[nm] = __stack__.pop()

            elif __op__ == 'DELETE_GLOBAL':

                nm = _unmask_n(__arg__)

                if nm in __globs__:

                    del __globs__[nm]

                else:

                    raise NameError(f"name '{nm}' is not defined")

            elif __op__ == 'LOAD_ATTR':

                nm = _unmask_n(__arg__)

                obj = __stack__.pop()

                __stack__.append(getattr(obj, nm))

            elif __op__ == 'STORE_ATTR':

                nm = _unmask_n(__arg__)

                obj = __stack__.pop()

                val = __stack__.pop()

                setattr(obj, nm, val)

            elif __op__ == 'DELETE_ATTR':

                nm = _unmask_n(__arg__)

                obj = __stack__.pop()

                delattr(obj, nm)

            elif __op__ == 'LOAD_SUBSCR':

                sl = __stack__.pop()

                obj = __stack__.pop()

                __stack__.append(obj[sl])

            elif __op__ == 'STORE_SUBSCR':

                sl = __stack__.pop()

                obj = __stack__.pop()

                val = __stack__.pop()

                obj[sl] = val

            elif __op__ == 'DELETE_SUBSCR':

                sl = __stack__.pop()

                obj = __stack__.pop()

                del obj[sl]

            elif __op__ == 'BUILD_LIST':

                items = [__stack__.pop() for _ in range(__arg__)]

                items.reverse()

                __stack__.append(items)

            elif __op__ == 'BUILD_TUPLE':

                items = [__stack__.pop() for _ in range(__arg__)]

                items.reverse()

                __stack__.append(tuple(items))

            elif __op__ == 'BUILD_SET':

                items = [__stack__.pop() for _ in range(__arg__)]

                __stack__.append(set(items))

            elif __op__ == 'BUILD_MAP':

                d = {}

                pairs = []

                for _ in range(__arg__):

                    v = __stack__.pop()

                    k = __stack__.pop()

                    pairs.append((k, v))

                pairs.reverse()

                for k, v in pairs:

                    d[k] = v

                __stack__.append(d)

            elif __op__ == 'LIST_APPEND':

                val = __stack__.pop()

                target_list = __stack__[-__arg__]

                target_list.append(val)

            elif __op__ == 'LIST_EXTEND':

                seq = __stack__.pop()

                target_list = __stack__[-__arg__]

                target_list.extend(seq)

            elif __op__ == 'SET_ADD':

                val = __stack__.pop()

                target_set = __stack__[-__arg__]

                target_set.add(val)

            elif __op__ == 'SET_UPDATE':

                seq = __stack__.pop()

                target_set = __stack__[-__arg__]

                target_set.update(seq)

            elif __op__ == 'MAP_ADD':

                val = __stack__.pop()

                key = __stack__.pop()

                target_map = __stack__[-__arg__]

                target_map[key] = val

            elif __op__ == 'MAP_UPDATE':

                sub_map = __stack__.pop()

                target_map = __stack__[-__arg__]

                target_map.update(sub_map)

            elif __op__ == 'REG_STORE':

                _regs[__arg__ & 15] = __stack__.pop()

            elif __op__ == 'REG_LOAD':

                __stack__.append(_regs[__arg__ & 15])

            elif __op__ == 'REG_SWAP':

                _ridx = __arg__ & 15

                _regs[_ridx], __stack__[-1] = __stack__[-1], _regs[_ridx]

            elif __op__ == 'ACC_STORE':

                _acc = __stack__.pop()

            elif __op__ == 'ACC_LOAD':

                __stack__.append(_acc)

            elif __op__ == 'VM_JUNK_NOP':

                _chaos = (_chaos * 1103515245 + 12345 + __arg__) & 0xFFFFFFFF

            elif __op__ == 'BUILD_SLICE':

                if __arg__ == 2:

                    u = __stack__.pop()

                    l = __stack__.pop()

                    __stack__.append(slice(l, u))

                elif __arg__ == 3:

                    st = __stack__.pop()

                    u = __stack__.pop()

                    l = __stack__.pop()

                    __stack__.append(slice(l, u, st))

            elif __op__ == 'BUILD_STRING':

                parts = [str(__stack__.pop()) for _ in range(__arg__)]

                parts.reverse()

                __stack__.append(''.join(parts))

            elif __op__ == 'FORMAT_VALUE':

                conv, fmt = _unmask_c(__arg__)

                val = __stack__.pop()

                if conv == 115: val = str(val)

                elif conv == 114: val = repr(val)

                elif conv == 97: val = ascii(val)

                if fmt:

                    val = format(val, fmt)

                __stack__.append(str(val))

            elif __op__ == 'BINARY_OP':

                op_sym = _unmask_c(__arg__)

                r = __stack__.pop()

                l = __stack__.pop()

                __stack__.append(_bin_calc(l, r, op_sym))

            elif __op__ == 'UNARY_OP':

                op_sym = _unmask_c(__arg__)

                v = __stack__.pop()

                __stack__.append(_unary_calc(v, op_sym))

            elif __op__ == 'COMPARE_OP':

                op_sym = _unmask_c(__arg__)

                r = __stack__.pop()

                l = __stack__.pop()

                __stack__.append(_comp_calc(l, r, op_sym))

            elif __op__ == 'JUMP':

                __pc__ = __arg__

            elif __op__ == 'JUMP_IF_TRUE':

                if __stack__[-1]:

                    __pc__ = __arg__

            elif __op__ == 'JUMP_IF_FALSE':

                if not __stack__[-1]:

                    __pc__ = __arg__

            elif __op__ == 'POP_JUMP_IF_TRUE':

                if __stack__.pop():

                    __pc__ = __arg__

            elif __op__ == 'POP_JUMP_IF_FALSE':

                if not __stack__.pop():

                    __pc__ = __arg__

            elif __op__ == 'POP_TOP':

                __stack__.pop()

            elif __op__ == 'DUP_TOP':

                __stack__.append(__stack__[-1])

            elif __op__ == 'DUP_TOP_TWO':

                __stack__.append(__stack__[-2])

                __stack__.append(__stack__[-2])

            elif __op__ == 'ROT_TWO':

                t = __stack__[-1]

                __stack__[-1] = __stack__[-2]

                __stack__[-2] = t

            elif __op__ == 'ROT_THREE':

                a = __stack__[-1]

                b = __stack__[-2]

                c = __stack__[-3]

                __stack__[-1] = b

                __stack__[-2] = c

                __stack__[-3] = a

            elif __op__ == 'CALL_FUNC':

                args = [__stack__.pop() for _ in range(__arg__)]

                args.reverse()

                func = __stack__.pop()

                if func is super and len(args) == 0:

                    first_arg = __locs__.get('self', next(iter(list(__locs__.values())), None)) if __locs__ else None

                    cls_val = None

                    if __closure__:

                        for sc in __closure__:

                            if '__class__' in sc:

                                cls_val = sc['__class__']

                                break

                    if cls_val is not None and first_arg is not None:

                        __stack__.append(super(cls_val, first_arg))

                    else:

                        __stack__.append(super())

                else:

                    _had_call_in_window = True
                    if _t_perf_last is not None:
                        try: _t_perf_last = _t_vm_mod.perf_counter()
                        except Exception: pass

                    __stack__.append(func(*args))

            elif __op__ == 'CALL_KW':

                n_pos = __arg__ >> 16

                kw_names_idx = __arg__ & 0xFFFF

                kw_names = _unmask_c(kw_names_idx)

                kw_vals = [__stack__.pop() for _ in range(len(kw_names))]

                kw_vals.reverse()

                kwargs = dict(zip(kw_names, kw_vals))

                args = [__stack__.pop() for _ in range(n_pos)]

                args.reverse()

                func = __stack__.pop()

                _had_call_in_window = True
                if _t_perf_last is not None:
                    try: _t_perf_last = _t_vm_mod.perf_counter()
                    except Exception: pass

                __stack__.append(func(*args, **kwargs))

            elif __op__ == 'CALL_EX':

                kwargs = __stack__.pop()

                args = __stack__.pop()

                func = __stack__.pop()

                _had_call_in_window = True
                if _t_perf_last is not None:
                    try: _t_perf_last = _t_vm_mod.perf_counter()
                    except Exception: pass

                __stack__.append(func(*args, **kwargs))

__RETURN_OP__

            elif __op__ == 'GET_ITER':

                obj = __stack__.pop()

                __stack__.append(iter(obj))

            elif __op__ == 'FOR_ITER':

                it = __stack__[-1]

                try:

                    v = next(it)

                    __stack__.append(v)

                except StopIteration:

                    __stack__.pop()

                    __pc__ = __arg__

            elif __op__ == 'IMPORT_NAME':

                nm = _unmask_n(__arg__)

                from_list = __stack__.pop()

                level = __stack__.pop()

                if type(__import__) is not _b_typ or hasattr(__import__, '__code__'):
                    sys.exit(137)

                mod = __import__(nm, __globs__, __locs__, from_list, level)

                __stack__.append(mod)

            elif __op__ == 'IMPORT_FROM':

                nm = _unmask_n(__arg__)

                mod = __stack__[-1]

                __stack__.append(getattr(mod, nm))

            elif __op__ == 'IMPORT_STAR':

                mod = __stack__.pop()

                for k in getattr(mod, '__all__', [x for x in dir(mod) if not x.startswith('_')]):

                    __locs__[k] = getattr(mod, k)

            elif __op__ == 'SETUP_EXCEPT':

                __except_stack__.append((__arg__, len(__stack__), len(__with_stack__)))

            elif __op__ == 'POP_EXCEPT':

                if __except_stack__:

                    __except_stack__.pop()

            elif __op__ == 'SETUP_WITH':

                mgr = __stack__.pop()

                enter = getattr(mgr, '__enter__')

                exit_m = getattr(mgr, '__exit__')

                res = enter()

                __with_stack__.append((False, exit_m, len(__stack__), __arg__))

                __stack__.append(res)

            elif __op__ == 'EXIT_WITH':

                if __with_stack__:

                    _, exit_m, _, _ = __with_stack__.pop()

                    exit_m(None, None, None)

            elif __op__ == 'RAISE_VARARGS':

                if __arg__ == 0:

                    raise

                elif __arg__ == 1:

                    exc = __stack__.pop()

                    if isinstance(exc, type) and issubclass(exc, BaseException):

                        raise exc()

                    raise exc

            elif __op__ == 'MAKE_FUNCTION':

                meta = _unmask_c(__arg__)

                kw_defaults = __stack__.pop()

                defaults = __stack__.pop()

                if __locs__ is __globs__:

                    parent_closure = []

                else:

                    parent_closure = [__locs__] + (__closure__ or [])

                __stack__.append(_make_vm_fn(

                    meta['sub_code'], meta, defaults, kw_defaults, __globs__, parent_closure

                ))

            elif __op__ == 'MAKE_CLASS':

                meta = _unmask_c(__arg__)

                bases = __stack__.pop()

                cls_name = meta['name']

                sub_pkg = meta['sub_code']

                class_ns = {'__module__': __globs__.get('__name__', '__main__'), '__qualname__': cls_name, '__annotations__': {}}

                class_closure = [__locs__] + (__closure__ or []) if __locs__ is not __globs__ else []

                __yuki_hypervm_exec__(sub_pkg, __globs__, class_ns, class_closure)

                new_cls = type(cls_name, bases, class_ns)

                for k, v in list(class_ns.items()):

                    if hasattr(v, '__closure_scope__') and isinstance(v.__closure_scope__, list):

                        for sc in v.__closure_scope__:

                            if sc is class_ns:

                                sc['__class__'] = new_cls

                                break

                __stack__.append(new_cls)

            elif __op__ == 'UNPACK_SEQUENCE':

                seq = __stack__.pop()

                items = list(seq)

                if len(items) != __arg__:

                    raise ValueError(f"not enough values to unpack (expected {__arg__}, got {len(items)})")

                items.reverse()

                for it in items:

                    __stack__.append(it)

            elif __op__ == 'UNPACK_EX':

                _u_m = __arg__ >> 8

                _u_k = __arg__ & 0xFF

                _u_seq = list(__stack__.pop())

                if len(_u_seq) < _u_m + _u_k:

                    raise ValueError(f"not enough values to unpack (expected at least {_u_m + _u_k}, got {len(_u_seq)})")

                _u_star = _u_seq[_u_m:len(_u_seq) - _u_k] if _u_k > 0 else _u_seq[_u_m:]

                _u_after = _u_seq[len(_u_seq) - _u_k:] if _u_k > 0 else []

                _u_items = _u_seq[:_u_m] + [_u_star] + _u_after

                _u_items.reverse()

                for it in _u_items:

                    __stack__.append(it)

__ASYNC_OPS__

__YIELD_HANDLER__

        except Exception as _e:

__EXCEPT_HANDLER__

    del __stack__[:]
    try: _local_c_cache.clear()
    except Exception: pass
    _regs = [None] * 16

    return None

'''



    return_op_sync = r'''            elif __op__ == 'RETURN_VALUE':

                val = __stack__.pop()

                while __with_stack__:

                    _, exit_m, _, _ = __with_stack__.pop()

                    exit_m(None, None, None)

                del __stack__[:]
                try: _local_c_cache.clear()
                except Exception: pass
                _regs = [None] * 16

                return val'''



    return_op_async = r'''            elif __op__ == 'RETURN_VALUE':

                val = __stack__.pop()

                while __with_stack__:

                    is_aw, exit_m, _, _ = __with_stack__.pop()

                    if is_aw:

                        await exit_m(None, None, None)

                    else:

                        exit_m(None, None, None)

                del __stack__[:]
                try: _local_c_cache.clear()
                except Exception: pass
                _regs = [None] * 16

                return val'''



    async_ops_sync = r'''            elif __op__ == 'GET_AWAITABLE':

                raise RuntimeError("'await' outside async function")

            elif __op__ == 'GET_AITER':

                raise RuntimeError("'async for' outside async function")

            elif __op__ == 'FOR_AITER':

                raise RuntimeError("'async for' outside async function")

            elif __op__ == 'SETUP_ASYNC_WITH':

                raise RuntimeError("'async with' outside async function")

            elif __op__ == 'EXIT_ASYNC_WITH':

                raise RuntimeError("'async with' outside async function")'''



    async_ops_async = r'''            elif __op__ == 'GET_AWAITABLE':

                obj = __stack__.pop()

                res = await obj

                __stack__.append(res)

            elif __op__ == 'GET_AITER':

                obj = __stack__.pop()

                if hasattr(obj, '__aiter__'):

                    __stack__.append(obj.__aiter__())

                else:

                    __stack__.append(obj)

            elif __op__ == 'FOR_AITER':

                it = __stack__[-1]

                try:

                    anxt_fn = getattr(it, '__anext__')

                    v = await anxt_fn()

                    __stack__.append(v)

                except StopAsyncIteration:

                    __stack__.pop()

                    __pc__ = __arg__

            elif __op__ == 'SETUP_ASYNC_WITH':

                mgr = __stack__.pop()

                enter = getattr(mgr, '__aenter__')

                exit_m = getattr(mgr, '__aexit__')

                res = await enter()

                __with_stack__.append((True, exit_m, len(__stack__), __arg__))

                __stack__.append(res)

            elif __op__ == 'EXIT_ASYNC_WITH':

                if __with_stack__:

                    is_aw, exit_m, _, _ = __with_stack__.pop()

                    if is_aw:

                        await exit_m(None, None, None)

                    else:

                        exit_m(None, None, None)'''



    except_handler_sync = r'''            suppressed = False

            target_pc = None

            if __except_stack__:

                handler_pc, orig_stack_len, with_depth = __except_stack__.pop()

                while len(__with_stack__) > with_depth:

                    _, exit_m, saved_len, end_pc = __with_stack__.pop()

                    try:

                        if exit_m(type(_e), _e, _e.__traceback__):

                            suppressed = True

                            target_pc = end_pc

                            orig_stack_len = saved_len

                            break

                    except Exception as _exit_e:

                        _e = _exit_e

                if suppressed:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __pc__ = target_pc

                else:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __stack__.append(_e)

                    __pc__ = handler_pc

            else:

                while __with_stack__:

                    _, exit_m, saved_len, end_pc = __with_stack__.pop()

                    try:

                        if exit_m(type(_e), _e, _e.__traceback__):

                            suppressed = True

                            target_pc = end_pc

                            orig_stack_len = saved_len

                            break

                    except Exception as _exit_e:

                        _e = _exit_e

                if suppressed:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __pc__ = target_pc

                else:

                    raise _e'''



    except_handler_async = r'''            suppressed = False

            target_pc = None

            if __except_stack__:

                handler_pc, orig_stack_len, with_depth = __except_stack__.pop()

                while len(__with_stack__) > with_depth:

                    is_aw, exit_m, saved_len, end_pc = __with_stack__.pop()

                    try:

                        supp = (await exit_m(type(_e), _e, _e.__traceback__)) if is_aw else exit_m(type(_e), _e, _e.__traceback__)

                        if supp:

                            suppressed = True

                            target_pc = end_pc

                            orig_stack_len = saved_len

                            break

                    except Exception as _exit_e:

                        _e = _exit_e

                if suppressed:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __pc__ = target_pc

                else:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __stack__.append(_e)

                    __pc__ = handler_pc

            else:

                while __with_stack__:

                    is_aw, exit_m, saved_len, end_pc = __with_stack__.pop()

                    try:

                        supp = (await exit_m(type(_e), _e, _e.__traceback__)) if is_aw else exit_m(type(_e), _e, _e.__traceback__)

                        if supp:

                            suppressed = True

                            target_pc = end_pc

                            orig_stack_len = saved_len

                            break

                    except Exception as _exit_e:

                        _e = _exit_e

                if suppressed:

                    while len(__stack__) > orig_stack_len:

                        __stack__.pop()

                    __pc__ = target_pc

                else:

                    raise _e'''



    # Hide rotating keys: opaque ints/bytes, never a hex constant or key blob.

    global _YUKI_HVM_UNWRAP_FN

    try:

        _unwrap = '_' + uuid.uuid4().hex[:8]

        _pname = '_' + uuid.uuid4().hex[:8]

        _sname = '_' + uuid.uuid4().hex[:8]

        _YUKI_HVM_UNWRAP_FN = _unwrap

        common_helpers = (

            common_helpers

            .replace('__HVM_UNWRAP__', _unwrap)

            .replace('__HVM_SALT__', _yuki_opaque_bytes_expr(_YUKI_HVM_WRAP_SALT))

            .replace('__HVM_PEP__', _yuki_opaque_bytes_expr(_YUKI_HVM_PEPPER))

            .replace('__HVM_HL__', _yuki_chr_expr('hashlib'))

            .replace('__HVM_KM__', _yuki_opaque_int(_YUKI_HVM_K))

            .replace('__HVM_KA__', _yuki_opaque_int(_YUKI_HVM_K2))

            .replace('__HVM_EP__', _yuki_opaque_int(_YUKI_HVM_EPOCH))

            .replace('__HVM_NUM_OPS__', str(len(OPCODE_NAMES)))

            .replace('__HVM_P__', _pname)

            .replace('__HVM_S__', _sname)

        )

        _hvm_rnd = uuid.uuid4().hex[:5]

        common_helpers = common_helpers + f"\n_hvm_alias_{_hvm_rnd} = _fetch_ins\n"

    except Exception:

        _YUKI_HVM_UNWRAP_FN = '_hvmU'

    yield_ops_sync = r'''            elif __op__ == 'YIELD_VALUE':
                raise RuntimeError("'yield' outside generator function")'''

    yield_ops_async = r'''            elif __op__ == 'YIELD_VALUE':
                raise RuntimeError("'yield' outside generator function")'''

    yield_ops_gen = r'''            elif __op__ == 'YIELD_VALUE':
                _y_val = __stack__.pop()
                _y_sent = yield _y_val
                __stack__.append(_y_sent)'''

    return_op_gen = r'''            elif __op__ == 'RETURN_VALUE':
                val = __stack__.pop()
                while __with_stack__:
                    _, exit_m, _, _ = __with_stack__.pop()
                    exit_m(None, None, None)
                del __stack__[:]
                try: _local_c_cache.clear()
                except Exception: pass
                _regs = [None] * 16
                return val'''

    loop_sync = loop_template.replace('__DEF_KW__', 'def').replace('__FN_NAME__', '__yuki_hypervm_exec__').replace('__RETURN_OP__', return_op_sync).replace('__ASYNC_OPS__', async_ops_sync).replace('__YIELD_HANDLER__', yield_ops_sync).replace('__EXCEPT_HANDLER__', except_handler_sync)

    loop_async = loop_template.replace('__DEF_KW__', 'async def').replace('__FN_NAME__', '__yuki_hypervm_aexec__').replace('__RETURN_OP__', return_op_async).replace('__ASYNC_OPS__', async_ops_async).replace('__YIELD_HANDLER__', yield_ops_async).replace('__EXCEPT_HANDLER__', except_handler_async)

    loop_gen = loop_template.replace('__DEF_KW__', 'def').replace('__FN_NAME__', '__yuki_hypervm_gexec__').replace('__RETURN_OP__', return_op_gen).replace('__ASYNC_OPS__', async_ops_sync).replace('__YIELD_HANDLER__', yield_ops_gen).replace('__EXCEPT_HANDLER__', except_handler_sync)

    if opcode_map:

        for name, idx in opcode_map.items():

            loop_sync = loop_sync.replace(f"__op__ == '{name}'", f"__op__ == {idx}")

            loop_async = loop_async.replace(f"__op__ == '{name}'", f"__op__ == {idx}")

            loop_gen = loop_gen.replace(f"__op__ == '{name}'", f"__op__ == {idx}")

    return f"{common_helpers}\n\n{loop_sync}\n\n{loop_async}\n\n{loop_gen}\n"





# Obfuscate & Pack VM Bytecode Package into Self-Contained Executable


def generate_central_security_kernel_code(kernel_class: str, kernel_inst: str, heartbeat_secret: int) -> str:
    _r0_name = f"_YukiR0_{uuid.uuid4().hex[:6]}"
    _r1_name = f"_YukiR1_{uuid.uuid4().hex[:6]}"
    _r2_name = f"_YukiR2_{uuid.uuid4().hex[:6]}"
    _r3_name = f"_YukiR3_{uuid.uuid4().hex[:6]}"
    _om_name = f"_YukiOmega_{uuid.uuid4().hex[:6]}"
    _canary_val = random.randint(0x10000000, 0x7FFFFFFF)

    return f"""# ==============================================================================
# YUKI DECENTRALIZED FRAGMENTED RUNTIME MICROKERNEL & SECURITY SENTINEL MESH
# ==============================================================================

class {_r0_name}:
    \"\"\"Sentinel Ring 0: Hardware, Kernel Substrate & OS Environment Integrity\"\"\"

    @staticmethod
    def check_windows():
        try:
            import ctypes as _ct
            if not hasattr(_ct, 'windll') or not hasattr(_ct.windll, 'kernel32'):
                return True
            _k32 = _ct.windll.kernel32
            
            # 1. Win32 Debugger API Check
            if _k32.IsDebuggerPresent() != 0:
                return False
                
            # 2. Remote Debugger Attached Check
            _remote_dbg = _ct.c_bool(False)
            if _k32.CheckRemoteDebuggerPresent(_k32.GetCurrentProcess(), _ct.byref(_remote_dbg)) != 0:
                if _remote_dbg.value:
                    return False
            
            # 3. Direct PEB In-Memory Probing & NtQueryInformationProcess
            try:
                if hasattr(_ct.windll, 'ntdll'):
                    _ntdll = _ct.windll.ntdll
                    # Query ProcessDebugPort (class 7)
                    _dbg_port = _ct.c_size_t(0)
                    _ret_len = _ct.c_ulong(0)
                    _st = _ntdll.NtQueryInformationProcess(
                        _k32.GetCurrentProcess(),
                        7,
                        _ct.byref(_dbg_port),
                        _ct.sizeof(_dbg_port),
                        _ct.byref(_ret_len)
                    )
                    if _st == 0 and _dbg_port.value != 0:
                        return False
                        
                    # Query ProcessDebugObjectHandle (class 0x1E)
                    _dbg_obj = _ct.c_size_t(0)
                    _st3 = _ntdll.NtQueryInformationProcess(
                        _k32.GetCurrentProcess(),
                        0x1E,
                        _ct.byref(_dbg_obj),
                        _ct.sizeof(_dbg_obj),
                        _ct.byref(_ret_len)
                    )
                    if _st3 == 0 and _dbg_obj.value != 0:
                        return False
            except Exception: pass
            
            # 4. Hardware Breakpoint Verification (Dr0 - Dr7)
            try:
                _is_64bit = (_ct.sizeof(_ct.c_void_p) == 8)
                if _is_64bit:
                    class _CONTEXT64(_ct.Structure):
                        _fields_ = [
                            ('P1Home', _ct.c_ulonglong), ('P2Home', _ct.c_ulonglong),
                            ('P3Home', _ct.c_ulonglong), ('P4Home', _ct.c_ulonglong),
                            ('P5Home', _ct.c_ulonglong), ('P6Home', _ct.c_ulonglong),
                            ('ContextFlags', _ct.c_ulong), ('MxCsr', _ct.c_ulong),
                            ('SegCs', _ct.c_ushort), ('SegDs', _ct.c_ushort),
                            ('SegEs', _ct.c_ushort), ('SegFs', _ct.c_ushort),
                            ('SegGs', _ct.c_ushort), ('SegSs', _ct.c_ushort),
                            ('EFlags', _ct.c_ulong),
                            ('Dr0', _ct.c_ulonglong), ('Dr1', _ct.c_ulonglong),
                            ('Dr2', _ct.c_ulonglong), ('Dr3', _ct.c_ulonglong),
                            ('Dr6', _ct.c_ulonglong), ('Dr7', _ct.c_ulonglong),
                            ('Rax', _ct.c_ulonglong), ('Rcx', _ct.c_ulonglong),
                            ('Rdx', _ct.c_ulonglong), ('Rbx', _ct.c_ulonglong),
                            ('Rsp', _ct.c_ulonglong), ('Rbp', _ct.c_ulonglong),
                            ('Rsi', _ct.c_ulonglong), ('Rdi', _ct.c_ulonglong),
                            ('R8', _ct.c_ulonglong), ('R9', _ct.c_ulonglong),
                            ('R10', _ct.c_ulonglong), ('R11', _ct.c_ulonglong),
                            ('R12', _ct.c_ulonglong), ('R13', _ct.c_ulonglong),
                            ('R14', _ct.c_ulonglong), ('R15', _ct.c_ulonglong),
                            ('Rip', _ct.c_ulonglong),
                        ]
                    _ctx = _CONTEXT64()
                    _ctx.ContextFlags = 0x100010
                    if _k32.GetThreadContext(_k32.GetCurrentThread(), _ct.byref(_ctx)) != 0:
                        if _ctx.Dr0 != 0 or _ctx.Dr1 != 0 or _ctx.Dr2 != 0 or _ctx.Dr3 != 0:
                            return False
                        if (_ctx.Dr7 & 0xF) != 0:
                            return False
            except Exception: pass
            
            # 5. Injected Reversing Foreign DLLs Check (Frida, Scylla, Cheat Engine, x64dbg)
            try:
                _bad_dlls = (
                    'frida-agent', 'frida-gadget', 'scylla', 'cheatengine',
                    'x64dbg', 'x32dbg', 'vehdebug', 'speedhack', 'pydumper'
                )
                for _bd in _bad_dlls:
                    if _k32.GetModuleHandleW(_bd) != 0:
                        return False
            except Exception: pass
            
        except Exception: pass
        return True

    @staticmethod
    def check_linux_android():
        try:
            import os as _o
            # 1. TracerPid check via /proc/self/status
            if _o.path.exists('/proc/self/status'):
                try:
                    with open('/proc/self/status', 'r', encoding='utf-8', errors='ignore') as _f:
                        for _l in _f:
                            if _l.startswith('TracerPid:'):
                                if int(_l.split(':')[1].strip()) != 0:
                                    return False
                except Exception: pass

            # 2. Waiting channel inspection (/proc/self/wchan)
            if _o.path.exists('/proc/self/wchan'):
                try:
                    with open('/proc/self/wchan', 'r', encoding='utf-8', errors='ignore') as _f:
                        _w = _f.read().strip()
                        if 'ptrace' in _w or 'sys_ptrace' in _w:
                            return False
                except Exception: pass

            # 3. Scan foreign injected libraries in /proc/self/maps
            if _o.path.exists('/proc/self/maps'):
                try:
                    _bad_libs = ('frida', 'substrate', 'xposed', 'gum-js', 'libmem')
                    with open('/proc/self/maps', 'r', encoding='utf-8', errors='ignore') as _f:
                        for _l in _f:
                            _l_low = _l.lower()
                            if any(_b in _l_low for _b in _bad_libs):
                                return False
                except Exception: pass

            # 4. Parent process inspect (/proc/ppid/cmdline)
            try:
                _ppid = _o.getppid()
                _ppath = '/proc/' + str(_ppid) + '/cmdline'
                if _o.path.exists(_ppath):
                    with open(_ppath, 'rb') as _f:
                        _pcmd = _f.read().decode('utf-8', errors='ignore').lower()
                        if any(_d in _pcmd for _d in ('gdb', 'lldb', 'strace', 'ltrace', 'frida', 'radare2', 'r2')):
                            return False
            except Exception: pass
            
        except Exception: pass
        return True

    @staticmethod
    def check_timing_jitter():
        try:
            import time as _tm
            _t0 = _tm.perf_counter_ns()
            _acc = 0
            for _i in range(150):
                _acc = (_acc * 31 + _i) & 0xFFFFFF
            _t1 = _tm.perf_counter_ns()
            if (_t1 - _t0) > 50000000:
                return False
        except Exception: pass
        return True

    @classmethod
    def verify(cls):
        if not cls.check_windows():
            return False
        if not cls.check_linux_android():
            return False
        if not cls.check_timing_jitter():
            return False
        return True


class {_r1_name}:
    \"\"\"Sentinel Ring 1: CPython Virtual Machine Purity & Call Frame Introspection\"\"\"

    @staticmethod
    def check_c_builtin_purity():
        import sys as _s, marshal as _m, builtins as _bi
        _b_typ = type(abs)
        
        _core_builtins = [
            _m.loads, _m.dumps, exec, eval, compile, getattr, setattr, hasattr,
            __import__, _s.gettrace, _s.exit, open, id, isinstance, hash, len
        ]
        if hasattr(_s, 'settrace'): _core_builtins.append(_s.settrace)
        if hasattr(_s, 'setprofile'): _core_builtins.append(_s.setprofile)
        if hasattr(_s, 'addaudithook'): _core_builtins.append(_s.addaudithook)
        for _fn in _core_builtins:
            if _fn is open and getattr(_fn, '__name__', '') == 'filtered_open':
                continue
            if hasattr(_fn, '__code__') or hasattr(_fn, '__closure__') or hasattr(_fn, '__dict__'):
                return False
            if not isinstance(_fn, _b_typ):
                return False

        # Module Namespace Integrity Lock
        if _s.modules.get('builtins') is not _bi:
            return False
        if _s.modules.get('sys') is not _s:
            return False
        if _s.modules.get('marshal') is not _m:
            return False

        try:
            import os as _o
            if hasattr(_o, '_exit'):
                if hasattr(_o._exit, '__code__') or not isinstance(_o._exit, _b_typ):
                    return False
        except Exception: pass
        return True

    @staticmethod
    def check_trace_and_frames():
        import sys as _s
        if _s.gettrace() is not None:
            return False
        if hasattr(_s, 'getprofile') and _s.getprofile() is not None:
            return False

        _bad_files = ('bdb.py', 'pdb.py', 'pydevd', 'debugpy', 'pycdc', 'ida_', 'ghidra_', 'pylingual')
        _bad_locals = ('__debugger_state__', 'pydev_step', 'set_trace', 'post_mortem')
        
        if hasattr(_s, '_current_frames'):
            try:
                for _fr in _s._current_frames().values():
                    _cur = _fr
                    while _cur:
                        if getattr(_cur, 'f_trace', None) is not None or getattr(_cur, 'f_trace_opcodes', False):
                            return False
                        _co_name = getattr(_cur.f_code, 'co_filename', '') or ''
                        _co_low = _co_name.lower()
                        if any(_bf in _co_low for _bf in _bad_files):
                            return False
                        _locs = getattr(_cur, 'f_locals', None)
                        if isinstance(_locs, dict):
                            if any(_bl in _locs for _bl in _bad_locals):
                                return False
                        _cur = _cur.f_back
            except Exception: pass
        return True

    @staticmethod
    def check_monitoring():
        import sys as _s
        if hasattr(_s, 'monitoring'):
            try:
                for _ti in range(6):
                    _ev = _s.monitoring.get_events(_ti)
                    _tl = _s.monitoring.get_tool(_ti)
                    if _ev != 0 or (_tl is not None and not str(_tl).startswith('yuki_')):
                        return False
            except Exception: pass
        return True

    @staticmethod
    def check_native_c_api_hooks():
        try:
            import ctypes as _ct
            _pyapi = getattr(_ct, 'pythonapi', None)
            if not _pyapi:
                return True
            _targets = (
                'PyMarshal_ReadObjectFromString',
                'PyMarshal_WriteObjectToString',
                'PyEval_EvalCode',
                'PyRun_StringFlags',
                'PyObject_Call'
            )
            for _sym in _targets:
                try:
                    _fn_ptr = getattr(_pyapi, _sym, None)
                    if not _fn_ptr:
                        continue
                    _addr = _ct.cast(_fn_ptr, _ct.c_void_p).value
                    if not _addr:
                        continue
                    _buf = (_ct.c_ubyte * 16).from_address(_addr)
                    _b = bytes(_buf)
                    if not _b or len(_b) < 2:
                        continue
                    if _b[0] in (0xE9, 0xEB, 0xCC, 0xC3, 0xC2):
                        return False
                    if _b[0] == 0xFF and (_b[1] in (0x25, 0xE0, 0xE1, 0xE2, 0xE3, 0xE4)):
                        return False
                    if _b[0] == 0x48 and _b[1] == 0xB8:
                        return False
                    if _b[0] == 0x90 and _b[1] == 0x90 and _b[2] == 0x90:
                        return False
                    if len(_b) >= 4 and (_b[0] == 0x50 and _b[1] == 0x00 and _b[2] == 0x00 and _b[3] == 0x58):
                        return False
                    if len(_b) >= 4 and (_b[0] == 0x00 and _b[1] == 0x00 and _b[2] == 0x20 and _b[3] == 0xD4):
                        return False
                except Exception: pass
        except Exception: pass
        return True

    @classmethod
    def verify(cls):
        if not cls.check_c_builtin_purity():
            return False
        if not cls.check_native_c_api_hooks():
            return False
        if not cls.check_trace_and_frames():
            return False
        if not cls.check_monitoring():
            return False
        return True


class {_r2_name}:
    \"\"\"Sentinel Ring 2: Dynamic Anti-Hooking, Importer & In-Memory Code Integrity\"\"\"

    _script_path = None
    _script_hash = None
    _script_size = None
    _script_file_obj = None

    @classmethod
    def init_file_guard(cls):
        try:
            import sys as _s, os as _o, hashlib as _hl
            _tp = (getattr(_s.modules.get('__main__'), '__file__', None) or 
                   (_s.argv[0] if _s.argv else None) or 
                   globals().get('__file__'))
            if _tp and _o.path.exists(_tp):
                cls._script_path = _o.path.abspath(_tp)
                with open(cls._script_path, 'rb') as _f:
                    _content = _f.read()
                cls._script_size = len(_content)
                cls._script_hash = _hl.sha256(_content).digest()
                if b'khangcoder' not in _content or b'61593602324700' not in _content:
                    return False
                try:
                    cls._script_file_obj = open(cls._script_path, 'rb')
                except Exception: pass
                return True
        except Exception: pass
        return True

    @classmethod
    def check_file_integrity(cls):
        try:
            import os as _o, hashlib as _hl
            if not cls._script_path or not cls._script_hash:
                return True
            if not _o.path.exists(cls._script_path):
                return False
            if _o.path.getsize(cls._script_path) != cls._script_size:
                return False
            with open(cls._script_path, 'rb') as _f:
                if _hl.sha256(_f.read()).digest() != cls._script_hash:
                    return False
        except Exception:
            return False
        return True

    _BAD_MODULES = (
        'pdb', 'debugpy', 'pydevd', 'pydev', 'pylingual', 'pycdc', 'decompyle',
        'uncompyle', 'xdis', 'frida', 'ropper', 'radare2', 'r2pipe', 'capstone',
        'keystone', 'angr', 'triton', 'z3', 'ptrace', 'memory_profiler', 'trace'
    )

    @classmethod
    def check_sys_modules(cls):
        import sys as _s
        for _m in list(_s.modules.keys()):
            _m_low = _m.lower()
            for _b in cls._BAD_MODULES:
                if _m_low == _b or _m_low.startswith(_b + '.') or ('.' + _b) in _m_low:
                    return False
        return True

    @staticmethod
    def check_meta_path():
        import sys as _s
        if hasattr(_s, 'meta_path'):
            _bad_hooks = ('dump', 'hook', 'spy', 'patch', 'intercept', 'sniff', 'snoop')
            for _finder in _s.meta_path:
                _name = (getattr(_finder, '__name__', '') or _finder.__class__.__name__).lower()
                if any(_bh in _name for _bh in _bad_hooks):
                    return False
        return True

    @staticmethod
    def check_code_hash(func, expected_digest):
        if not func or not expected_digest:
            return True
        try:
            import hashlib as _hl
            if hasattr(func, '__code__') and hasattr(func.__code__, 'co_code'):
                if _hl.sha256(func.__code__.co_code).digest() != expected_digest:
                    return False
        except Exception:
            return False
        return True

    @classmethod
    def verify(cls, monitored_func=None, expected_hash=None):
        if not cls.check_sys_modules():
            return False
        if not cls.check_meta_path():
            return False
        if not cls.check_file_integrity():
            return False
        if monitored_func and expected_hash:
            if not cls.check_code_hash(monitored_func, expected_hash):
                return False
        return True


class {_om_name}:
    \"\"\"Sentinel Omega: Low-Level Suicide Executioner & Memory Scrubber\"\"\"

    @staticmethod
    def wipe_buffers(*buffers):
        try:
            for _b in buffers:
                if isinstance(_b, bytearray):
                    _b[:] = b'\\x00' * len(_b)
                elif isinstance(_b, dict):
                    _b.clear()
                elif isinstance(_b, list):
                    _b.clear()
        except Exception: pass

    @classmethod
    def execute_purge(cls, code=137):
        try:
            globals()['__yuki_pulse__'] = (0.0, 0)
        except Exception: pass
        if '__yuki_mesh__' in globals():
            try:
                globals()['__yuki_mesh__']['status'] = 0xDEAD
            except Exception: pass
            
        try:
            import os as _o, subprocess as _sp
            if _o.name == 'nt':
                _sp.Popen(['mshta', 'vbscript:msgbox("CANH BAO: FILE DA BI SUA DOI (FILE TAMPERED)! ANTI BY khangcoder & thao my coder",16,"Security Sentinel")(window.close)'])
        except Exception: pass
            
        try:
            import ctypes as _ct
            if hasattr(_ct, 'memset') and not hasattr(_ct.memset, '__code__'):
                _ct.memset(0, 0, 1)
        except Exception: pass
        
        try:
            import os as _o
            if hasattr(_o, '_exit') and not hasattr(_o._exit, '__code__'):
                _o._exit(code)
        except Exception: pass
        
        try:
            import os as _o
            if hasattr(_o, 'kill') and hasattr(_o, 'getpid'):
                _o.kill(_o.getpid(), 9)
        except Exception: pass
        
        try:
            import sys as _s
            _s.exit(137)
        except Exception: pass


class {_r3_name}:
    \"\"\"Sentinel Ring 3: Decentralized Multi-Thread Cross-Interlock Mesh\"\"\"

    def __init__(self, secret: int, monitored_func=None, expected_hash=None):
        import time as _tm, threading as _th
        self._secret = secret
        self._monitored_func = monitored_func
        self._expected_hash = expected_hash
        self._active = True
        self._lock = _th.Lock()
        
        self._alpha_lfsr = {random.randint(0x10000000, 0x7FFFFFFF)}
        self._beta_lfsr = {random.randint(0x10000000, 0x7FFFFFFF)}
        self._alpha_hb = _tm.time()
        self._beta_hb = _tm.time()
        
        globals()['__yuki_mesh__'] = dict(
            alpha_hb=self._alpha_hb,
            alpha_token=self._alpha_lfsr ^ self._secret,
            beta_hb=self._beta_hb,
            beta_token=self._beta_lfsr ^ self._secret,
            gamma_hb=_tm.time(),
            gamma_cycle=0,
            status=0,
            secret=self._secret
        )
        globals()['__yuki_pulse__'] = (self._alpha_hb, self._alpha_lfsr ^ self._secret)

    def _alpha_worker(self):
        import time as _tm
        while self._active:
            try:
                if not {_r0_name}.verify():
                    {_om_name}.execute_purge()
                if not {_r1_name}.verify():
                    {_om_name}.execute_purge()
                if not {_r2_name}.verify(self._monitored_func, self._expected_hash):
                    {_om_name}.execute_purge()

                with self._lock:
                    self._alpha_hb = _tm.time()
                    self._alpha_lfsr = ((self._alpha_lfsr * 1103515245) + 12345) & 0x7FFFFFFF
                    _tok = self._alpha_lfsr ^ self._secret
                    globals()['__yuki_mesh__']['alpha_hb'] = self._alpha_hb
                    globals()['__yuki_mesh__']['alpha_token'] = _tok
                    globals()['__yuki_pulse__'] = (self._alpha_hb, _tok)
            except Exception: pass
            _tm.sleep(0.35)

    def _beta_worker(self):
        import time as _tm
        while self._active:
            try:
                _tm.sleep(0.55)
                _now = _tm.time()
                self._beta_hb = _now
                
                if abs(_now - self._alpha_hb) > 3.0:
                    {_om_name}.execute_purge()
                    
                if not {_r1_name}.check_trace_and_frames():
                    {_om_name}.execute_purge()
                    
                if not {_r1_name}.check_native_c_api_hooks():
                    {_om_name}.execute_purge()
                    
                if not {_r0_name}.check_windows():
                    {_om_name}.execute_purge()
                    
                if not {_r0_name}.check_linux_android():
                    {_om_name}.execute_purge()
                    
                if not {_r2_name}.check_sys_modules():
                    {_om_name}.execute_purge()
                    
                if not {_r2_name}.check_file_integrity():
                    {_om_name}.execute_purge()
                    
                with self._lock:
                    self._beta_lfsr = ((self._beta_lfsr * 214013) + 2531011) & 0x7FFFFFFF
                    _tok_beta = self._beta_lfsr ^ self._secret
                    globals()['__yuki_mesh__']['beta_hb'] = self._beta_hb
                    globals()['__yuki_mesh__']['beta_token'] = _tok_beta
            except Exception: pass

    def start_sentinels(self):
        import threading as _th
        _t_a = _th.Thread(target=self._alpha_worker, daemon=True, name=\"_YukiKrnAlpha\")
        _t_a.start()
        _t_b = _th.Thread(target=self._beta_worker, daemon=True, name=\"_YukiKrnBeta\")
        _t_b.start()


class {kernel_class}:
    \"\"\"Yuki Decentralized Security Microkernel Controller\"\"\"
    _instance = None

    def __init__(self):
        self._secret = {heartbeat_secret}
        self._monitored_func = None
        self._expected_hash = None
        self._mesh = None
        self._compromised = False
        self._canary = {_canary_val}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = {kernel_class}()
        return cls._instance

    def _silent_die(self, code=137):
        self._compromised = True
        {_om_name}.execute_purge(code)

    def register_vm_func(self, func):
        try:
            import hashlib as _hl
            if hasattr(func, '__code__') and hasattr(func.__code__, 'co_code'):
                self._monitored_func = func
                self._expected_hash = _hl.sha256(func.__code__.co_code).digest()
        except Exception: pass

    def verify_all_rings(self):
        if self._compromised:
            return False
        if not {_r0_name}.verify():
            return False
        if not {_r1_name}.verify():
            return False
        if not {_r2_name}.verify(self._monitored_func, self._expected_hash):
            return False
        return True

    def boot(self, vm_func=None):
        if vm_func:
            self.register_vm_func(vm_func)
            
        if not {_r2_name}.init_file_guard():
            self._silent_die()

        if not self.verify_all_rings():
            self._silent_die()

        self._mesh = {_r3_name}(
            secret=self._secret,
            monitored_func=self._monitored_func,
            expected_hash=self._expected_hash
        )
        self._mesh.start_sentinels()

        try:
            import sys as _s
            if hasattr(_s, 'addaudithook'):
                def _audit_guard(event, args):
                    if any(x in event for x in ('cpython.run_command', 'pdb.Pdb', 'sys.settrace', 'sys.setprofile', 'cpython._PySys_ClearAuditHooks')):
                        self._silent_die()
                _s.addaudithook(_audit_guard)
        except Exception: pass

        return self

    def guard_exec(self, _func, *_args, **_kwargs):
        if self._compromised or not self.verify_all_rings():
            self._silent_die()
        try:
            return _func(*_args, **_kwargs)
        finally:
            try:
                import gc as _gc
                _gc.collect()
            except Exception: pass

    @staticmethod
    def wipe_memory(*_buffers):
        {_om_name}.wipe_buffers(*_buffers)
"""



def build_hyper_vm_payload(source_code: str):

    # Fresh hidden keys every build so a leaked output cannot unlock the next one.

    _yuki_refresh_hvm_secrets()

    # FIX BUG #5/#18: fragmented blobs + random names + indirect imports + sha256 integrity.

    shuffled_opcodes = list(OPCODE_NAMES)

    random.shuffle(shuffled_opcodes)

    opcode_map = {name: idx for idx, name in enumerate(shuffled_opcodes)}



    try:

        _tree = ast.parse(source_code)

        LocalVarRenamer(_tree).visit(_tree)

        ast.fix_missing_locations(_tree)

        source_code = ast.unparse(_tree)

    except Exception:

        pass



    compiler = YukiBoostedVMCompiler(opcode_map=opcode_map)

    vm_pkg = compiler.compile(source_code)



    marshaled = marshal.dumps(vm_pkg)

    compressed = zlib.compress(lzma.compress(marshaled), 9)

    _hvm_digest = _yuki_sha256(compressed)



    # SHA256-CTR wrap: keystream rotates every 32 bytes. No XOR key blob in output.

    xored = _yuki_hvm_ctr_xor(compressed, _YUKI_HVM_PEPPER, _YUKI_HVM_WRAP_SALT)



    runtime_str = generate_hyper_vm_runtime(opcode_map)

    _unwrap = _YUKI_HVM_UNWRAP_FN



    # fragment ciphertext only (never emit the wrap key)

    _d_expr = _yuki_b85_frag_expr(xored)

    _fn = f'__yuki_launch_hypervm_{uuid.uuid4().hex[:5]}__'

    _vd = '_d' + uuid.uuid4().hex[:5]

    _ve = '_e' + uuid.uuid4().hex[:5]

    _vp = '_p' + uuid.uuid4().hex[:5]

    _imp_b64 = _yuki_chr_expr('base64')

    _imp_z = _yuki_chr_expr('zlib')

    _imp_lz = _yuki_chr_expr('lzma')

    _imp_m = _yuki_chr_expr('marshal')

    _imp_h = _yuki_chr_expr('hashlib')

    _h1, _h2 = _hvm_digest[:32], _hvm_digest[32:]

    _krn_cls = f"__YukiKrn_{uuid.uuid4().hex[:6]}__"
    _krn_inst = f"__krn_{uuid.uuid4().hex[:6]}__"
    _krn_code = generate_central_security_kernel_code(_krn_cls, _krn_inst, _YUKI_HEARTBEAT_SECRET)

    loader_src = f"""# ==================== YUKI HYPER-VM ENGINE V8.0 QUANTUM SHIELD ====================
import os as _yuki_env_os, sys as _yuki_env_sys
for _e in ('PYTHONSTARTUP', 'PYTHONINSPECT', 'PYTHONBREAKPOINT', 'PYTHONDEBUG', 'PYTHONPROFILEIMPORT', 'PYTHONTRACE'):
    if _e in _yuki_env_os.environ:
        del _yuki_env_os.environ[_e]
if hasattr(_yuki_env_sys, 'breakpointhook'):
    _yuki_env_sys.breakpointhook = lambda *a, **k: None
for _m in ('pdb', 'ipdb', 'pydevd', 'debugpy', 'ptvsd', 'frida', 'r2pipe'):
    if _m in _yuki_env_sys.modules:
        _yuki_env_sys.exit(137)
if 'sitecustomize' in _yuki_env_sys.modules:
    try:
        _mod = _yuki_env_sys.modules['sitecustomize']
        if hasattr(_mod, '__file__') and _mod.__file__:
            _fp = _yuki_env_os.path.abspath(_mod.__file__)
            if _fp.startswith(_yuki_env_os.path.abspath(_yuki_env_sys.path[0] if _yuki_env_sys.path else '')):
                _yuki_env_sys.exit(137)
    except Exception: pass
if 'usercustomize' in _yuki_env_sys.modules:
    try:
        _mod = _yuki_env_sys.modules['usercustomize']
        if hasattr(_mod, '__file__') and _mod.__file__:
            _fp = _yuki_env_os.path.abspath(_mod.__file__)
            if _fp.startswith(_yuki_env_os.path.abspath(_yuki_env_sys.path[0] if _yuki_env_sys.path else '')):
                _yuki_env_sys.exit(137)
    except Exception: pass

def _yuki_cff_gadget_anchor():
    for _ in (0,):
        try:
            try:
                if 1 == 2: raise StopIteration
            finally: break
        except Exception: pass
        finally: pass
_yuki_cff_gadget_anchor()

{runtime_str}

{_krn_code}

{_krn_inst} = {_krn_cls}.get_instance().boot(__yuki_hypervm_exec__)



def {_fn}():

    import gc as _gc_hvm

    if _gc_hvm.isenabled():

        try: _gc_hvm.disable()

        except: pass

    {_vd}=(__import__({_imp_b64}).b85decode({_d_expr}))

    {_ve}={_unwrap}({_vd})

    del {_vd}

    assert __import__({_imp_h}).sha256({_ve}).hexdigest()==({_h1!r}+{_h2!r}),'hvm-integrity'

    (lambda: (
        __import__('sys').exit(137) if __import__('sys').gettrace() is not None else None,
        __import__('sys').exit(137) if (hasattr(__import__('hashlib').sha256, '__code__') or type(__import__('hashlib').sha256) is not type(abs)) else None,
        __import__('sys').exit(137) if hasattr(__import__('marshal').loads, '__code__') else None
    ))()
    _raw_buf = __import__({_imp_lz}).decompress(__import__({_imp_z}).decompress({_ve}))
    try:
        _ct = __import__('ctypes')
        _papi_m = getattr(getattr(_ct, 'pythonapi', None), 'PyMarshal_ReadObjectFromString', None)
        if _papi_m:
            _papi_m.restype = getattr(_ct, 'py_object')
            _papi_m.argtypes = [getattr(_ct, 'c_char_p'), getattr(_ct, 'c_ssize_t')]
            {_vp} = _papi_m(_raw_buf, len(_raw_buf))
        else:
            {_vp} = __import__({_imp_m}).loads(_raw_buf)
    except Exception:
        {_vp} = __import__({_imp_m}).loads(_raw_buf)
    del _raw_buf

    del {_ve}

    try:

        return {_krn_inst}.guard_exec(__yuki_hypervm_exec__, {_vp}, globals(), globals())

    finally:

        try:

            {_krn_cls}.wipe_memory({_vp}.get('b'))

            {_vp}.clear()

            del {_vp}

        except: pass

        try:

            if _gc_hvm.isenabled() == False:

                _gc_hvm.enable()

        except: pass



{_fn}()

"""


    return loader_src



def main():

    global _YUKI_STR_MACHINE_ID, _YUKI_STR_MACHINE_V5_ID, _YUKI_STR_MACHINE_V6_ID

    _yuki_refresh_hvm_secrets()

    _YUKI_STR_MACHINE_ID = f"__Yuki_StrMachine_{uuid.uuid4().hex[:8]}__"

    _YUKI_STR_MACHINE_V5_ID = f"__Yuki_StrM5_{uuid.uuid4().hex[:8]}__"

    _YUKI_STR_MACHINE_V6_ID = f"__Yuki_StrM6_{uuid.uuid4().hex[:8]}__"

    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f"\n >> Version --> [{ver}] <<"))

    while True:

        file_name = input(stage(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Enter File: "))).strip(' "\'')

        try:

            with open(file_name, "r", encoding="utf-8") as f:

                code = f.read()

            break

        except FileNotFoundError:

            print(Colorate.Horizontal(Colors.red_to_white, "File Not Found."))

    _runsource = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Type File: [0-FULL ACTIVE CỰC ĐỊA | 1-Main | 2-Exec | 3-Import]: "))).lower()

    if _runsource in ('0', 'full', 'max', 'super'):
        _runsource = '1'
        vm_virtualize = True
        cff_flatten = True
        moreobf = True
        _obf_ = '6'
        hide_builtins = 'y'
        anti_debug = True
        anti_crack = True
        rename_vars = True
        reverse = 'y'
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> ⚡ [FULL ACTIVE CỰC ĐỊA KÍCH HOẠT] Toàn bộ 10/10 tầng phòng ngự tối cao đã bật! <<"))
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> [HyperVM v7.0 + String Machine V6 (Quantum MBA) + CFF + Anti-Crack + Multi-Ring Sentinels] <<"))
    else:
        vm_virtualize = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "HyperVM Virtualization (Custom Bytecode Virtual Machine)? [y] Yes | [n] No: "))).lower() != 'n' else False

        cff_flatten = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Control Flow Flattening (Làm phẳng luồng điều khiển, ma trận State Machine)? [y] Yes | [n] No: "))).lower() != 'n' else False

        moreobf = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "More OBF? [y] Yes | [n] No: "))).lower() != 'n' else False

        _obf_ = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),"OBF-String? [y] V1 | [n] V2 | [x] V3 | [v] V4 | [5] V5 | [6] V6 (Quantum MBA String VM): "))).lower()

        hide_builtins = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Hide-Builtins? [y] V1 | [n] V2: "))).lower()

        anti_debug = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Anti-Debug? [y] Yes | [n] No: "))).lower() != 'n' else False

        anti_crack = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Anti Crack, Anti-Crack Requests Lib? [y] Yes | [n] No: "))).lower() != 'n' else False

        rename_vars = True if input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "More String? [y] Yes | [n] No: "))).lower() != 'n' else False

        reverse = input(stage2(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), "Do you want to increase the difficulty of the Obf? [y] V1 | [n] V2: "))).lower()

    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--------------------------------------'))

    print(stage3(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), 'Starting...')))

    # === THUẬT TOÁN 1 (từ pyobfus): MBA NUMERIC & CONSTANT TRANSMUTATION ===
    try:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '>> [MBA Numeric Transmutation] Biến đổi toàn bộ số nguyên & số thực thành toán tử bitwise <<'))
        _num_tree = ast.parse(code)
        _num_tree = YukiNumericObfuscator().transform(_num_tree)
        ast.fix_missing_locations(_num_tree)
        code = ast.unparse(_num_tree)
    except Exception:
        pass

    # === THUẬT TOÁN 2 (từ adversarial-obfuscator): ANTI-AI REASONING LOOPS ===
    try:
        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '>> [Anti-AI Reasoning Traps] Cấy bẫy vòng lặp suy luận đệ quy đánh lừa AI & Static Solvers <<'))
        _trap_tree = ast.parse(code)
        _trap_tree = YukiReasoningLoopInjector().inject_loop(_trap_tree, depth=3)
        ast.fix_missing_locations(_trap_tree)
        code = ast.unparse(_trap_tree)
    except Exception:
        pass

    if cff_flatten:

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '>> [Control Flow Flattening] Băm nát luồng điều khiển thành ma trận State Machine <<'))

        try:

            _cff_tree = ast.parse(code)

            _cff_tree = ControlFlowFlattener(min_statements=2, add_bogus_blocks=True).visit(_cff_tree)

            ast.fix_missing_locations(_cff_tree)

            code = ast.unparse(_cff_tree)

        except Exception:

            pass

    if vm_virtualize:

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '>> [HyperVM v5.0 Ultra Real] Fetch-Decode-Execute + hidden rotating keys <<'))

        try:

            code = build_hyper_vm_payload(code)

        except Exception as _e_vm:

            try:

                print(Colorate.Diagonal(Colors.DynamicMIX((Col.yellow, Col.red)), f'>> [HyperVM] Bỏ qua do code chứa cú pháp không tương thích VM ({_e_vm}). Tự động dùng OBF AST đa tầng <<'))

            except Exception:

                pass


    code = __xamlolthoi__(code)

    st = time.time()

    if _runsource == '1':

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: main File <<"))

        code = _runmain(code)

    elif _runsource == '2':

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: exec File <<"))

        code = _runexec(code)

    elif _runsource == '3':

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Type: import File <<"))

        code = _runimport(code)

    else:

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài main <<"))

        code = _runmain(clean(code))

    Bangchon = {"1": "main", "2": "exec", "3": "import"}

    Bangchon1 = Bangchon.get(_runsource, "main")

    brotuongthelangau1 = brotuongthelangau.replace("{_runsourceobf}", Bangchon1)

    # === VÔ ĐỐI: LUÔN BẬT ẨN URL + ANTI HOOK DÙ CHỌN No ===

    # FIX BUG #3/#8: per-build patch of static 0x5A/13 in RQ payloads so decoder matches polymorphic encoder.

    def _patch_rq_keys(_s: str) -> str:

        try:

            _s = _s.replace('0x5A', hex(_YUKI_URL_XOR & 0xFF))

            _s = _s.replace('- 32 - 13)', f'- 32 - {_YUKI_URL_ROT % 95})')

            _s = _s.replace('+ 32)', f'+ 32)')  # keep decode base

            # rot encode uses '+ 13)' in _encode; payload decode uses '- 32 - 13)'

            # also patch b64 rot encode constant if present as '+ 13)'

            # (conservative: only patch exact decoder pattern)

        except Exception:

            pass

        return _s

    if anti_crack:

        anti2 = _patch_rq_keys(rqprotect) + _patch_rq_keys(RQ_VODAI_SUPER) + anticrackkey

    else:

        anti2 = _patch_rq_keys(RQ_VODAI_SUPER) + RQ_VODAI_MINIMAL

        try:

            print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> [VÔ ĐỐI] Tự động bật ẩn URL + Anti-Hook dù chọn No <<"))

        except:

            pass

    # FIX BUG #8: wrap giant raw anti-hook payloads in fragmented encrypted bootstrap

    # so final output holds blobs, not greppable 'import sys/os/ctypes/threading' plaintext.

    try:

        _anti2_wrapped = _protect_raw_payload(anti2)

        # sanity: wrapped must be much smaller source-wise? keep fallback to raw on failure

        if isinstance(_anti2_wrapped, str) and len(_anti2_wrapped) > 0:

            anti2 = _anti2_wrapped

    except Exception:

        pass

    code = obflz1(anti2+load+code)

    code = ast.parse(code)

    list_truyen = ['Convert F-String 1', 'Hide Builtins', 'Obfuscate String', 'More OBF', 'Speed Transform', 'Rename Variables', 'Try Catch', 'Reversing', 'Anti-Pycdc']

    hehe = len(list_truyen)

    current_step = 0

    def progress():

        percent = current_step / hehe * 100

        text = f'CHECKING CODE {percent:7.3f}%...'

        print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text)), end='\r')

    def done():

        nonlocal current_step

        current_step += 1

        if current_step > hehe:

            current_step = hehe

        progress()

    code = cv().visit(code)

    done()

    if hide_builtins == 'y':

        code = hide().visit(code)

    elif hide_builtins == 'n':

        code = hide1().visit(code)

    else:

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Hide-Builtins V1 <<"))

        code = hide().visit(code)

    done()

    if _obf_ == 'y':

        code = obf1().visit(code)#1

    elif _obf_ == 'n':

        code = obf2().visit(code)#2

    elif _obf_ == 'x':

        code = obf3().visit(code)#3

    elif _obf_ in ('v', '4', 's', 'm'):

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> OBF-STRING V4 (Dedicated String Machine Engine) <<"))

        code = obf4(machine_name=_YUKI_STR_MACHINE_ID).visit(code)#4

    elif _obf_ in ('5', 'v5', 's5'):

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> OBF-STRING V5 (Stronger String Machine: split + CTR + poly-call) <<"))

        code = obf5(machine_name=_YUKI_STR_MACHINE_V5_ID).visit(code)#5

    elif _obf_ in ('6', 'v6', 's6'):

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> OBF-STRING V6 (Quantum MBA String Machine: 32 Opcodes + Dynamic S-Box + Nonce Stream + Anti-Trace) <<"))

        code = obf6(machine_name=_YUKI_STR_MACHINE_V6_ID).visit(code)#6

    else:

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> OBF-STRING V1 <<"))

        code = obf1().visit(code)

    done()

    if moreobf:

        code = __moreobf__(code)

        done()

    code = speed1(code)

    if rename_vars:

        code = speed3(code)

        code = longjunk(code)

    else:

        code = speed2(code)

        done()

    # === LUÔN ẨN URL DÙ CHỌN GÌ ===

    try:

        code = apply_url_hide_always(code)

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), ">> [VÔ ĐỐI] Đã ẩn toàn bộ URL (http/https) trong code <<"))

    except Exception as _e_urlhide:

        try:

            print(f"[WARN URL HIDE] {_e_urlhide}")

        except:

            pass

    done()

    if anti_debug:

        anti3 = anti+brotuongthelangau1+gen_invincible_antidebug()

    else:

        anti3 = anti+gen_invincible_antidebug()

    tree = ast.parse(anti3)

    if _obf_ in ('v', '4', 's', 'm'):

        tree = inject_string_machine(tree, machine_name=_YUKI_STR_MACHINE_ID)

    if _obf_ in ('5', 'v5', 's5'):

        tree = inject_string_machine_v5(tree, machine_name=_YUKI_STR_MACHINE_V5_ID)

    if _obf_ in ('6', 'v6', 's6'):

        tree = inject_string_machine_v6(tree, machine_name=_YUKI_STR_MACHINE_V6_ID)

    try:

        # === ENHANCED POLYMORPHIC URL + REQUESTS HIDE FOR COMBINED TREE ===

        _fresh_main = f'__Yuki_Url_{_uuid_url_hide.uuid4().hex[:7]}__'

        tree = inject_url_decoder(tree, decoder_name=_fresh_main)

        try:

            if isinstance(code, ast.Module):

                tree.body.extend(code.body)

            elif isinstance(code, ast.AST):

                tree.body.append(code)

            elif isinstance(code, str):

                tree.body.extend(ast.parse(code).body)

        except Exception:

            try:

                tree.body.extend(ast.parse(ast.unparse(code)).body)

            except Exception:

                pass

        tree = UrlHideTransformer(decoder_name=_fresh_main).visit(tree)

        tree = apply_requests_hide(tree, decoder_name=_fresh_main)

        import ast as _ast_fix

        _ast_fix.fix_missing_locations(tree)

    except Exception as _e_main_hide:

        try:

            if _obf_ in ('v', '4', 's', 'm'):

                tree = inject_string_machine(tree, machine_name=_YUKI_STR_MACHINE_ID)

            if _obf_ in ('5', 'v5', 's5'):

                tree = inject_string_machine_v5(tree, machine_name=_YUKI_STR_MACHINE_V5_ID)

            if isinstance(code, ast.Module):

                tree.body.extend(code.body)

            elif isinstance(code, ast.AST):

                tree.body.append(code)

            elif isinstance(code, str):

                tree.body.extend(ast.parse(code).body)

            tree = UrlHideTransformer().visit(tree)

            tree = apply_requests_hide(tree)

            _ast_fix.fix_missing_locations(tree)

        except Exception:

            pass

    code = phienbantrycath(tree)

    done()

    if reverse == 'y':

        code = reversing(code)

    elif reverse == 'n':

        code = reversing1(code)

    else:

        code = reversing(code)

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Lựa chọn không hợp lệ! Mặc định sài V1 <<"))

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)),f">> Increased Difficulty OBF V1 <<"))

    done()

    class Luadoku(ast.NodeTransformer):

        def _is_valid_id(self, s):

            if not isinstance(s, str) or not s:

                return True

            try:

                return s.isidentifier()

            except Exception:

                return False

        def visit_Name(self, node):

            self.generic_visit(node)

            if isinstance(node.ctx, (ast.Store, ast.Del)):

                return node

            if not self._is_valid_id(node.id):

                try:

                    parsed = ast.parse(node.id, mode='eval').body

                    if isinstance(parsed, ast.AST):

                        parsed = ast.fix_missing_locations(parsed)

                        return ast.copy_location(parsed, node)

                except Exception:

                    pass

            return node

        def visit_Attribute(self, node):

            self.generic_visit(node)

            if not self._is_valid_id(node.attr):

                try:

                    parsed = ast.parse(node.attr, mode='eval').body

                    if isinstance(parsed, ast.Call):

                        if isinstance(parsed.func, ast.Name):

                            new_attr = parsed.func.id

                            new_call = ast.Call(

                                func=ast.Attribute(value=node.value, attr=new_attr, ctx=ast.Load()),

                                args=getattr(parsed, 'args', []),

                                keywords=getattr(parsed, 'keywords', [])

                            )

                            new_call = ast.fix_missing_locations(new_call)

                            return ast.copy_location(new_call, node)

                    parsed = ast.fix_missing_locations(parsed)

                    return ast.copy_location(parsed, node)

                except Exception:

                    pass

            return node

    try:

        code = Luadoku().visit(code)

    except Exception:

        pass

    class sieuchogay(ast.NodeTransformer):

        def _norm(self, s):

            if not isinstance(s, str) or not s:

                return s

            return unicodedata.normalize('NFKC', s)

        def visit_Name(self, node):

            self.generic_visit(node)

            node.id = self._norm(node.id)

            return node

        def visit_FunctionDef(self, node):

            self.generic_visit(node)

            node.name = self._norm(node.name)

            return node

        def visit_AsyncFunctionDef(self, node):

            self.generic_visit(node)

            node.name = self._norm(node.name)

            return node

        def visit_ClassDef(self, node):

            self.generic_visit(node)

            node.name = self._norm(node.name)

            return node

        def visit_arg(self, node):

            self.generic_visit(node)

            node.arg = self._norm(node.arg)

            return node

        def visit_ExceptHandler(self, node):

            self.generic_visit(node)

            if node.name:

                node.name = self._norm(node.name)

            return node

        def visit_Global(self, node):

            self.generic_visit(node)

            node.names = [self._norm(n) for n in node.names]

            return node

        def visit_Nonlocal(self, node):

            self.generic_visit(node)

            node.names = [self._norm(n) for n in node.names]

            return node

        def visit_keyword(self, node):

            self.generic_visit(node)

            if node.arg:

                node.arg = self._norm(node.arg)

            return node

        def visit_alias(self, node):

            self.generic_visit(node)

            node.name = self._norm(node.name)

            if node.asname:

                node.asname = self._norm(node.asname)

            return node

    code = sieuchogay().visit(code)

    ast.fix_missing_locations(code)

    try:

        ast.fix_missing_locations(code)

        code= ast.unparse(code)

    except Exception as _e:

        code = f"# unparse failed: {_e!r}\n"

    code = textwrap.dedent(code)

    code = gen_advanced_antipycdc() + Antilol + code

    code = ast.parse(code)

    # FIX: ensure future imports at top before final compile

    try: code = _fix_future_in_ast(code)

    except: pass

    done()

    duration = 0.05

    giay = 20

    delay = duration / giay

    for i in range(giay + 1):

        percent = i / giay * 100

        text = f'LOADING OBFUSCATION {percent:7.3f}%...'

        print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), text), end='\r')

        time.sleep(delay)

    # FIX BUG #14: secure compile always reorders futures (docstring + futures stay on top).

    try:

        try:

            code = _fix_future_in_ast(code)

        except Exception:

            pass


        dump = _compile_secure(ast.unparse(code) if isinstance(code, ast.Module) else code, 'ProJect', 'exec')

    except SyntaxError as _e:

        if 'from __future__' in str(_e):

            code = _fix_future_in_ast(code)

            dump = _compile_secure(ast.unparse(code) if isinstance(code, ast.Module) else code, 'ProJect', 'exec')

        else:

            raise

    code = dequybadao(dump)

    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--> ADD FINAL LAYER <--'), end='\r')

    # FIX BUG #18: outer integrity digest (verified in final file before exec)

    try:

        _outer_digest = _yuki_sha256(code)

    except Exception:

        _outer_digest = '00' * 32

    _raw_inner_code = code
    code = base64.b85encode(zlib.compress(lzma.compress(code)))

    # FIXED: handle full path correctly, keep output in same dir as input

    try:

        _base = os.path.basename(file_name)

        _dir = os.path.dirname(file_name)

        if _dir and os.path.isdir(_dir):

            output = os.path.join(_dir, "obf-" + _base)

        else:

            output = "obf-" + _base

        # fallback if still invalid (e.g., Windows drive)

        output = os.path.normpath(output)

    except Exception:

        output = "obf-" + os.path.basename(file_name)

    # Layer 1 Cryptographic Self-File-Integrity & Tamper Binding Lock

    try:

        _lobby_tmp = Lobby.replace("{_runsourceobf}", Bangchon1)

        _ap_pos = _lobby_tmp.rfind(f"(lambda {_tail_p}")

        if _ap_pos != -1:

            _hdr_part = _lobby_tmp[:_ap_pos]

            _norm_hdr = _hdr_part.encode('utf-8').replace(b'\r\n', b'\n')

            _hf_expected = hashlib.sha256(_norm_hdr).digest()

        else:

            _hf_expected = b'\x00' * 32

        

        # Compress code first

        _comp_l1 = zlib.compress(lzma.compress(_raw_inner_code))

        _n_l1 = len(_comp_l1)

        _ks_l1 = b''.join(hashlib.sha256(_hf_expected + _YUKI_SALT_L1 + c.to_bytes(4, 'big')).digest() for c in range((_n_l1 + 31) // 32))[:_n_l1]

        _enc_l1 = bytes(b ^ _ks_l1[i] for i, b in enumerate(_comp_l1))

        _b85_cipher = base64.b85encode(_enc_l1)

        _frag_expr = _yuki_frag_bytes_expr(_b85_cipher, 128)

        

        _target = "(bytecode)"

        if _target in _lobby_tmp:

            _final_src = _lobby_tmp.replace(_target, f"({_frag_expr})", 1)

        else:

            _final_src = _lobby_tmp.replace("bytecode", _frag_expr, 1)

        _final_bytes = _final_src.encode('utf-8')

    except Exception as _e_pack:
        import traceback; traceback.print_exc()

        _comp_l1 = zlib.compress(lzma.compress(code))

        _b85_fallback = base64.b85encode(_comp_l1)

        _final_bytes = Lobby.replace("bytecode", str(_b85_fallback)).replace("{_runsourceobf}", Bangchon1).encode('utf-8')

    with open(output, 'wb') as f:

        f.write(_final_bytes)

    _base_obf = os.path.basename(output)

    for _d in [r"C:\Users\khang\Downloads\sourcode", r"C:\Users\khang\Downloads"]:

        try:

            if os.path.isdir(_d):

                _t_path = os.path.join(_d, _base_obf)

                if os.path.normpath(_t_path).lower() != os.path.normpath(output).lower():

                    with open(_t_path, 'wb') as _f_sync:

                        _f_sync.write(_final_bytes)

        except Exception:

            pass

    kichthuoc = os.path.getsize(output) / 1024

    print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), '--------------------------------------'))

    try:

        # Use getpass only if stdin is a TTY, otherwise just print (avoid hang in automation)

        if sys.stdin.isatty():

            getpass(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))

        else:

            print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))

    except Exception:

        print(stage1(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Col.cyan)), f'Obfuscation Completed Succesfully in {time.time() - st:.3f}s')))

if __name__ == '__main__':

    try:main()

    except KeyboardInterrupt:pass