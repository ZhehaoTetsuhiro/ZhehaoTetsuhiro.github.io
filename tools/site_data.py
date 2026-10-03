# -*- coding: utf-8 -*-
"""GitHub Pages 站点内容源（中英双语）。

改这个文件后跑 `python3 tools/build_site.py`，会把 index.html、p/*.html、
404.html 与 assets/ 里的静态资源重新生成到仓库根目录。
纯标准库，无需安装任何依赖。
"""

SITE_URL = "https://zhehaotetsuhiro.github.io"

PROFILE = {
    "display_zh": "犬忠铭天",
    "display_en": "ZhehaoTetsuhiro",
    "handle": "ZhehaoTetsuhiro",
    "tagline_zh": "物理光学与 Vibe-Coding 狂热爱好者 · AI 重度使用者",
    "tagline_en": "Physics-optics & vibe-coding enthusiast · heavy AI user",
    "bio_zh": [
        "我用业余时间造东西：一台 128 位指令集计算机（架构、模拟器、汇编器到板上的机器码编辑器），"
        "一个科学取向的波动光学与量子光学仿真内核，一门用文言书写的编程语言，一个自研压缩 + "
        "自研非对称加密的归档工具……",
        "绝大多数项目都是「先想清楚物理与规范，再动手写」，并且带着可复现的测试与实测数字交付："
        "Tetsuhiro-WOS 有 143 项物理数值测试，Tetsuhiro-Alpha 对每个示例做端到端断言，"
        "掌控板版本要拿假板子把整条烧录协议跑通。",
        "写作、文档与实现大量借助 AI 协作完成——我把这当作一种新的工程方式，而不是外包。",
    ],
    "bio_en": [
        "I build things in my spare time: a 128-bit instruction-set computer (architecture, simulator, "
        "assembler, down to a machine-code editor running on a handheld board), a science-first wave-optics "
        "and quantum-optics kernel, a programming language written in classical Chinese, and an archiver "
        "with home-grown compression and asymmetric encryption.",
        "Most of these start from \"get the physics and the spec right, then write code\", and ship with "
        "reproducible tests and measured numbers: 143 physics/numerics tests in Tetsuhiro-WOS, end-to-end "
        "assertions over every sample in Tetsuhiro-Alpha, and a full write-and-verify flash protocol on a "
        "fake board for the mPython port.",
        "Writing, documentation and implementation are heavily AI-collaborative — I treat that as a new "
        "engineering practice, not outsourcing.",
    ],
    "contacts": [
        {"kind": "email", "label_zh": "邮箱", "label_en": "Email",
         "text": "zhehaosdog@outlook.com", "url": "mailto:zhehaosdog@outlook.com"},
        {"kind": "github", "label_zh": "GitHub", "label_en": "GitHub",
         "text": "@ZhehaoTetsuhiro", "url": "https://github.com/ZhehaoTetsuhiro"},
        {"kind": "qq", "label_zh": "QQ", "label_en": "QQ",
         "text": "2700662430", "url": None},
        {"kind": "wechat", "label_zh": "微信", "label_en": "WeChat",
         "text": "notfish0729", "url": None},
    ],
    "location_zh": "中国",
    "location_en": "China",
    "avatar": "assets/avatar.jpg",
}

# ---------------------------------------------------------------- 项目
# slug / 名称 / 一句话 / 标签 / 徽章 / 详细介绍(分节) / 下载 / 链接
PROJECTS = [
    {
        "slug": "tetsuhiro-alpha",
        "repo": "Tetsuhiro-Alpha",
        "glyph": "α",
        "accent": "#2563eb",
        "name_zh": "Tetsuhiro-Alpha",
        "name_en": "Tetsuhiro-Alpha",
        "sub_zh": "TH128I 指令集参考实现 · 模拟器 / 汇编器 / 反汇编器 / 调试器",
        "sub_en": "Reference implementation of the TH128I ISA · simulator / assembler / disassembler / debugger",
        "tagline_zh": "一台 128 位计算机的参考实现：自研指令集 TH-ISA 与零依赖 Go 工具链 tthr。",
        "tagline_en": "A 128-bit computer, from scratch: the TH-ISA instruction set and the dependency-free Go toolchain tthr.",
        "tags": [("Go 标准库 · 零依赖", "Go stdlib · zero deps"), ("17606 行", "17,606 LOC"),
                 ("MIT", "MIT"), ("v0.1.0", "v0.1.0")],
        "facts": [
            ("指令集", "Instruction set", "TH128I：基础整数 + M / A / F / D / T / C / V",
             "TH128I: base integer + M / A / F / D / T / C / V extensions"),
            ("位宽", "Width", "通用寄存器 / PC / 地址 / CSR 均 128 位", "GPRs / PC / addresses / CSRs are all 128-bit"),
            ("特权级", "Privilege", "四级 T &gt; M &gt; D &gt; S，陷阱陷入/返回与异常委托链",
             "Four levels T &gt; M &gt; D &gt; S with trap entry/return and exception delegation"),
            ("存储", "Memory", "Sv128 分页（15 级、16 字节 PTE、超级页）+ PMP 强制",
             "Sv128 paging (15 levels, 16-byte PTEs, superpages) + PMP enforcement"),
            ("示例", "Samples", "14 个端到端示例（hello / fib / fp / vector / trap / AMO / 压缩指令 …）",
             "14 end-to-end samples (hello / fib / fp / vector / trap / AMO / compressed …)"),
            ("文档", "Docs", "ISA 规范初稿 + 汇编指南 / 机器码指南（LaTeX 已编译 PDF）",
             "ISA spec draft + assembler &amp; machine-code guides (compiled LaTeX PDFs)"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("<code>tthr</code> 是 Tetsuhiro 指令集架构（TH-ISA）的参考实现，一个可执行的 "
                 "128 位机器：解释器负责取指、译码、执行、陷阱与分页，两遍汇编器把汇编源码变成 "
                 "<code>.tthr</code> 镜像，反汇编器与交互式单步调试器负责看清机器在做什么。",
                 "<code>tthr</code> is the reference implementation of the Tetsuhiro ISA (TH-ISA): an "
                 "executable 128-bit machine — an interpreter doing fetch/decode/execute/traps/paging, a "
                 "two-pass assembler turning assembly into <code>.tthr</code> images, plus a disassembler "
                 "and an interactive single-step debugger."),
                ("整个工具链只用 Go 标准库，没有第三方依赖；<code>go build -o tthr .</code> 就能得到一个"
                 "零依赖静态二进制。",
                 "The whole toolchain uses only the Go standard library — <code>go build -o tthr .</code> "
                 "yields a dependency-free static binary."),
            ]},
            {"h": ("指令集覆盖", "Instruction-set coverage"), "p": [
                ("<b>基础整数</b>：LB…LQ 全宽度访存、算术逻辑、立即数、7 位移位、全部分支与跳转、"
                 "LUI/AUIPC、FENCE、CSR 指令组。",
                 "<b>Base integer</b>: full-width LB…LQ loads/stores, ALU ops, immediates, 7-bit shifts, "
                 "all branches and jumps, LUI/AUIPC, FENCE, the CSR family."),
                ("<b>M 扩展</b>：128 位 MUL/MULH*/DIV*/REM*，含除零与溢出语义。"
                 "<b>A 扩展</b>：LR/SC 与 AMO*（<code>.w/.d/.q</code>，含 min/max 的有无符号变体）。",
                 "<b>M extension</b>: 128-bit MUL/MULH*/DIV*/REM* with divide-by-zero and overflow "
                 "semantics. <b>A extension</b>: LR/SC and AMO* (<code>.w/.d/.q</code>, signed and "
                 "unsigned min/max)."),
                ("<b>F/D 扩展</b>：32 个浮点寄存器、FLEN=128 与 NaN-box，五种舍入模式 + 动态舍入、"
                 "融合乘加、<code>fclass</code>/比较/转换，NaN、符号零与单次舍入语义严格实现"
                 "（软浮点，正确性优先）。",
                 "<b>F/D</b>: 32 FP registers with FLEN=128 and NaN-boxing, five rounding modes plus "
                 "<i>dyn</i>, fused multiply-add, <code>fclass</code>/compare/convert, with strict "
                 "NaN, signed-zero and single-rounding semantics (soft-float, correctness first)."),
                ("<b>T 安全扩展</b>：<code>tattest</code>（HMAC-SHA256 密钥化测量）、"
                 "<code>tseal</code>/<code>tunseal</code>（AES-128），仅 T 特权级可执行。",
                 "<b>T security extension</b>: <code>tattest</code> (HMAC-SHA256 keyed measurement) and "
                 "<code>tseal</code>/<code>tunseal</code> (AES-128), executable only at T level."),
                ("<b>C 扩展</b>：16 位压缩指令，取指在 16 位边界上动态切换压缩/非压缩译码，"
                 "反汇编器能处理混合流；汇编器对 <code>c.*</code> 不做自动放宽（越界直接报错，"
                 "绝不静默生成错误代码）。",
                 "<b>C extension</b>: 16-bit compressed instructions with fetch dynamically switching "
                 "between compressed/uncompressed decoding at 16-bit boundaries; the disassembler handles "
                 "mixed streams. The assembler never auto-relaxes <code>c.*</code> — out-of-range operands "
                 "are an error, never silently mis-encoded."),
                ("<b>V 扩展（向量）</b>：沿用 RVV 1.0 编码与语法，VLEN=128 / ELEN=64 —— 配置、"
                 "单元步长/跨步/索引/段/整寄存器访存与首错即停、整数运算/乘除/乘加、定点舍入与饱和、"
                 "加宽收窄、比较/掩码逻辑/归约、浮点运算与融合乘加/转换/比较/归约/加宽、"
                 "gather/compress/iota。",
                 "<b>V extension</b>: RVV 1.0 encodings and syntax with VLEN=128 / ELEN=64 — "
                 "configuration, unit-stride/strided/indexed/segment/whole-register memory ops with "
                 "first-fault, integer arithmetic/mul-div/madd, fixed-point rounding and saturation, "
                 "widening and narrowing, compares/mask logic/reductions, vector float ops with fused "
                 "multiply-add/convert/compare/reduce/widening, and gather/compress/iota."),
            ]},
            {"h": ("模拟器与调试", "Simulator & debugging"), "p": [
                ("四级特权模型 T &gt; M &gt; D &gt; S，陷阱陷入与 xRET 返回、异常委托链 "
                 "（tdeleg → medeleg → dedeleg）、逐级 CSR 访问权限校验、向量/直接陷阱向量与中断仲裁。",
                 "Four privilege levels T &gt; M &gt; D &gt; S with trap entry, xRET return, the exception "
                 "delegation chain (tdeleg → medeleg → dedeleg), per-level CSR access checks, vectored/"
                 "direct trap vectors and interrupt arbitration."),
                ("Sv128 分页（15 级、16 字节 PTE、超级页、A/D 与 U 位）与 PMP 强制（TOR/NA4/NAPOT、"
                 "R/W/X、L 锁、<code>tprot</code> 锁）；稀疏 128 位地址空间按 4 KiB 页按需分配。",
                 "Sv128 paging (15 levels, 16-byte PTEs, superpages, A/D and U bits) and PMP enforcement "
                 "(TOR/NA4/NAPOT, R/W/X, L lock, <code>tprot</code> lock); a sparse 128-bit address space "
                 "allocated lazily in 4 KiB pages."),
                ("CLI：<code>run</code>（<code>--steps/--trace/--regs/--mem</code>）、<code>step</code> "
                 "交互式单步、<code>disasm</code>、<code>asm</code>、<code>version</code>；主机 I/O 走 "
                 "tohost 寄存器，写偶数即退出、写 <code>(字节&lt;&lt;8)|1</code> 即打印。",
                 "CLI: <code>run</code> (<code>--steps/--trace/--regs/--mem</code>), <code>step</code> "
                 "interactive stepping, <code>disasm</code>, <code>asm</code>, <code>version</code>. Host "
                 "I/O goes through the <code>tohost</code> register: write an even value to exit, "
                 "<code>(byte&lt;&lt;8)|1</code> to print."),
                ("按 <code>go test ./...</code> 会对 <code>samples/</code> 下每个示例做端到端断言"
                 "（汇编 → 载入 → 执行 → 校验退出码），新增示例必须登记期望值，否则测试会提醒补登记。",
                 "<code>go test ./...</code> runs end-to-end assertions over every sample (assemble → "
                 "load → execute → check exit code); new samples must declare their expected value or the "
                 "test suite asks you to."),
            ]},
        ],
        "downloads": {
            "version": "v0.1.0",
            "assets": [
                ("tthr-linux-amd64", "Linux x86-64"),
                ("tthr-linux-arm64", "Linux ARM64"),
                ("tthr-darwin-amd64", "macOS Intel"),
                ("tthr-darwin-arm64", "macOS Apple Silicon"),
                ("tthr-windows-amd64.exe", "Windows x86-64"),
                ("tthr-windows-arm64.exe", "Windows ARM64"),
                ("checksums.txt", "SHA-256 校验和 / checksums"),
            ],
            "cmds": [
                "chmod +x tthr-linux-amd64 && ./tthr-linux-amd64 version",
                "./tthr-linux-amd64 asm samples/hello.s && ./tthr-linux-amd64 run samples/hello.tthr",
                "sha256sum -c checksums.txt",
                "# 从源码构建 / build from source\n"
                "git clone https://github.com/ZhehaoTetsuhiro/Tetsuhiro-Alpha.git\n"
                "cd Tetsuhiro-Alpha && go build -o tthr .",
            ],
            "note_zh": "二进制为静态链接、零依赖，下载即用；<code>docs/</code> 内含 ISA 规范与两份已编译的 LaTeX 指南 PDF。",
            "note_en": "Binaries are statically linked with no dependencies — download and run. <code>docs/</code> holds the ISA spec and two compiled LaTeX guides (PDF).",
        },
    },

    {
        "slug": "tetsuhiro-wos",
        "repo": "Tetsuhiro-WOS",
        "glyph": "∿",
        "accent": "#0ea5e9",
        "name_zh": "Tetsuhiro WOS",
        "name_en": "Tetsuhiro WOS",
        "sub_zh": "波动光学 + 量子光学仿真内核 · Web GUI",
        "sub_en": "Wave-optics + quantum-optics simulation kernel · Web GUI",
        "tagline_zh": "科学、准确性优先的波动光学仿真内核（Go 标准库，零第三方依赖），带鼠标键盘双可用的 Web GUI。",
        "tagline_en": "A science-first wave-optics kernel (Go stdlib, zero third-party deps) with a mouse- and keyboard-driven web GUI.",
        "tags": [("Go · 零第三方依赖", "Go · zero third-party deps"), ("143 项物理测试", "143 physics tests"),
                 ("AGPL-3.0", "AGPL-3.0"), ("v1.3.0", "v1.3.0"), ("Docker", "Docker")],
        "facts": [
            ("数值内核", "Numerical core", "自研并行 FFT、角谱法（含零填充/离轴频移高精度变体）、菲涅耳、夫琅禾费",
             "In-house parallel FFT, angular spectrum (with padding/off-axis shifted variants), Fresnel, Fraunhofer"),
            ("高级传播", "Advanced propagation", "全矢量 Ez、split-step BPM、宽带谱、部分相干、双折射、3-D 体传播",
             "Full-vectorial Ez, split-step BPM, polychromatic, partial coherence, birefringence, 3-D volume"),
            ("光学元件", "Optical elements", "20+ 内置元件 + JSON 脚本元件（热重载、可导出为 Go）",
             "20+ built-ins plus JSON scripted elements (hot-reloaded, exportable to Go)"),
            ("量子光学", "Quantum optics", "Fock 基线性光学内核：HOM / 马赫-曾德尔 / 压缩 / EPR",
             "Fock-basis linear-optics kernel: HOM / Mach-Zehnder / squeezing / EPR"),
            ("光路模型", "Ray-free scene", "元件位置与几何形状决定光路（非元件序列），轮廓即通光孔径",
             "Elements are placed by position and geometry, not sequenced; outlines are apertures"),
            ("性能", "Performance", "1024² 单次 ASM 传播约 150 ms（8 核标量），可选 CUDA/cuFFT 后端",
             "~150 ms per 1024² ASM propagation (8-core scalar); optional CUDA/cuFFT backend"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("一台用 Go 从零写起的波动光学「示波器」：内核可以当库用"
                 "（<code>import \"twos/optics\"</code>），也可以起一个 HTTP 服务，"
                 "在浏览器里搭光路、看图像/相位/偏振/立体视图。",
                 "A wave-optics bench written from scratch in Go: the kernel works as a library "
                 "(<code>import \"twos/optics\"</code>) or as an HTTP service, and you compose optical "
                 "paths in the browser while watching image, phase, polarization and 3-D views."),
                ("设计取向是「物理优先」：能用解析解对照的地方就对照，数值有效性问题（采样、奈奎斯特"
                 "带限、衰逝波）主动告警而不是悄悄给你一张好看的图。",
                 "The design bias is physics first: anywhere an analytic solution exists it is used as a "
                 "reference, and numerical validity issues (sampling, Nyquist band-limiting, evanescent "
                 "waves) raise warnings instead of quietly producing a pretty picture."),
            ]},
            {"h": ("数值内核", "Numerical core"), "p": [
                ("自研并行 FFT（支持非 2 的幂网格，Bluestein 算法）、角谱法 ASM（亥姆霍兹方程精确解）"
                 "及其三个高精度变体（零填充 <code>asm_pad</code>、离轴频移 <code>asm_shift</code>、"
                 "两者结合）、菲涅耳（两种形式）与夫琅禾费远场；衰逝波处理、奈奎斯特带限正则化、"
                 "菲涅耳数与采样有效性自动告警。",
                 "In-house parallel FFT (including non-power-of-two grids via Bluestein), angular-spectrum "
                 "propagation (exact solution of the Helmholtz equation) with three higher-accuracy "
                 "variants (padding, off-axis frequency shift, both), two Fresnel forms and Fraunhofer "
                 "far field; evanescent handling, Nyquist band-limiting regularisation, automatic "
                 "Fresnel-number and sampling-validity warnings."),
                ("高级传播：<b>全矢量角谱法</b>（重构纵向分量 Ez，非傍轴）、<b>非均匀/复折射率介质</b>"
                 "（split-step BPM，分层/梯度/吸收/增益）、<b>宽带谱叠加</b>（polychromatic）、"
                 "<b>部分相干光</b>（Gaussian Schell 模型）、<b>各向异性/双折射介质</b>"
                 "（单轴晶体与 Berreman 4×4 双轴晶体）、<b>3-D 体传播</b>（一次传播输出 x,y,z 体积场）。",
                 "Advanced propagation: <b>full-vectorial angular spectrum</b> (reconstructing the "
                 "longitudinal Ez, non-paraxial), <b>inhomogeneous/complex-index media</b> (split-step BPM: "
                 "layered, gradient, absorbing, gain), <b>polychromatic</b> spectral superposition, "
                 "<b>partial coherence</b> (Gaussian Schell model), <b>anisotropic/birefringent media</b> "
                 "(uniaxial crystals and Berreman 4×4 biaxial crystals), and <b>3-D volume propagation</b>."),
            ]},
            {"h": ("元件与光路模型", "Elements & scene model"), "p": [
                ("20+ 种可调参数元件：透镜、光阑、光栅、轴锥镜、波带片、涡旋相位板、楔形棱镜、漫射体、"
                 "反射镜、凹面/凸面镜、泽尼克像差板、偏振片、波片、旋光片、自定义琼斯矩阵、分束器、"
                 "合束器、单轴/双轴晶体、均匀介质……",
                 "20+ parameterised elements: lenses, apertures, gratings, axicons, zone plates, vortex "
                 "phase plates, wedge prisms, diffusers, mirrors, concave/convex mirrors, Zernike "
                 "aberration plates, polarizers, wave plates, rotators, custom Jones matrices, beam "
                 "splitters/combiners, uniaxial/biaxial crystals, uniform media and more."),
                ("<b>脚本元件</b>让「新元件」不需要重编译：把复透过率写成 "
                 "<code>elements/&lt;名字&gt;.json</code> 里的表达式（相位、幅度、可选琼斯矩阵 + 参数表），"
                 "加载后与内置元件同等可用（GUI 插入对话框、参数面板、场景 JSON、Go API），"
                 "服务端每 2 秒自动热重载（新增、改写、删除都跟上），定型后可 "
                 "<code>-gen-go</code> 打印等价的原生 Go 元件。",
                 "<b>Scripted elements</b> mean new elements need no recompilation: write the complex "
                 "transmission as an expression in <code>elements/&lt;name&gt;.json</code> (phase, amplitude, "
                 "optional Jones matrix, parameter table) and it is usable exactly like a built-in — GUI "
                 "insert dialog, parameter panel, scene JSON, Go API — with automatic hot reload every "
                 "2 seconds (additions, edits and deletions) and <code>-gen-go</code> to print an "
                 "equivalent native Go element."),
                ("<b>定位场景光路（1.0 光路模型）</b>：光路存的是元件的<b>位置与几何形状</b>"
                 "（<code>scene.components[]</code>），而不是「依次经过的元件序列」；光线路径由最近命中与"
                 "反射/透射几何<b>推导</b>。元件带真实轮廓（圆/方/矩形/椭圆/三角/环/多边形/双缝/十字/"
                 "星形/超椭圆/自定义顶点/细缝），轮廓即通光孔径；旧的序列配置可一键自动转换"
                 "（<code>POST /api/convert</code>）。",
                 "<b>Positional scene model</b>: a scene stores element <b>position and geometry</b> "
                 "(<code>scene.components[]</code>) rather than an ordered element list; the light path is "
                 "<b>derived</b> from nearest-hit and reflection/transmission geometry. Elements carry real "
                 "outlines (circle/square/rect/ellipse/triangle/ring/polygon/double-slit/cross/star/"
                 "superellipse/custom vertices/slit) which act as the aperture. Legacy sequential configs "
                 "convert in one click (<code>POST /api/convert</code>)."),
                ("<b>多光源与相干分组</b>：任意多个光源，各有位置/方向/波长/功率/偏振与相干组；"
                 "同组同波长相干叠加产生干涉条纹，不同组/波长按强度叠加，每个平面保留各光源的复场"
                 "可按通道单独查看。图像视图按波长→线性 sRGB（CIE 1931 拟合）真实着色。",
                 "<b>Multiple sources and coherence groups</b>: any number of sources with position, "
                 "direction, wavelength, power, polarization and coherence group; same-group same-wavelength "
                 "fields add coherently (fringes), others add in intensity, and per-plane complex fields are "
                 "kept per source for per-channel viewing. The image view is colour-accurate via "
                 "wavelength→linear sRGB (CIE 1931 fit)."),
            ]},
            {"h": ("量子光学与测量视图", "Quantum optics & measurement views"), "p": [
                ("<b>量子光学</b>：Fock 基线性光学内核，支持 Fock/相干/压缩/双模压缩/热态输入与相移、"
                 "分束器、位移、压缩、损耗门，输出光子数分布、g²(0)、正交分量与联合分布 —— "
                 "Hong-Ou-Mandel、单光子马赫-曾德尔、压缩、EPR 与混合态/损耗效应都可复现，"
                 "图表可导出 PNG/SVG。",
                 "<b>Quantum optics</b>: a Fock-basis linear-optics kernel with Fock/coherent/squeezed/"
                 "two-mode-squeezed/thermal inputs and phase-shift, beam-splitter, displacement, squeezing "
                 "and loss gates; outputs photon-number distributions, g²(0), quadratures and joint "
                 "distributions — Hong-Ou-Mandel, single-photon Mach-Zehnder, squeezing, EPR and mixed-state/"
                 "loss effects, with PNG/SVG chart export."),
                ("<b>偏振与相位</b>：斯托克斯参数、偏振椭圆（ψ/χ/轴比/手性）、偏振度、二维相位去包裹与"
                 "波前 PV/RMS；点击图像上任意一点展开该点的琼斯矢量、斯托克斯参数与相位。"
                 "<b>立体视图</b>渲染整套光路（元件板、按光源着色与相对功率的光束段、遮挡、平台网格）。",
                 "<b>Polarization and phase</b>: Stokes parameters, polarization ellipse (ψ/χ/axis ratio/"
                 "handedness), degree of polarization, 2-D phase unwrapping and wavefront PV/RMS; click any "
                 "point to expand its Jones vector, Stokes parameters and phase. A <b>3-D view</b> renders "
                 "the whole bench (element plates, beam segments coloured by source and scaled by relative "
                 "power, occlusion, platform grid)."),
                ("<b>精度验证</b>：143 项物理与数值测试 —— 艾里斑峰值与暗环、单缝 sinc²、光栅 "
                 "Raman-Nath 级数、双缝条纹、高斯束腰演化与 Gouy 相位、琼斯计算、马赫-曾德尔/迈克尔逊"
                 "能量守恒、波带片效率、散斑对比度、功率守恒、Fresnel/ASM 互证与复场级解析解对比、"
                 "双折射/Berreman、部分相干、宽带谱、HOM/相干/压缩/Fock 量子统计等。",
                 "<b>Accuracy verification</b>: 143 physics and numerics tests — Airy peak and dark rings, "
                 "single-slit sinc², grating Raman-Nath orders, double-slit fringes, Gaussian waist "
                 "evolution and Gouy phase, Jones calculus, Mach-Zehnder/Michelson energy conservation, zone-"
                 "plate efficiency, speckle contrast, power conservation, Fresnel/ASM cross-checks against "
                 "analytic complex fields, birefringence/Berreman, partial coherence, polychromatic spectra "
                 "and HOM/coherent/squeezed/Fock quantum statistics."),
            ]},
            {"h": ("GUI 与接入", "GUI & integration"), "p": [
                ("浏览器 GUI <b>鼠标与键盘双可用</b>：视图标签条 1 图像 / 2 相位 / 3 偏振 / 4-6 各分量"
                 "强度 / 7-8 分量相位 / 0 立体视图，16 个内置模板，<code>n</code> 新建、<code>o</code> "
                 "打开、<code>s</code> 保存配置 JSON、<code>m</code> 切换量子光学模式、<code>h</code> "
                 "隐藏中心图样、自定义网格大小、毛玻璃视觉主题。",
                 "The browser GUI is <b>fully usable by mouse or keyboard</b>: view tabs 1 image / 2 phase / "
                 "3 polarization / 4-6 component intensities / 7-8 component phases / 0 3-D view, 16 built-in "
                 "templates, <code>n</code> new, <code>o</code> open, <code>s</code> save scene JSON, "
                 "<code>m</code> toggle quantum mode, <code>h</code> hide the centre pattern, custom grid "
                 "sizes and a frosted-glass visual theme."),
                ("内核即库（<code>import \"twos/optics\"</code>），HTTP API 供任意语言调用"
                 "（示例含 Python 客户端），并可选 <code>-tags cuda</code> 启用 CUDA/cuFFT 后端："
                 "所有走 FFT 的路径自动加速，无 CUDA 设备时安全回退 CPU。",
                 "The kernel is a library (<code>import \"twos/optics\"</code>) and an HTTP API callable from "
                 "any language (Python client example included). An optional <code>-tags cuda</code> build "
                 "dispatches FFTs to CUDA/cuFFT, accelerating every FFT-based path, with a safe CPU fallback "
                 "when no CUDA device is present."),
            ]},
        ],
        "downloads": {
            "version": "v1.3.0",
            "assets": [
                ("wos-linux-amd64", "Linux x86-64 单文件 / single binary"),
                ("wos-linux-amd64.zip", "Linux x86-64 zip（含说明 / with notes）"),
                ("wos-windows-amd64.exe", "Windows x86-64 单文件 / single exe"),
                ("wos-windows-amd64.zip", "Windows x86-64 zip（含说明 / with notes）"),
            ],
            "cmds": [
                "./wos -addr :1120        # 打开 http://localhost:1120",
                "# 容器镜像 / container image\ndocker pull ghcr.io/zhehaotetsuhiro/tetsuhiro-wos:v1.3.0\n"
                "docker run -p 1120:1120 ghcr.io/zhehaotetsuhiro/tetsuhiro-wos:v1.3.0",
                "# 从源码构建 / from source\ngit clone https://github.com/ZhehaoTetsuhiro/Tetsuhiro-WOS.git\n"
                "cd Tetsuhiro-WOS && go build -o wos ./cmd/wos",
                "# 精度测试套件 / accuracy suite\ngo test ./optics/ -v",
            ],
            "note_zh": "容器镜像与 Release 二进制用完全相同工具链与标志编译，<b>逐位相同</b>；镜像内置 "
                       "<code>elements/</code> 元件定义，默认监听 <code>:1120</code>。",
            "note_en": "The container image and the release binaries are built with identical toolchain and "
                       "flags and are <b>bit-for-bit identical</b>; the image bundles <code>elements/</code> "
                       "and listens on <code>:1120</code>.",
        },
    },

    {
        "slug": "tetsuhiro-alpha-on-mpython",
        "repo": "Tetsuhiro-Alpha-on-mPython",
        "glyph": "◫",
        "accent": "#22c55e",
        "name_zh": "Tetsuhiro-Alpha on mPython",
        "name_en": "Tetsuhiro-Alpha on mPython",
        "sub_zh": "在掌控板上直接编辑、运行 TH128I 机器码",
        "sub_en": "Edit and run TH128I machine code directly on an mPython board",
        "tagline_zh": "把 128 位机器塞进一块掌控板：屏幕上是一串四进制数字，敲、存 flash、跑，插上电就能用。",
        "tagline_en": "A 128-bit machine squeezed onto a handheld board: the screen shows quaternary digits — type, save to flash, run, power on and go.",
        "tags": [("MicroPython", "MicroPython"), ("MIT", "MIT"), ("132 + 34 项测试", "132 + 34 tests"),
                 ("掌控板", "mPython board")],
        "facts": [
            ("板上界面", "On-board UI", "四进制数字编辑器：16 个数字 = 一条 32 位指令，一行 16 位 = 一条指令",
             "Quaternary digit editor: 16 digits = one 32-bit instruction, 16 bits per row"),
            ("寄存器", "Registers", "128 位（MicroPython 整数本就是任意精度，一分钱不花）",
             "128-bit (MicroPython ints are arbitrary precision for free)"),
            ("指令子集", "ISA subset", "基础整数 + M 扩展；CSR/陷阱/浮点/向量/压缩指令不实现，碰到就报错",
             "Base integer + M; CSR/traps/float/vector/compressed are not implemented and raise errors"),
            ("I/O", "I/O", "tohost 输出口 0x1000 + 输入口 0x1004（没输入就停在那儿等你敲）",
             "tohost output at 0x1000 plus input at 0x1004 (blocks until you type)"),
            ("电脑端工具", "Host tools", "asm / dis / run / keys / sim / push / pull",
             "asm / dis / run / keys / sim / push / pull"),
            ("烧录", "Flashing", "自动找串口、打包、写入、读回校验、重启，带备份与失败回退",
             "Auto-detect port, pack, write, read-back verify, restart — with backup and rollback"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("一块掌控板上跑着的 TH128I 子集机器：屏幕上就是一串四进制数字（<code>0 1 2 3</code>），"
                 "16 个数字 = 一条 32 位指令，一排 16 位 = 一整条指令；"
                 "<code>P Y T H O N</code> 六个金指加 <code>A B</code> 两个大按键完成编辑、存 flash、运行。",
                 "A TH128I-subset machine that lives on an mPython board: the screen <i>is</i> a string of "
                 "quaternary digits (<code>0 1 2 3</code>), 16 digits = one 32-bit instruction, 16 bits per "
                 "row. Six metal-finger keys <code>P Y T H O N</code> plus two big buttons <code>A B</code> "
                 "handle editing, saving to flash and running."),
            ]},
            {"h": ("板上机器", "The on-board machine"), "p": [
                ("<b>指令</b>：基础整数全组（全宽度访存、ALU、立即数、分支、跳转、<code>fence</code>）"
                 "与 M 扩展（<code>mul/mulh/mulhsu/mulhu/div/divu/rem/remu</code>，除零与溢出语义照规范）；"
                 "<code>ecall</code>/<code>ebreak</code> 即停机。",
                 "<b>Instructions</b>: the full base-integer set (all-width loads/stores, ALU, immediates, "
                 "branches, jumps, <code>fence</code>) plus the M extension "
                 "(<code>mul/mulh/mulhsu/mulhu/div/divu/rem/remu</code> with spec-defined divide-by-zero and "
                 "overflow semantics); <code>ecall</code>/<code>ebreak</code> halt the machine."),
                ("<b>刻意不实现</b>：CSR、陷阱/特权级、浮点、向量、压缩指令、<code>xRET</code> —— "
                 "碰到就报错，绝不猜着往下跑（理由与取舍见 <code>docs/设计.md</code>）。",
                 "<b>Deliberately unimplemented</b>: CSRs, traps/privilege levels, floating point, vectors, "
                 "compressed instructions and <code>xRET</code> — hitting one is an error, never a guess "
                 "(rationale in <code>docs/设计.md</code>)."),
                ("<b>I/O</b>沿用 <code>tthr</code> 的 tohost 约定，另加一个输入口：往 <code>0x1000</code> "
                 "写 <code>(ch&lt;&lt;8)|1</code> 打印字符、写 <code>0</code> 结束程序；从 "
                 "<code>0x1004</code> 读一个输入字符。",
                 "<b>I/O</b> follows the <code>tthr</code> tohost convention plus an input port: write "
                 "<code>(ch&lt;&lt;8)|1</code> to <code>0x1000</code> to print, <code>0</code> to exit; read "
                 "<code>0x1004</code> for one input character."),
                ("<b>编辑画面的两种看法</b>：数字视图与反汇编视图（<code>A+B</code> 快点切换），"
                 "长按 <code>O</code>/<code>N</code> 挪 16 位即上下挪一整条指令。",
                 "<b>Two ways to read the editor</b>: raw digits or disassembly (quick <code>A+B</code> "
                 "toggles). Long-pressing <code>O</code>/<code>N</code> moves 16 bits — one whole instruction."),
            ]},
            {"h": ("电脑上写程序 + 一键烧录", "Write on a PC, flash in one command"), "p": [
                ("板上敲 16 下才出一条指令，长程序受不了 —— 所以在电脑上写汇编，一条命令推上去：",
                 "Typing 16 presses per instruction does not scale, so write assembly on a PC and push it "
                 "in one command:"),
                ("<code>python3 tools/ta.py asm/dis/run/keys/sim/push/pull</code>：汇编、反汇编、"
                 "在电脑上跑、算出在板上该按哪几个键、终端里模拟掌控板、烧录 / 从板上取回。"
                 "汇编语法就是 <code>Tetsuhiro-Alpha</code> 的那一套（伪指令、指示字、<code>#</code> 注释）。",
                 "<code>python3 tools/ta.py asm/dis/run/keys/sim/push/pull</code>: assemble, disassemble, run "
                 "on the PC, work out which keys the board needs, emulate the board in a terminal, flash to "
                 "the board or pull from it. The assembly syntax is exactly "
                 "<code>Tetsuhiro-Alpha</code>'s (pseudo-instructions, directives, <code>#</code> comments)."),
                ("<code>tools/flash.py</code> 自动找串口、打包、写入、读回校验、重启，支持 "
                 "<code>--program</code>（顺便写进程序）、<code>--monitor</code>、<code>--dry-run</code>、"
                 "<code>--doctor</code>（固件版本、文件列表、剩余空间，并把六个模块逐个 import 一遍）。",
                 "<code>tools/flash.py</code> auto-detects the port, packs, writes, verifies by read-back and "
                 "restarts, with <code>--program</code> (also load a program), <code>--monitor</code>, "
                 "<code>--dry-run</code> and <code>--doctor</code> (firmware version, file list, free space, "
                 "and it imports all six modules once)."),
                ("<b>真板子上踩过的坑（都已修）</b>：板上写文件必须 <code>close()</code>（MicroPython 没有"
                 "引用计数，写完即丢会静默丢数据）；板上没有 <code>bytes.fromhex</code>，解码方式到板上"
                 "现问；写前先问剩余空间；核对时一小块一小块读（大文件一口气读会 <code>MemoryError</code>）；"
                 "等板子回话给足时间；老文件备份成 <code>*.bak</code>（已有就不动，最先备份的才是原件）；"
                 "半路写炸会自动退回；<code>main.py</code> 最后才传，断在半路旧程序还能跑。",
                 "<b>Real-board pitfalls, all fixed</b>: files must be <code>close()</code>d (MicroPython has "
                 "no refcounting; fire-and-forget writes silently lose data); the board lacks "
                 "<code>bytes.fromhex</code>, so the decoder is probed at runtime; free space is queried "
                 "before writing; verification reads small chunks (one big read raises "
                 "<code>MemoryError</code>); replies get generous timeouts; old files are backed up to "
                 "<code>*.bak</code> (never overwritten); a failed write rolls back; and <code>main.py</code> "
                 "goes last so a broken transfer leaves a working board."),
                ("<b>测试</b>：<code>tests/test_all.py</code> 132 条（机器核心、汇编/反汇编往返、界面模型、"
                 "整机剧本）+ <code>tests/test_flash.py</code> 34 条（拿假板子跑完整条写入 → 核对的路，"
                 "含「砍掉 unhexlify 的假板子」与发给板子的每段代码的 MicroPython 解析）。",
                 "<b>Tests</b>: 132 cases in <code>tests/test_all.py</code> (machine core, assemble/"
                 "disassemble round-trips, UI model, scripted end-to-end runs) plus 34 in "
                 "<code>tests/test_flash.py</code> (the whole write→verify protocol against a fake board, "
                 "including a board with <code>unhexlify</code> removed, and MicroPython parsing of every "
                 "code fragment sent to the board)."),
            ]},
        ],
        "downloads": {
            "version": None,
            "assets": [],
            "cmds": [
                "git clone https://github.com/ZhehaoTetsuhiro/Tetsuhiro-Alpha-on-mPython.git\n"
                "cd Tetsuhiro-Alpha-on-mPython",
                "pip install pyserial",
                "python3 tools/flash.py --list        # 看看有哪些串口 / list serial ports",
                "python3 tools/flash.py               # 打包、写入、读回校验、重启",
                "python3 tools/flash.py --doctor      # 固件版本、文件列表、剩余空间",
                "make check                           # 全部测试 / full test suite",
            ],
            "note_zh": "这个项目走「源码 + 一键烧录」而非预编译二进制：板上跑的是 MicroPython，"
                       "固件与文件都由 <code>tools/flash.py</code> 直接写入掌控板。",
            "note_en": "This project ships as source with a one-command flasher rather than prebuilt binaries: "
                       "the board runs MicroPython, and <code>tools/flash.py</code> writes everything it needs.",
        },
    },

    {
        "slug": "tetsuhiro-code-on-casio",
        "repo": "Tetsuhiro-Code-On-Casio",
        "glyph": "∑",
        "accent": "#f59e0b",
        "name_zh": "Tetsuhiro Code-on-Casio 991/999",
        "name_en": "Tetsuhiro Code-on-Casio 991/999",
        "sub_zh": "在 Casio 991/999 计算器上编程：Lean 4 模拟器 + 配套书",
        "sub_en": "Programming the Casio 991/999 calculators: a Lean 4 simulator plus a book",
        "tagline_zh": "没有 while、没有数组、没有 if、没有回车 —— 分支、循环、递归、状态机全部编码进算术本身。",
        "tagline_en": "No while, no arrays, no if, no enter key — branches, loops, recursion and state machines all encoded into arithmetic itself.",
        "tags": [("Lean 4 模拟器", "Lean 4 simulator"), ("MIT", "MIT"), ("中英各 78 页", "78 pages × 2 languages"),
                 ("v0.1.1", "v0.1.1")],
        "facts": [
            ("模拟器", "Simulator", "Lean 4：15 位十进制算术、Math/Syntax/Argument ERROR、多语句链",
             "Lean 4: 15-digit decimal arithmetic, Math/Syntax/Argument ERROR, statement chains"),
            ("配套书", "The book", "《Casio Coding 从入门到精通》中文 / *From Beginner to Master* 英文，各 78 页",
             "“Casio Coding: From Beginner to Master”, 78 pages each in Chinese and English"),
            ("示例", "Examples", "素数判定、EXE 范围模拟、函数记忆、标记位冻结、终止语句",
             "Primality test, EXE-range runs, function memory, flag freeze, terminating statement"),
            ("测试", "Tests", "Math/Syntax/Argument ERROR 检测用例，含 Σ 体内 STO 反例",
             "Math/Syntax/Argument ERROR detection cases, incl. a STO-inside-Σ counterexample"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("一套关于「在函数计算器上编程」的完整作品：一本 78 页（中英各一版）的书，"
                 "加一个用 Lean 4 从零写的 991/999 模拟器 —— 书里的每个构造都能在模拟器上逐步复现。",
                 "A complete treatment of programming a scientific calculator: a 78-page book (in both "
                 "Chinese and English) plus a Lean 4 simulator of the 991/999 written from scratch, so every "
                 "construct in the book can be reproduced step by step."),
                ("你拥有的全部工具是「一条条用 <code>:</code> 相连的语句」和「一次一次的 EXE」。"
                 "布尔逻辑藏进阶跃函数 OZ 里，循环只此一家 <code>Σ(f(x),x,a,b)</code>，"
                 "取整函数族 Rnd/RNI 承担截断与取模，多语句链就是循环的程序计数器，"
                 "标记位给链装上记忆，终止语句 <code>B÷(1−B)</code> 用 Math ERROR 结束程序、防止多按。",
                 "Your entire toolkit is statements chained with <code>:</code> and one EXE press at a time. "
                 "Boolean logic hides inside a step function OZ, the only loop is "
                 "<code>Σ(f(x),x,a,b)</code>, the rounding family Rnd/RNI handles truncation and modulo, the "
                 "statement chain <i>is</i> the loop's program counter, flag bits give it memory, and the "
                 "terminating statement <code>B÷(1−B)</code> ends a program with a Math ERROR so it cannot be "
                 "over-pressed."),
                ("<b>引子</b>：下面这一行表达式，在 991/999 上按一次 EXE，就能判定 "
                 "<code>2&lt;A&lt;10⁸</code> 内任意整数是否为素数（1 素数 / 0 合数）：",
                 "<b>A taste</b>: this single expression decides primality for any "
                 "<code>2&lt;A&lt;10⁸</code> with one EXE press (1 prime, 0 composite):"),
                ("<code>1-OZ(e^(Σ(ln(OZ((cos(Aπ/x))²)+1), x=2, RNI(√A−1/2)))-1)</code>",
                 "<code>1-OZ(e^(Σ(ln(OZ((cos(Aπ/x))²)+1), x=2, RNI(√A−1/2)))-1)</code>"),
                ("原理：<code>x</code> 整除 <code>A</code> 时 <code>cos(Aπ/x)=±1</code>，其平方经 "
                 "<code>ln</code> 后贡献 0；<code>OZ</code> 是手工构造的阶跃函数（借计算器 15 位内部精度与 "
                 "<code>10⁻¹⁰</code> 量级的小量把「是否为零」变成 0/1），<code>RNI</code> 把内部 15 位值"
                 "截断为显示精度 —— 整条公式把整除性、全称量词与布尔化全部压缩进一次求值。"
                 "完整构造、正确性证明与推广（因子和、GCD、Pell 方程、蒙特卡洛……）见配套书籍。",
                 "Why it works: when <code>x</code> divides <code>A</code>, <code>cos(Aπ/x)=±1</code> whose "
                 "square contributes 0 after <code>ln</code>; <code>OZ</code> is a hand-built step function "
                 "(using the calculator's 15-digit internal precision and a <code>10⁻¹⁰</code> epsilon to turn "
                 "\"is it zero\" into 0/1) and <code>RNI</code> truncates the internal 15 digits to display "
                 "precision — the whole formula compresses divisibility, universal quantification and "
                 "Booleanisation into one evaluation. The full construction, a correctness proof and "
                 "generalisations (divisor sums, GCD, Pell's equation, Monte Carlo, …) are in the book."),
            ]},
            {"h": ("模拟器", "The simulator"), "p": [
                ("Lean 4 实现，复现真机行为：15 位十进制算术、Math/Syntax/Argument ERROR、"
                 "多语句链（每按一句、回绕、出错复位 —— 也就是循环的程序计数器语义）、语句级 STO 校验、"
                 "变量 <code>A–F x y z</code>、<code>ANS</code>、函数记忆 <code>f(x)/g(x)</code>、"
                 "EXE 次数（或范围）模拟。",
                 "A Lean 4 implementation reproducing real-machine behaviour: 15-digit decimal arithmetic, "
                 "Math/Syntax/Argument ERROR, statement chains (one press per statement, wrap-around, reset "
                 "on error — i.e. loop program-counter semantics), statement-level STO checking, variables "
                 "<code>A–F x y z</code>, <code>ANS</code>, function memory <code>f(x)/g(x)</code>, and "
                 "EXE-count (or range) simulation."),
                ("<code>.tc</code> 文件描述一条语句链，模拟器可以逐步执行或按 EXE 次数批量跑：",
                 "<code>.tc</code> files describe a statement chain; the simulator steps through it or runs "
                 "a range of EXE counts:"),
                ("<code>cd simulator &amp;&amp; lake build</code><br>"
                 "<code>.lake/build/bin/tcc ../examples/prime.tc</code>&nbsp;&nbsp;→ 输出 0：3721=61² 是合数<br>"
                 "<code>.lake/build/bin/tcc ../examples/prime.tc 10 20</code>&nbsp;&nbsp;→ 对范围内每个 EXE 次数模拟",
                 "<code>cd simulator &amp;&amp; lake build</code><br>"
                 "<code>.lake/build/bin/tcc ../examples/prime.tc</code>&nbsp;&nbsp;→ prints 0: 3721=61² is composite<br>"
                 "<code>.lake/build/bin/tcc ../examples/prime.tc 10 20</code>&nbsp;&nbsp;→ simulates each EXE count in the range"),
            ]},
            {"h": ("书与仓库", "Book & repository"), "p": [
                ("《Casio Coding 从入门到精通》：语句与多语句链编程基础、程序成本（EXE 复杂度、以 Σ 求和"
                 "次数计的时间复杂度、空间复杂度）、绝对值与 OZ 布尔逻辑、取整函数族、Σ 求和、标记位与"
                 "终止语句、数论应用（素数判定的完整证明、因子和、GCD、Pell 方程）、迭代与数值方法、"
                 "复数/多项式/矩阵、函数记忆、精度理论与错误大全。",
                 "The book covers statement-chain programming basics, program cost (EXE complexity, time "
                 "complexity counted in Σ summations, space complexity), absolute values and OZ Boolean "
                 "logic, the rounding family, Σ summation, flag bits and terminating statements, number-"
                 "theoretic applications (full primality proof, divisor sums, GCD, Pell), iteration and "
                 "numerical methods, complex numbers / polynomials / matrices, function memory, and precision "
                 "theory with an error catalogue."),
                ("仓库结构：<code>simulator/</code>（Lean 4 模拟器）、<code>documents/zh/</code> 与 "
                 "<code>documents/en/</code>（各 78 页，黑白印刷风格，<code>xelatex</code> 编译）、"
                 "<code>examples/</code>（<code>.tc</code> 示例）、<code>tests/</code>（错误检测用例）。",
                 "Repository layout: <code>simulator/</code> (Lean 4), <code>documents/zh/</code> and "
                 "<code>documents/en/</code> (78 pages each, print-style black and white, built with "
                 "<code>xelatex</code>), <code>examples/</code> (<code>.tc</code> samples) and "
                 "<code>tests/</code> (error-detection cases)."),
                ("<b>致谢</b>：基本思路与设想（包括素数判定函数等核心构造）由 ZhehaoTetsuhiro 提出；"
                 "完善、文档撰写与模拟器实现由 Kimi K3 完成。",
                 "<b>Credits</b>: the core ideas and vision — including the primality-testing function — were "
                 "conceived by ZhehaoTetsuhiro; refinement, book writing and the Lean 4 simulator were done "
                 "by Kimi K3."),
            ]},
        ],
        "downloads": {
            "version": "v0.1.1",
            "assets": [
                ("casio-coding-zh.pdf", "《Casio Coding 从入门到精通》中文版（78 页）"),
                ("casio-coding-en.pdf", "“Casio Coding: From Beginner to Master” English (78 pp.)"),
            ],
            "cmds": [
                "git clone https://github.com/ZhehaoTetsuhiro/Tetsuhiro-Code-On-Casio.git",
                "cd simulator && lake build          # 构建 Lean 4 模拟器 / build the simulator",
                ".lake/build/bin/tcc ../examples/prime.tc",
                "# 书源码编译（需 xelatex）/ rebuild the book\ncd documents/zh && xelatex main.tex",
            ],
            "note_zh": "两本书的成品 PDF 直接从 Release 下载；<code>documents/</code> 里是 <code>xelatex</code> 源码。",
            "note_en": "Both books are downloadable as PDFs from the release; <code>documents/</code> holds the "
                       "<code>xelatex</code> sources.",
        },
    },

    {
        "slug": "codex-manager",
        "repo": "Codex-Manager",
        "glyph": "⚙",
        "accent": "#a855f7",
        "name_zh": "Codex-Manager",
        "name_en": "Codex-Manager",
        "sub_zh": "Codex CLI 配置可视化管理器 · 现代 TUI",
        "sub_en": "A modern TUI to manage your Codex CLI configuration",
        "tagline_zh": "把 <code>~/.codex/config.toml</code> 手工编辑的痛，变成表单一填、下拉一选，且注释原样保留。",
        "tagline_en": "Turns hand-editing <code>~/.codex/config.toml</code> into forms and dropdowns — while keeping every comment intact.",
        "tags": [("Go · bubbletea", "Go · bubbletea"), ("AGPL-3.0", "AGPL-3.0"), ("v0.1.1", "v0.1.1"),
                 ("跨平台", "Cross-platform")],
        "facts": [
            ("概览", "Overview", "Codex 版本、当前生效模型/供应商、密钥就绪状态、备份统计",
             "Codex version, effective model/provider, key readiness, backup stats"),
            ("全局与模型设置", "Global & model settings", "model / approval_policy / sandbox_mode / 上下文窗口 / 最大输出 tokens",
             "model / approval_policy / sandbox_mode / context window / max output tokens"),
            ("供应商与档案", "Providers & profiles", "<code>[model_providers.*]</code> 与 <code>[profiles.*]</code> 增删改查、一键应用为全局",
             "CRUD for <code>[model_providers.*]</code> and <code>[profiles.*]</code>, one-key apply as global"),
            ("安全设计", "Safety", "外科手术式编辑、自动备份 30 份、先校验后落盘、密钥掩码与 0600",
             "Surgical edits, 30 automatic backups, validate-before-write, masked keys with 0600"),
            ("命令行", "CLI mode", "<code>tcm list</code> / <code>tcm use</code> / <code>tcm doctor</code>",
             "<code>tcm list</code> / <code>tcm use</code> / <code>tcm doctor</code>"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("Codex CLI 的配置都藏在 <code>~/.codex/config.toml</code> 里 —— 手工编辑容易破坏格式、"
                 "丢失注释、记不住字段名。<code>tcm</code> 把这些变成直观界面：表单编辑、下拉选择、"
                 "掩码输入，并且<b>只改动你触碰的键</b>，注释与排版原样保留。",
                 "Codex CLI keeps its configuration in <code>~/.codex/config.toml</code>, where hand-editing "
                 "breaks formatting, loses comments and requires memorising key names. <code>tcm</code> turns "
                 "that into a real interface — forms, dropdowns, masked input — and <b>only touches the keys "
                 "you touch</b>, preserving comments and layout byte for byte."),
            ]},
            {"h": ("功能", "Features"), "p": [
                ("<b>概览</b>：Codex 版本、当前生效模型/供应商、密钥就绪状态、备份统计。"
                 "<b>全局设置</b>：<code>model</code> / <code>model_provider</code> / "
                 "<code>approval_policy</code> / <code>sandbox_mode</code> / "
                 "<code>model_reasoning_effort</code> / <code>model_verbosity</code> 等常用键，"
                 "表单 + 下拉编辑，<b>留空即删除该键</b>。",
                 "<b>Overview</b>: Codex version, effective model/provider, key readiness, backup stats. "
                 "<b>Global settings</b>: <code>model</code>, <code>model_provider</code>, "
                 "<code>approval_policy</code>, <code>sandbox_mode</code>, "
                 "<code>model_reasoning_effort</code>, <code>model_verbosity</code> and friends, edited via "
                 "forms and dropdowns — <b>empty means delete the key</b>."),
                ("<b>模型设置</b>：上下文窗口 <code>model_context_window</code>（Codex 直接生效）与最大"
                 "输出 tokens <code>model_max_output_tokens</code>，正整数校验，概览页同步展示。",
                 "<b>Model settings</b>: <code>model_context_window</code> (honoured directly by Codex) and "
                 "<code>model_max_output_tokens</code> with positive-integer validation, mirrored on the "
                 "overview page."),
                ("<b>模型供应商</b>：<code>[model_providers.*]</code> 增删改查，<code>wire_api</code>"
                 "（responses / chat）下拉，支持 <code>key = value</code> 高级自定义字段，新建时可直接"
                 "保存 API Key。<b>配置档案</b>：<code>[profiles.*]</code> 增删改查，一键「应用为全局」，"
                 "配合 <code>codex --profile &lt;名称&gt;</code> 使用。",
                 "<b>Providers</b>: CRUD for <code>[model_providers.*]</code>, a <code>wire_api</code> "
                 "(responses / chat) dropdown, advanced <code>key = value</code> custom fields, and saving an "
                 "API key right when creating one. <b>Profiles</b>: CRUD for <code>[profiles.*]</code> with "
                 "one-key \"apply as global\", for use with <code>codex --profile &lt;name&gt;</code>."),
            ]},
            {"h": ("安全设计", "Safety design"), "p": [
                ("<b>外科手术式编辑</b>：只修改目标键，注释、空行、键顺序、其余字段字节级保留。",
                 "<b>Surgical editing</b>: only the target key changes; comments, blank lines, key order and "
                 "every other byte are preserved."),
                ("<b>自动备份</b>：每次写盘前备份到 <code>~/.codex/backups/</code>，保留最近 30 份，"
                 "应用内可恢复。<b>先校验后落盘</b>：TOML 不合法直接拒绝保存，坏配置进不了你的 "
                 "<code>~/.codex</code>。",
                 "<b>Automatic backups</b>: every write is preceded by a backup into "
                 "<code>~/.codex/backups/</code> (last 30 kept) restorable from inside the app. "
                 "<b>Validate before write</b>: invalid TOML is refused outright, so broken config never "
                 "reaches your <code>~/.codex</code>."),
                ("<b>密钥安全</b>：掩码输入、默认打码显示，<code>auth.json</code> / <code>env.sh</code> "
                 "权限 <code>0600</code>。OpenAI 官方 Key 写入 <code>auth.json</code> 的 "
                 "<code>OPENAI_API_KEY</code>；自定义供应商（DeepSeek / OpenRouter / Kimi …）的 Key "
                 "持久化到 <code>~/.codex/env.sh</code>，按 <code>i</code> 向 <code>~/.zshrc</code> / "
                 "<code>~/.bashrc</code> 注入带标记的 <code>source</code> 行。",
                 "<b>Key handling</b>: masked input and masked display by default, with "
                 "<code>auth.json</code> / <code>env.sh</code> at mode <code>0600</code>. An official OpenAI "
                 "key goes into <code>OPENAI_API_KEY</code> in <code>auth.json</code>; custom-provider keys "
                 "(DeepSeek / OpenRouter / Kimi …) persist to <code>~/.codex/env.sh</code> and <code>i</code> "
                 "injects a marked <code>source</code> line into <code>~/.zshrc</code> / "
                 "<code>~/.bashrc</code>."),
                ("<b>命令行模式</b>：<code>tcm list</code>、<code>tcm use fast</code>、"
                 "<code>tcm doctor</code> —— <code>use</code> 沿用同样的外科手术式编辑与自动备份，"
                 "<code>doctor</code> 只检查本地状态，不发网络请求、不消耗额度。",
                 "<b>CLI mode</b>: <code>tcm list</code>, <code>tcm use fast</code>, <code>tcm doctor</code> "
                 "— <code>use</code> reuses the same surgical editing and backups, and <code>doctor</code> "
                 "only inspects local state: no network calls, no quota spent."),
            ]},
        ],
        "downloads": {
            "version": "v0.1.1",
            "assets": [
                ("tcm-linux-amd64", "Linux x86-64"),
                ("tcm-darwin-amd64", "macOS Intel"),
                ("tcm-darwin-arm64", "macOS Apple Silicon"),
                ("tcm-windows-amd64.exe", "Windows x86-64"),
                ("checksums.txt", "SHA-256 校验和 / checksums"),
            ],
            "cmds": [
                "sudo install -m 0755 tcm-linux-amd64 /usr/local/bin/tcm",
                "# 或 go install / or go install\ngo install github.com/ZhehaoTetsuhiro/Codex-Manager@latest",
                "# 或源码构建 / or from source\ngit clone https://github.com/ZhehaoTetsuhiro/Codex-Manager.git\n"
                "cd Codex-Manager && make install   # 装到 ~/.local/bin/tcm",
                "tcm list && tcm doctor",
            ],
            "note_zh": "需要 Go 1.25+ 才能 <code>go install</code>；国内网络可设 "
                       "<code>GOPROXY=https://goproxy.cn,direct</code>。",
            "note_en": "<code>go install</code> needs Go 1.25+; behind a slow link to proxy.golang.org, set "
                       "<code>GOPROXY=https://goproxy.cn,direct</code>.",
        },
    },

    {
        "slug": "tetsuhiro-lang",
        "repo": "Tetsuhiro-Lang",
        "glyph": "谕",
        "accent": "#e11d48",
        "name_zh": "哲浩之谕 · Tetsuhiro-Lang",
        "name_en": "Tetsuhiro-Lang (哲浩之谕)",
        "sub_zh": "以文言书写 · 以栈运化 · 铸为静态 ELF",
        "sub_en": "Written in classical Chinese, computed on a stack, forged into a static ELF",
        "tagline_zh": "一门以古汉语书写的栈式编程语言；编译器 zhc 以 Go 撰成，铸无 libc 之静态 Linux 可执行文件。",
        "tagline_en": "A stack language written in classical Chinese; its compiler zhc (Go) forges libc-free static Linux executables.",
        "tags": [("Go", "Go"), ("AGPL-3.0", "AGPL-3.0"), ("v0.1.0", "v0.1.0"),
                 ("Linux x86-64", "Linux x86-64"), ("真编译", "Compiles for real")],
        "facts": [
            ("语法", "Syntax", "名号书于 《》，文辞书于 「」，数书汉数，注以 <code>注曰「……」</code>",
             "Names in 《》, strings in 「」, numbers in Chinese numerals, comments as <code>注曰「…」</code>"),
            ("核心", "Core", "栈式；<code>复 弃 换 凌 转</code> 五字运栈，术（函数）循「栈之礼」",
             "Stack-based; five stack verbs 复/弃/换/凌/转, functions follow the \"stack rite\""),
            ("编译", "Backend", "生成 x86-64 汇编（Intel 句法）→ 系统 <code>as</code>/<code>ld</code> → 静态 ELF",
             "Emits x86-64 assembly (Intel syntax) → system <code>as</code>/<code>ld</code> → static ELF"),
            ("值模型", "Value model", "64 位带标记值：数/虚/阴阳/文/列/典/浮，低三位记其类",
             "64-bit tagged values: number/void/yin-yang/text/list/dict/float, type in the low 3 bits"),
            ("模块", "Modules", "<code>承</code> 纳经卷（<code>.浩</code>）与典册（<code>.哲</code>），可递归相承",
             "<code>承</code> imports scrolls (<code>.浩</code>) and tomes (<code>.哲</code>), recursively"),
            ("运行", "Runtime", "以 syscall 直通内核，无 libc 之倚",
             "Syscalls straight to the kernel — no libc"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("一门认真的语言，用文言写：<code>.浩</code> 是源界，编译器 <code>zhc</code> 把界译成 "
                 "AMD64 汇编，经系统 <code>as</code> 与 <code>ld</code> 铸为<b>无 libc 的静态 Linux "
                 "可执行文件</b> —— 不是解释器，不是玩具转译。",
                 "A serious language written in classical Chinese: <code>.浩</code> is a source \"realm\", and "
                 "the compiler <code>zhc</code> translates it to AMD64 assembly, forged by the system "
                 "<code>as</code> and <code>ld</code> into a <b>libc-free static Linux executable</b> — not "
                 "an interpreter, not a toy transpiler."),
                ("界以「哲浩御世」开篇，以「归源」收官；误犯则本源垂示于误途"
                 "（<code>哲浩垂示：……</code>），其行归一。",
                 "A realm opens with 「哲浩御世」 and closes with 「归源」; on an error the source speaks "
                 "(<code>哲浩垂示：…</code>) and execution ends cleanly."),
                ("<code>例/首例.浩</code>：",
                 "<code>例/首例.浩</code>:"),
                ("哲浩御世。<br>注曰「首例——万物之首要示现：问候本源」<br><br>"
                 "「浩哉，哲浩御世之界！」宣。<br>二、三加五乘宣。&nbsp;&nbsp;注曰「得二十五」<br>"
                 "九根宣。&nbsp;&nbsp;注曰「得三」<br>「浩」三乘宣。&nbsp;&nbsp;注曰「得「浩浩浩」」<br>归源。",
                 "哲浩御世。<br>注曰「首例——万物之首要示现：问候本源」<br><br>"
                 "「浩哉，哲浩御世之界！」宣。<br>二、三加五乘宣。&nbsp;&nbsp;注曰「yields 25」<br>"
                 "九根宣。&nbsp;&nbsp;注曰「yields 3」<br>「浩」三乘宣。&nbsp;&nbsp;注曰「yields 「浩浩浩」」<br>归源。"),
                ("<code>make build &amp;&amp; zhc/zhc 例/首例.浩 -o 首例 --run</code> →<br>"
                 "<code>浩哉，哲浩御世之界！</code> / <code>25</code> / <code>3.0</code> / <code>浩浩浩</code>",
                 "<code>make build &amp;&amp; zhc/zhc 例/首例.浩 -o 首例 --run</code> →<br>"
                 "<code>浩哉，哲浩御世之界！</code> / <code>25</code> / <code>3.0</code> / <code>浩浩浩</code>"),
            ]},
            {"h": ("语言设计", "Language design"), "p": [
                ("<b>纯文言语法</b>：无空格、无外邦符号；名号书于 <code>《》</code>，文辞书于 "
                 "<code>「」</code>，数书汉数（<code>三十四</code>、<code>三点一四</code>），"
                 "注以 <code>注曰「……」</code>。",
                 "<b>Purely classical syntax</b>: no spaces, no foreign symbols; names live in "
                 "<code>《》</code>, strings in <code>「」</code>, numbers are Chinese numerals "
                 "(<code>三十四</code>, <code>三点一四</code>), comments are <code>注曰「…」</code>."),
                ("<b>栈式核心</b>：诸敕皆与栈相往来，<code>复 弃 换 凌 转</code> 五字运栈；"
                 "术（函数）循「栈之礼」—— 受参自栈取，成果留栈顶。",
                 "<b>Stack core</b>: every edict goes through the stack, with the five verbs 复/弃/换/凌/转; "
                 "functions follow the \"stack rite\" — arguments come off the stack, results are left on top."),
                ("<b>带标记值</b>：64 位 tagged value，低三位记其类 —— 数、虚、阴阳、文、列、典、浮。",
                 "<b>Tagged values</b>: 64-bit words whose low three bits carry the type — number, void, "
                 "yin/yang, text, list, dict, float."),
                ("<b>经籍模块</b>：<code>承</code> 字可纳经卷（<code>.浩</code> 源界）与典册"
                 "（<code>.哲</code>），经经相承，允许互相引用而不会循环展开。",
                 "<b>Scripture modules</b>: the keyword <code>承</code> imports scrolls (<code>.浩</code>) and "
                 "tomes (<code>.哲</code>); realms can import each other without circular expansion."),
                ("<b>编译器用法</b>：<code>zhc &lt;界.浩&gt; [-o 出] [-s 出.s] [--run]</code>；"
                 "界中可取化生「外众」（一列），得命令行所附之众。",
                 "<b>Compiler usage</b>: <code>zhc &lt;realm.浩&gt; [-o out] [-s out.s] [--run]</code>; a "
                 "realm can materialise 「外众」, a list of the command-line arguments."),
            ]},
        ],
        "downloads": {
            "version": "v0.1.0",
            "assets": [
                ("zhc-v0.1.0-linux-amd64", "编译器 / compiler（静态链接，仅需系统 as 与 ld）"),
                ("Tetsuhiro-Langv0.1.0.tet", "示例程序归档 / sample programs archive"),
                ("Tetsuhiro-Langv0.1.0.tet.key", "归档密钥 / archive key"),
            ],
            "cmds": [
                "chmod +x zhc-v0.1.0-linux-amd64 && ./zhc-v0.1.0-linux-amd64 --help",
                "# 铸界并即行 / forge and run\n./zhc-v0.1.0-linux-amd64 例/首例.浩 -o 首例 --run",
                "# 从源码构建 / from source（需 Go ≥ 1.25 与 binutils）\n"
                "git clone https://github.com/ZhehaoTetsuhiro/Tetsuhiro-Lang.git\ncd Tetsuhiro-Lang && make install",
                "make check     # 全部测试 / full test suite",
            ],
            "note_zh": "编译器本身是静态二进制，但铸界需要系统里有 <code>as</code> 与 <code>ld</code>"
                       "（binutils）；产物是 x86-64 Linux 静态 ELF。",
            "note_en": "The compiler is a static binary, but forging a realm needs system <code>as</code> and "
                       "<code>ld</code> (binutils); output is a static x86-64 Linux ELF.",
        },
    },

    {
        "slug": "tetsuhiror",
        "repo": "Tetsuhiror",
        "glyph": "◈",
        "accent": "#14b8a6",
        "name_zh": "Tetsuhiror",
        "name_en": "Tetsuhiror",
        "sub_zh": "自研压缩 · 自研非对称加密 · 量子增强熵源",
        "sub_en": "Home-grown compression · home-grown asymmetric encryption · quantum-enhanced entropy",
        "tagline_zh": "命令行归档工具 <code>tet</code>：TCZ 压缩 + T-IES 加密，密钥派生里掺进量子电路测量的随机性。",
        "tagline_en": "The <code>tet</code> archiver: TCZ compression + T-IES encryption, with quantum-circuit measurement mixed into key derivation.",
        "tags": [("Go + pyqpanda", "Go + pyqpanda"), ("AGPL-3.0", "AGPL-3.0"), ("v0.1.0", "v0.1.0"),
                 ("Windows / Linux", "Windows / Linux"), ("单文件", "Single binary")],
        "facts": [
            ("压缩", "Compression", "TCZ：LZ77 变体 + 自适应算术编码两级流水线，文本场景优于 <code>gzip -9</code>",
             "TCZ: a two-stage LZ77 variant + adaptive arithmetic coding, beating <code>gzip -9</code> on text"),
            ("加密", "Encryption", "T-IES：ElGamal 型混合加密，RFC 3526 组 14（2048 位 MODP）安全素数群",
             "T-IES: ElGamal-style hybrid encryption over the RFC 3526 group 14 (2048-bit MODP) safe-prime group"),
            ("量子增强", "Quantum boost", "QPanda Shor 周期查找（QPE）测量比特经 THASH-256 提取白化后参与密钥派生",
             "QPanda Shor period-finding (QPE) measurement bits whitened through THASH-256 feed key derivation"),
            ("完整性", "Integrity", "TMAC 认证 + 条目 CRC + 路径穿越防护；元数据全在密文内，头部零泄露",
             "TMAC authentication + per-entry CRC + path-traversal defence; all metadata inside the ciphertext"),
            ("分发", "Distribution", "静态链接单文件，Windows / Linux 开箱即用",
             "Statically linked single binary, ready to run on Windows / Linux"),
        ],
        "detail": [
            {"h": ("它是什么", "What it is"), "p": [
                ("一个刻意「自己造轮子」的归档工具：压缩算法自己写（TCZ），非对称加密自己构造（T-IES），"
                 "连随机熵源都接了一条量子电路。Go 实现核心，pyqpanda 提供量子随机源。",
                 "A deliberately wheel-reinventing archiver: its own compression (TCZ), its own asymmetric "
                 "construction (T-IES), and even a quantum circuit wired into the entropy source. Go core, "
                 "pyqpanda for the quantum randomness."),
            ]},
            {"h": ("三个自研件", "Three home-grown pieces"), "p": [
                ("<b>TCZ 压缩</b>：两级流水线，LZ77 变体 + 自适应算术编码，文本场景压缩率显著优于 "
                 "<code>gzip -9</code>；不可压缩数据自动回退存储模式，保证<b>最坏情况零膨胀</b>。",
                 "<b>TCZ compression</b>: a two-stage pipeline of an LZ77 variant plus adaptive arithmetic "
                 "coding that beats <code>gzip -9</code> noticeably on text; incompressible input falls back "
                 "to stored mode, guaranteeing <b>zero expansion in the worst case</b>."),
                ("<b>T-IES 加密</b>：自研 ElGamal 型混合加密，群参数取 RFC 3526 组 14（2048 位 MODP）"
                 "安全素数群，构造本身自研。",
                 "<b>T-IES encryption</b>: an in-house ElGamal-style hybrid scheme over the public RFC 3526 "
                 "group 14 (2048-bit MODP) safe-prime group — the parameters are standard, the construction "
                 "is not."),
                ("<b>量子增强熵源</b>：QPanda 的 Shor 周期查找电路（QPE）测量比特经 THASH-256 提取白化后"
                 "参与密钥派生。",
                 "<b>Quantum-enhanced entropy</b>: measurement bits from a QPanda Shor period-finding circuit "
                 "(QPE) are whitened through THASH-256 and fed into key derivation."),
                ("<b>完整性与分发</b>：TMAC 认证、条目 CRC 校验、路径穿越防护；元数据全部在密文内，"
                 "头部零泄露；静态单文件，Windows / Linux 开箱即用。",
                 "<b>Integrity and shipping</b>: TMAC authentication, per-entry CRC verification and "
                 "path-traversal defence; all metadata lives inside the ciphertext so the header leaks "
                 "nothing; one statically linked file for Windows and Linux."),
            ]},
            {"h": ("用法与安全声明", "Usage and security notice"), "p": [
                ("<code>tet pack &lt;目录&gt;</code> 压缩 + 加密为 <code>.tet</code> 容器（自动生成密钥）、"
                 "<code>tet unpack</code> 解密解压、<code>tet keygen</code> 生成 T-IES 密钥对、"
                 "<code>tet info</code> 查看容器信息（不泄露内容）。",
                 "<code>tet pack &lt;dir&gt;</code> compresses and encrypts into a <code>.tet</code> container "
                 "(generating a key), <code>tet unpack</code> decrypts and restores, <code>tet keygen</code> "
                 "creates a T-IES key pair, and <code>tet info</code> reports container metadata without "
                 "revealing contents."),
                ("<b>安全性说明（作者原话，原样保留）</b>：本项目为自研算法的实验性实现，THASH-256、"
                 "TStream、TMAC、T-IES 均为本项目原创构造，<b>未经过第三方密码分析与审计</b>，"
                 "不应用于生产环境的高价值数据保护。",
                 "<b>Security notice (the author's own words)</b>: this is an experimental implementation of "
                 "in-house algorithms — THASH-256, TStream, TMAC and T-IES are original constructions that "
                 "have <b>not been third-party cryptanalysed or audited</b>, and should not be used to protect "
                 "high-value production data."),
            ]},
        ],
        "downloads": {
            "version": "v0.1.0",
            "assets": [
                ("tetsuhiror-v0.1.0-linux-amd64", "Linux x86-64（静态链接 / static）"),
                ("tetsuhiror-v0.1.0-windows-amd64.exe", "Windows x86-64"),
            ],
            "cmds": [
                "# 压缩 + 加密（自动生成密钥）/ pack with a generated key\n./tet pack mydir",
                "# 解密 + 解压 / unpack\n./tet unpack mydir.tet -k mydir.tet.key -d /target/dir",
                "./tet info mydir.tet",
                "# 从源码构建 / from source\ngit clone https://github.com/ZhehaoTetsuhiro/Tetsuhiror.git\n"
                "cd Tetsuhiror && go build -o tet ./cmd/tet",
            ],
            "note_zh": "只做「加/解压」这件事：没有安装器、没有依赖，单文件跑。"
                       "量子熵源需要 QPanda 环境（README 的「QPanda 环境搭建」一节）。",
            "note_en": "It does one thing — pack and unpack — as a single file with no installer and no "
                       "dependencies. The quantum entropy source needs a QPanda environment (see the "
                       "“QPanda environment” section of the README).",
        },
    },
]
