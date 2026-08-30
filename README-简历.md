# RST 竞赛训练营 · 入营筛选赛题提交

**作者：杨豫豪（YYH）**
**学校 / 专业：河南城建学院 · 环境工程专业（2026级）**
**联系方式：177 1989 1195 ｜ 2813573523@qq.com ｜ 河南郑州**

---

# 必做题：个人在线简历

## 🌐 在线访问地址（已部署上线 · 加分项）

https://yanghao158640.github.io/competition-bootcamp/

## 📁 文件结构

```
├── index.html        个人在线简历（单文件，零外部依赖，双击即可离线运行）
├── 1.jpg ~ 8.jpg     本人 AI 领域证书图片素材（画廊 + 灯箱展示）
├── netlify.toml      Netlify 部署配置文件
└── README.md         本说明文档（文末附 index.html 完整源代码）
```

## ✅ 完成情况

- **内容完整**：基本信息（姓名/电话/邮箱/学校专业）、教育背景、实践经历、
  项目经历、技能矩阵、特长爱好、获奖证书、联系方式；
- **响应式设计**：适配 PC 与移动端（汉堡菜单、弹性网格、多级断点）；
- **代码规范**：语义化标签、ARIA 无障碍属性、结构注释清晰；
- **交互与创意（加分项）**：深浅主题切换并记忆偏好、选项卡键盘操作、
  证书画廊 + 灯箱（左右/滑动/键盘切换）、一键复制邮箱 + Toast、
  返回顶部、平滑滚动、打印样式优化；
- **图片素材（加分项）**：页面插入 8 张本人 AI 领域证书图片；
- **线上部署（加分项）**：已部署上线，网址见上方。

## 🗺️ 源代码导读（index.html）

| 部分 | 内容 |
|---|---|
| `<style>` | CSS 变量双主题（`:root` / `[data-theme="dark"]`）、响应式媒体查询、打印样式 |
| `<header>` | Hero 区：姓名、学校专业、联系方式、统计卡片 |
| `section#about / #edu` | 关于我、教育背景（高考 493 分 / 全省前 20%） |
| `section#experience` | 实践经历（选项卡：主持队 / 文娱部 / AI 工具实践） |
| `section#skills` | 技能矩阵：7+ 款 AI 工具标签墙 |
| `section#gallery / #certs` | 证书画廊（灯箱）+ 8 项 AI 认证清单 |
| `<script>` | 主题切换、选项卡、灯箱、灯箱键盘/触摸导航、复制邮箱、滚动监听 |

---

## 📖 index.html 完整源代码

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>杨豫豪 - 个人简历</title>

    <!-- 字体改为系统字体栈, 去除 Google Fonts 外部依赖(微信内更稳定) -->
    <!-- Tailwind CSS (本地预编译, 微信内无外部 CDN 依赖) -->
    <link rel="stylesheet" href="tailwind.css">

    <!-- Lucide Icons (本地同源) -->
    <script src="lucide.js"></script>

    <style>
        /* ===== Base ===== */
        html { scroll-behavior: smooth; }
        body { font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif; }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.3); border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.5); }

        /* ===== Glow blobs ===== */
        .glow-blob-1 {
            position: fixed;
            top: -120px;
            left: -120px;
            width: 600px;
            height: 600px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(6, 182, 212, 0.12), transparent 70%);
            filter: blur(140px);
            pointer-events: none;
            z-index: 0;
            animation: float 8s ease-in-out infinite alternate;
        }
        .glow-blob-2 {
            position: fixed;
            bottom: -160px;
            right: -120px;
            width: 550px;
            height: 550px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1), transparent 70%);
            filter: blur(140px);
            pointer-events: none;
            z-index: 0;
            animation: float 10s ease-in-out infinite alternate-reverse;
        }

        /* ===== Dynamic Canvas Background (dark glow + waves) ===== */
        #bgCanvas {
            position: fixed;
            inset: 0;
            width: 100%;
            height: 100%;
            display: block;
            z-index: 0;
            pointer-events: none;
        }

        /* ===== Reveal scroll animation ===== */
        .reveal {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1), transform 0.7s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .reveal-d1 { transition-delay: 0.08s; }
        .reveal-d2 { transition-delay: 0.16s; }
        .reveal-d3 { transition-delay: 0.24s; }
        .reveal-d4 { transition-delay: 0.32s; }

        /* ===== Lightbox ===== */
        .lightbox-overlay {
            position: fixed;
            inset: 0;
            z-index: 9999;
            background: rgba(3, 7, 18, 0.95);
            backdrop-filter: blur(20px);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.35s ease, visibility 0.35s ease;
        }
        .lightbox-overlay.active {
            opacity: 1;
            visibility: visible;
        }
        .lightbox-overlay img {
            max-width: 90vw;
            max-height: 85vh;
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
            transform: scale(0.92);
            transition: transform 0.4s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .lightbox-overlay.active img {
            transform: scale(1);
        }

        /* ===== Tabs ===== */
        .tab-btn {
            transition: all 0.25s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .tab-btn[aria-selected="true"] {
            background: rgba(6, 182, 212, 0.15);
            border-color: rgba(6, 182, 212, 0.3);
            color: #22d3ee;
        }

        /* ===== Skill bar ===== */
        .skill-bar-track {
            background: rgba(51, 65, 85, 0.4);
            border-radius: 999px;
            height: 8px;
            overflow: hidden;
        }
        .skill-bar-fill {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #06b6d4, #22d3ee);
            transition: width 0.8s cubic-bezier(0.22, 0.61, 0.36, 1);
            position: relative;
        }
        .skill-bar-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
            animation: shimmer 2.5s infinite;
        }
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }

        /* ===== Gallery hover ===== */
        .gallery-item {
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            cursor: pointer;
            aspect-ratio: 4 / 3;
            border: 1px solid rgba(255, 255, 255, 0.06);
            transition: all 0.35s cubic-bezier(0.22, 1, 0.36, 1);
        }
        .gallery-item:hover {
            transform: scale(1.03);
            border-color: rgba(6, 182, 212, 0.3);
            box-shadow: 0 12px 40px rgba(6, 182, 212, 0.15);
        }
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        .gallery-item:hover img {
            transform: scale(1.08);
        }
        .gallery-item .gallery-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(0deg, rgba(3, 7, 18, 0.6) 0%, transparent 50%);
            opacity: 0;
            transition: opacity 0.3s ease;
            display: flex;
            align-items: flex-end;
            padding: 12px;
        }
        .gallery-item:hover .gallery-overlay {
            opacity: 1;
        }

        /* ===== Mobile nav ===== */
        .nav-mobile {
            position: fixed;
            top: 0;
            right: 0;
            width: 260px;
            height: 100vh;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(20px);
            border-left: 1px solid rgba(255, 255, 255, 0.06);
            transform: translateX(100%);
            transition: transform 0.35s cubic-bezier(0.22, 1, 0.36, 1);
            z-index: 9998;
            padding: 80px 24px 24px;
        }
        .nav-mobile.open {
            transform: translateX(0);
        }
        .nav-overlay {
            position: fixed;
            inset: 0;
            background: rgba(3, 7, 18, 0.6);
            z-index: 9997;
            opacity: 0;
            visibility: hidden;
            transition: all 0.35s ease;
        }
        .nav-overlay.open {
            opacity: 1;
            visibility: visible;
        }

        /* ===== Toast ===== */
        .toast-container {
            position: fixed;
            bottom: 32px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 99999;
            pointer-events: none;
        }

        /* ===== Print ===== */
        @media print {
            .glow-blob-1, .glow-blob-2, .lightbox-overlay, .toast-container,
            .nav-mobile, .nav-overlay, .hamburger-btn { display: none !important; }
            body { background: #fff !important; color: #1e293b !important; }
            .glass-card { background: #fff !important; border: 1px solid #e2e8f0 !important; backdrop-filter: none !important; }
            .reveal { opacity: 1 !important; transform: none !important; }
            .text-slate-300, .text-slate-400 { color: #64748b !important; }
            .text-white { color: #1e293b !important; }
            .text-cyan-400 { color: #0891b2 !important; }
        }
        @media (prefers-reduced-motion: reduce) {
            .glow-blob-1, .glow-blob-2 { animation: none !important; }
            .reveal { opacity: 1 !important; transform: none !important; transition: none !important; }
            .gallery-item:hover img { transform: none !important; }
            .skill-bar-fill::after { animation: none !important; }
        }
    </style>
</head>

<body class="bg-[#030712] text-slate-200 font-jakarta min-h-screen overflow-x-hidden relative">

    <!-- ===== Dynamic Background (dark glow + waves) ===== -->
    <canvas id="bgCanvas" aria-hidden="true"></canvas>

    <!-- ===== Background Glow Blobs ===== -->
    <div class="glow-blob-1" aria-hidden="true"></div>
    <div class="glow-blob-2" aria-hidden="true"></div>

    <!-- ===== Mobile Nav Overlay ===== -->
    <div class="nav-overlay" id="navOverlay" aria-hidden="true"></div>

    <!-- ===== Mobile Nav ===== -->
    <nav class="nav-mobile" id="navMobile" aria-label="移动端导航">
        <div class="flex flex-col gap-2">
            <a href="#hero" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">首页</a>
            <a href="#experience" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">经历</a>
            <a href="#projects" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">项目</a>
            <a href="#skills" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">技能</a>
            <a href="#gallery" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">掠影</a>
            <a href="#contact" class="nav-mobile-link block px-4 py-3 rounded-xl text-slate-300 hover:text-white hover:bg-white/5 transition-all">联系</a>
        </div>
    </nav>

    <!-- ===== Navbar ===== -->
    <header class="fixed top-0 left-0 right-0 z-50 bg-[#030712]/80 backdrop-blur-xl border-b border-white/5">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="#hero" class="text-white font-extrabold text-lg tracking-tight">
                YYH<span class="text-cyan-400">.</span>
            </a>
            <!-- Desktop Nav -->
            <nav class="hidden md:flex items-center gap-1" aria-label="主导航">
                <a href="#hero" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">首页</a>
                <a href="#experience" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">经历</a>
                <a href="#projects" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">项目</a>
                <a href="#skills" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">技能</a>
                <a href="#gallery" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">掠影</a>
                <a href="#contact" class="nav-link px-4 py-2 rounded-xl text-sm text-slate-400 hover:text-white hover:bg-white/5 transition-all">联系</a>
            </nav>
            <!-- Hamburger -->
            <button class="md:hidden hamburger-btn w-10 h-10 flex flex-col items-center justify-center gap-1.5 rounded-xl hover:bg-white/5 transition-all" id="hamburgerBtn" aria-label="展开菜单" aria-expanded="false">
                <span class="block w-5 h-0.5 bg-slate-300 rounded transition-all duration-300"></span>
                <span class="block w-5 h-0.5 bg-slate-300 rounded transition-all duration-300"></span>
                <span class="block w-5 h-0.5 bg-slate-300 rounded transition-all duration-300"></span>
            </button>
        </div>
    </header>

    <!-- ===== Main Content ===== -->
    <main class="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 pt-28 pb-20">

        <!-- ========== HERO ========== -->
        <section id="hero" class="reveal">
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-8 sm:p-12 text-center">
                <!-- Avatar -->
                <div class="w-20 h-20 mx-auto mb-5 rounded-full bg-gradient-to-br from-cyan-400 to-indigo-500 flex items-center justify-center text-2xl font-extrabold text-white shadow-lg shadow-cyan-500/20">
                    杨
                </div>
                <!-- Name -->
                <h1 class="text-3xl sm:text-4xl font-extrabold text-white mb-2">杨豫豪</h1>
                <!-- Subtitle -->
                <p class="text-cyan-400 font-semibold text-lg mb-3">环境工程专业 · AI 技术探索者</p>
                <!-- Divider -->
                <div class="w-16 h-1 bg-gradient-to-r from-cyan-400 to-indigo-500 rounded-full mx-auto mb-5"></div>
                <!-- Contact row -->
                <div class="flex flex-wrap justify-center gap-x-6 gap-y-2 text-sm text-slate-400 mb-4">
                    <span class="inline-flex items-center gap-1.5"><i data-lucide="phone" class="w-3.5 h-3.5 text-cyan-400/70"></i>17719891195</span>
                    <span class="inline-flex items-center gap-1.5"><i data-lucide="mail" class="w-3.5 h-3.5 text-cyan-400/70"></i>2813573523@qq.com</span>
                    <span class="inline-flex items-center gap-1.5"><i data-lucide="map-pin" class="w-3.5 h-3.5 text-cyan-400/70"></i>河南郑州</span>
                </div>
                <!-- Tags -->
                <div class="flex flex-wrap justify-center gap-2">
                    <span class="px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">河南城建学院</span>
                    <span class="px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">2026级</span>
                    <span class="px-3 py-1 rounded-full text-xs font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">高考493分</span>
                </div>
                <!-- Professional Summary -->
                <div class="mt-6 pt-5 border-t border-white/5">
                    <p class="text-sm text-slate-300 leading-relaxed max-w-2xl mx-auto">
                        环境工程专业本科生，辅修<span class="text-cyan-300 font-medium">AI工具应用</span>方向。
                        熟练运用 <span class="text-cyan-300 font-medium">7+</span> 款AI工具，持有 <span class="text-cyan-300 font-medium">8</span> 项AI领域认证。
                        具备 Python 脚本开发、小游戏制作、海报设计等实践能力，能快速上手新技术并产出落地成果。
                    </p>
                </div>
            </div>
        </section>

        <!-- ========== HIGHLIGHTS ========== -->
        <section id="highlights" class="mt-6 reveal">
            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4">
                <div class="highlight-card glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-xl p-5 text-center hover:-translate-y-1 hover:shadow-lg hover:shadow-cyan-500/10 transition-all duration-300">
                    <div class="text-2xl sm:text-3xl font-extrabold bg-gradient-to-r from-cyan-400 to-indigo-400 bg-clip-text text-transparent">7+</div>
                    <div class="text-xs text-slate-400 mt-1">款AI工具熟练运用</div>
                </div>
                <div class="highlight-card glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-xl p-5 text-center hover:-translate-y-1 hover:shadow-lg hover:shadow-cyan-500/10 transition-all duration-300">
                    <div class="text-2xl sm:text-3xl font-extrabold bg-gradient-to-r from-cyan-400 to-indigo-400 bg-clip-text text-transparent">8</div>
                    <div class="text-xs text-slate-400 mt-1">项AI领域认证</div>
                </div>
                <div class="highlight-card glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-xl p-5 text-center hover:-translate-y-1 hover:shadow-lg hover:shadow-cyan-500/10 transition-all duration-300">
                    <div class="text-2xl sm:text-3xl font-extrabold bg-gradient-to-r from-cyan-400 to-indigo-400 bg-clip-text text-transparent">多个</div>
                    <div class="text-xs text-slate-400 mt-1">Python实践项目</div>
                </div>
                <div class="highlight-card glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-xl p-5 text-center hover:-translate-y-1 hover:shadow-lg hover:shadow-cyan-500/10 transition-all duration-300">
                    <div class="text-2xl sm:text-3xl font-extrabold bg-gradient-to-r from-cyan-400 to-indigo-400 bg-clip-text text-transparent">1篇+</div>
                    <div class="text-xs text-slate-400 mt-1">文章被校内文学社刊采用</div>
                </div>
            </div>
        </section>

        <!-- ========== EXPERIENCE ========== -->
        <section id="experience" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="briefcase" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">经历</h2>
            </div>
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl overflow-hidden">
                <!-- Tabs -->
                <div class="flex border-b border-white/5" role="tablist" id="expTabs">
                    <button class="tab-btn flex-1 px-4 py-3.5 text-sm font-medium text-slate-400 border-b-2 border-transparent" role="tab" aria-selected="true" aria-controls="expPanel0">
                        <i data-lucide="code" class="w-4 h-4 inline-block mr-1.5"></i>实践经历
                    </button>
                    <button class="tab-btn flex-1 px-4 py-3.5 text-sm font-medium text-slate-400 border-b-2 border-transparent" role="tab" aria-selected="false" aria-controls="expPanel1">
                        <i data-lucide="book-open" class="w-4 h-4 inline-block mr-1.5"></i>教育背景
                    </button>
                </div>
                <!-- Panels -->
                <div>
                    <div class="p-5 sm:p-6" role="tabpanel" id="expPanel0">
                        <div class="space-y-4">
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                    <div class="w-px flex-1 bg-gradient-to-b from-cyan-500/20 to-transparent"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">Python脚本开发</h3>
                                    <p class="text-sm text-slate-400 mt-1">借助AI工具完成自动化脚本，按文件类型自动归类，提升日常文件管理效率，将AI能力转化为实际生产力。</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                    <div class="w-px flex-1 bg-gradient-to-b from-cyan-500/20 to-transparent"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">AI工具应用实践</h3>
                                    <p class="text-sm text-slate-400 mt-1">深度使用DeepSeek、Kimi、通义千问、豆包、Trae等AI工具，完成数据分析、写作辅助、工作流设计等多种任务。</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">海报设计与演示文稿制作</h3>
                                    <p class="text-sm text-slate-400 mt-1">利用AI辅助设计工具完成校园活动海报，独立完成多套演示文稿用于班级展示，获得积极反馈。</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="p-5 sm:p-6 hidden" role="tabpanel" id="expPanel1">
                        <div class="space-y-4">
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                    <div class="w-px flex-1 bg-gradient-to-b from-cyan-500/20 to-transparent"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">河南城建学院 · 环境工程专业</h3>
                                    <p class="text-sm text-slate-400 mt-1">2026级本科生 · 高考 493 分，全省位次前 20%</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                    <div class="w-px flex-1 bg-gradient-to-b from-cyan-500/20 to-transparent"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">吴恩达《机器学习》课程</h3>
                                    <p class="text-sm text-slate-400 mt-1">完成课程学习并获证书，掌握监督学习、无监督学习、神经网络等核心概念。</p>
                                </div>
                            </div>
                            <div class="flex gap-4">
                                <div class="hidden sm:flex flex-col items-center">
                                    <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 ring-4 ring-cyan-500/20 mt-1.5"></div>
                                </div>
                                <div class="flex-1">
                                    <h3 class="text-white font-semibold">8项AI领域专业认证</h3>
                                    <p class="text-sm text-slate-400 mt-1">讯飞星火Prompt Engineer、华为AI微认证、阿里达摩院高级人工智能训练师、Datawhale Agent Engineer等。</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========== PROJECTS ========== -->
        <section id="projects" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="folder-git-2" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">实践项目</h2>
            </div>
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl overflow-hidden">
                <!-- Tabs -->
                <div class="flex border-b border-white/5" role="tablist" id="projTabs">
                    <button class="tab-btn flex-1 px-4 py-3.5 text-sm font-medium text-slate-400 border-b-2 border-transparent" role="tab" aria-selected="true" aria-controls="projPanel0">
                        <i data-lucide="bot" class="w-4 h-4 inline-block mr-1.5"></i>AI工具类
                    </button>
                    <button class="tab-btn flex-1 px-4 py-3.5 text-sm font-medium text-slate-400 border-b-2 border-transparent" role="tab" aria-selected="false" aria-controls="projPanel1">
                        <i data-lucide="palette" class="w-4 h-4 inline-block mr-1.5"></i>设计类
                    </button>
                    <button class="tab-btn flex-1 px-4 py-3.5 text-sm font-medium text-slate-400 border-b-2 border-transparent" role="tab" aria-selected="false" aria-controls="projPanel2">
                        <i data-lucide="globe" class="w-4 h-4 inline-block mr-1.5"></i>作品展示
                    </button>
                </div>
                <!-- Panels -->
                <div>
                    <div class="p-5 sm:p-6" role="tabpanel" id="projPanel0">
                        <div class="grid sm:grid-cols-2 gap-3">
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="folder" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">自动整理文件夹脚本</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Python</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Trae</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed">借助AI完成脚本，按文件类型自动归类，提升日常文件管理效率。</p>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="bar-chart-3" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">成绩统计分析工具</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Python</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Pandas</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed">支持多科目成绩录入、均分计算与排名生成，应用于实际学习场景。</p>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300 sm:col-span-2">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="pen-line" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">AI辅助写作工作流</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">DeepSeek</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Kimi</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed">设计AI辅助写作流程，产出读后感及时事评论，部分被校内文学社刊采用。</p>
                            </div>
                        </div>
                    </div>
                    <div class="p-5 sm:p-6 hidden" role="tabpanel" id="projPanel1">
                        <div class="grid sm:grid-cols-2 gap-3">
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="image" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">校园活动海报设计</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">AI辅助设计</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed">利用AI工具完成数套海报，用于校内活动宣传并获得积极反馈。</p>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="presentation" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">演示文稿制作</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">PowerPoint</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed">AI辅助生成大纲并优化排版，独立完成多套演示文稿用于班级展示。</p>
                            </div>
                        </div>
                    </div>
                    <div class="p-5 sm:p-6 hidden" role="tabpanel" id="projPanel2">
                        <div class="grid sm:grid-cols-2 gap-3">
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="gamepad-2" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">坦克大战小游戏</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">JavaScript</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Canvas</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed mb-2">用原生JS + Canvas实现的坦克大战游戏，支持键盘操控、敌人生成、碰撞检测。</p>
                                <a href="https://你的链接.netlify.app" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs text-cyan-400 hover:text-cyan-300 transition-colors" onclick="return confirm('请将链接替换为你的实际部署地址')">
                                    <i data-lucide="external-link" class="w-3 h-3"></i>在线试玩
                                </a>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="presentation" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">PPT作品集</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">PowerPoint</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">AI辅助</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed mb-2">AI辅助生成的演示文稿，涵盖校园活动、学习汇报等主题，排版精美逻辑清晰。</p>
                                <a href="https://你的链接.netlify.app" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-1 text-xs text-cyan-400 hover:text-cyan-300 transition-colors" onclick="return confirm('请将链接替换为你的实际部署地址')">
                                    <i data-lucide="external-link" class="w-3 h-3"></i>在线查看
                                </a>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="file-text" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">个人简历网站</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Tailwind</span>
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">Lucide</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed mb-2">本简历网站，采用Tailwind CSS + Lucide图标 + Google Fonts构建，完全响应式。</p>
                                <span class="inline-flex items-center gap-1 text-xs text-cyan-400/60">
                                    <i data-lucide="check-circle" class="w-3 h-3"></i>当前页面
                                </span>
                            </div>
                            <div class="project-card bg-white/5 border border-white/10 rounded-xl p-4 hover:bg-white/[0.07] hover:border-cyan-500/20 hover:-translate-y-0.5 transition-all duration-300">
                                <div class="flex items-center gap-2 mb-2">
                                    <i data-lucide="plus" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                                    <h3 class="text-white font-semibold text-sm">更多作品</h3>
                                </div>
                                <div class="flex flex-wrap gap-1.5 mb-2">
                                    <span class="px-2 py-0.5 rounded-full text-[11px] font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">持续更新</span>
                                </div>
                                <p class="text-xs text-slate-400 leading-relaxed mb-2">更多作品持续部署中，后续将在此补充Netlify展示链接。</p>
                                <span class="inline-flex items-center gap-1 text-xs text-slate-500">
                                    <i data-lucide="clock" class="w-3 h-3"></i>即将上线
                                </span>
                            </div>
                        </div>
                    </div>
            </div>
        </section>

        <!-- ========== SKILLS ========== -->
        <section id="skills" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="zap" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">技能矩阵</h2>
            </div>
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-5 sm:p-6">
                <div class="grid sm:grid-cols-2 gap-x-8 gap-y-4">
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">AI工具应用</span>
                            <span class="text-cyan-400 font-semibold">90%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:90%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">海报设计</span>
                            <span class="text-cyan-400 font-semibold">80%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:80%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">写作能力</span>
                            <span class="text-cyan-400 font-semibold">80%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:80%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">演示文稿 / PPT制作</span>
                            <span class="text-cyan-400 font-semibold">80%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:80%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">Python编程</span>
                            <span class="text-cyan-400 font-semibold">60%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:60%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">数据分析</span>
                            <span class="text-cyan-400 font-semibold">55%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:55%"></div></div>
                    </div>
                    <div class="skill-item">
                        <div class="flex justify-between text-sm mb-1.5">
                            <span class="text-slate-300">小游戏制作</span>
                            <span class="text-cyan-400 font-semibold">50%</span>
                        </div>
                        <div class="skill-bar-track"><div class="skill-bar-fill" style="width:50%"></div></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ========== HOBBIES ========== -->
        <section id="hobbies" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="heart" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">特长与爱好</h2>
            </div>
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-5 sm:p-6">
                <div class="flex flex-wrap gap-2.5">
                    <span class="tag px-4 py-1.5 rounded-full text-sm font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20 hover:border-cyan-400/30 transition-all duration-300">写作</span>
                    <span class="tag px-4 py-1.5 rounded-full text-sm font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20 hover:border-cyan-400/30 transition-all duration-300">海报设计</span>
                    <span class="tag px-4 py-1.5 rounded-full text-sm font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20 hover:border-cyan-400/30 transition-all duration-300">Python</span>
                    <span class="tag px-4 py-1.5 rounded-full text-sm font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20 hover:border-cyan-400/30 transition-all duration-300">AI工具探索</span>
                    <span class="tag px-4 py-1.5 rounded-full text-sm font-medium bg-cyan-500/10 border border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20 hover:border-cyan-400/30 transition-all duration-300">阅读</span>
                </div>
            </div>
        </section>

        <!-- ========== GALLERY ========== -->
        <section id="gallery" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="images" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">个人掠影</h2>
            </div>
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-5 sm:p-6">
                <div class="grid grid-cols-2 sm:grid-cols-4 gap-3" id="mainGalleryGrid"></div>
            </div>
        </section>

        <!-- ========== CERTS ========== -->
        <section id="certs" class="mt-10 reveal">
            <div class="flex items-center gap-3 mb-5">
                <i data-lucide="award" class="w-5 h-5 text-cyan-400"></i>
                <h2 class="text-xl font-extrabold text-white">获奖与证书</h2>
            </div>
            <div class="grid sm:grid-cols-2 gap-4">
                <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-5 sm:p-6">
                    <h3 class="text-white font-semibold text-sm mb-3 flex items-center gap-2">
                        <i data-lucide="list" class="w-4 h-4 text-cyan-400"></i>证书列表
                    </h3>
                    <ul class="space-y-2" id="certList"></ul>
                </div>
                <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-5 sm:p-6">
                    <h3 class="text-white font-semibold text-sm mb-3 flex items-center gap-2">
                        <i data-lucide="image" class="w-4 h-4 text-cyan-400"></i>证书展示
                    </h3>
                    <div class="grid grid-cols-2 gap-2" id="certGalleryGrid"></div>
                </div>
            </div>
        </section>

        <!-- ========== CONTACT ========== -->
        <section id="contact" class="mt-10 reveal">
            <div class="glass-card bg-slate-900/50 backdrop-blur-xl border border-white/10 rounded-2xl p-8 sm:p-10 text-center">
                <i data-lucide="send" class="w-8 h-8 text-cyan-400 mx-auto mb-4"></i>
                <h2 class="text-2xl font-extrabold text-white mb-2">联系我</h2>
                <p class="text-slate-400 text-sm mb-6">如果有任何机会或合作意向，欢迎联系</p>
                <div class="flex flex-wrap justify-center gap-3 mb-4">
                    <span class="inline-flex items-center gap-2 text-sm text-slate-300 bg-white/5 px-4 py-2 rounded-xl border border-white/5">
                        <i data-lucide="phone" class="w-4 h-4 text-cyan-400"></i>17719891195
                    </span>
                    <span class="inline-flex items-center gap-2 text-sm text-slate-300 bg-white/5 px-4 py-2 rounded-xl border border-white/5">
                        <i data-lucide="mail" class="w-4 h-4 text-cyan-400"></i>2813573523@qq.com
                    </span>
                </div>
                <button id="copyEmailBtn" class="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl text-sm font-semibold text-white bg-gradient-to-r from-cyan-500 to-cyan-600 hover:from-cyan-400 hover:to-cyan-500 shadow-lg shadow-cyan-500/20 hover:shadow-cyan-500/40 transition-all duration-300 active:scale-95">
                    <i data-lucide="copy" class="w-4 h-4"></i>一键复制邮箱
                </button>
            </div>
        </section>

    </main>

    <!-- ===== Footer ===== -->
    <footer class="relative z-10 border-t border-white/5 py-6 text-center">
        <p class="text-xs text-slate-500">&copy; 2026 杨豫豪 | 更新于 2026年8月 | 此简历为个人学习与求职用途</p>
    </footer>

    <!-- ===== Lightbox ===== -->
    <div class="lightbox-overlay" id="lightbox" role="dialog" aria-label="图片查看器">
        <button class="absolute top-4 right-4 w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white transition-all z-10" id="lightboxClose" aria-label="关闭">
            <i data-lucide="x" class="w-5 h-5"></i>
        </button>
        <button class="absolute left-4 top-1/2 -translate-y-1/2 w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white transition-all z-10" id="lightboxPrev" aria-label="上一张">
            <i data-lucide="chevron-left" class="w-5 h-5"></i>
        </button>
        <button class="absolute right-4 top-1/2 -translate-y-1/2 w-10 h-10 flex items-center justify-center rounded-full bg-white/10 hover:bg-white/20 text-white transition-all z-10" id="lightboxNext" aria-label="下一张">
            <i data-lucide="chevron-right" class="w-5 h-5"></i>
        </button>
        <img id="lightboxImg" src="" alt="证书大图">
        <div class="absolute bottom-6 left-1/2 -translate-x-1/2 text-sm text-white/60" id="lightboxCounter"></div>
    </div>

    <!-- ===== Toast ===== -->
    <div class="toast-container" id="toastContainer">
        <div id="toast" class="pointer-events-auto px-5 py-3 rounded-xl bg-slate-800/90 backdrop-blur-xl border border-white/10 shadow-2xl shadow-black/50 text-sm text-slate-200 flex items-center gap-2.5 opacity-0 translate-y-4 scale-95 transition-all duration-400" style="transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);">
            <i data-lucide="check-circle" class="w-4 h-4 text-cyan-400 shrink-0"></i>
            <span id="toastMsg"></span>
        </div>
    </div>

    <!-- ===== JavaScript ===== -->
    <script src="lucide.js"></script>
    <script>
        (function() {
            'use strict';

            const resume = {
                name: '杨豫豪',
                email: '2813573523@qq.com',
                phone: '17719891195',
                location: '河南郑州',
                university: '河南城建学院',
                major: '环境工程',
            };

            const galleryImages = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg'];
            let currentLightboxIndex = -1;

            // ===== All certificates =====
            const certNames = [
                'Datawhale & 科大讯飞联合颁发的 Prompt Engineer 证书',
                '华为人工智能初识微认证',
                '阿里达摩院高级人工智能训练师',
                'Datawhale & 文付宝百宝箱联合颁发的 Agent Engineer 能力认证证书',
                'Datawhale & 豆包 MarsCode 联合颁发的 AI + 编程能力认证证书',
                '国际培训中心（ITCILO）人工智能证书',
                'Datawhale & 科大讯飞星愿 MaaS 平台联合颁发的 Fine-tuning Engineer 能力认证证书',
                '玻尔「AI4S Cup - Python 基础能力认证」AI 证书'
            ];

            // // ===== Render functions =====
            function renderMainGallery() {
                const grid = document.getElementById('mainGalleryGrid');
                if (!grid) return;
                grid.innerHTML = galleryImages.map((f, i) =>
                    `<div class="gallery-item" data-index="${i}" tabindex="0" role="button" aria-label="查看图片 ${i+1}">
                        <img src="${f}" alt="证书图片 ${i+1}" loading="lazy">
                        <div class="gallery-overlay">
                            <span class="text-xs text-white/80 font-medium">点击查看</span>
                        </div>
                    </div>`
                ).join('');
                grid.querySelectorAll('.gallery-item').forEach(el => {
                    el.addEventListener('click', () => openLightbox(parseInt(el.dataset.index)));
                    el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault();
                            openLightbox(parseInt(el.dataset.index)); } });
                });
            }

            function renderCertSideGallery() {
                const grid = document.getElementById('certGalleryGrid');
                if (!grid) return;
                grid.innerHTML = galleryImages.map((f, i) =>
                    `<div class="gallery-item cursor-pointer" data-index="${i}" tabindex="0" role="button" aria-label="证书 ${i+1}">
                        <img src="${f}" alt="证书 ${i+1}" loading="lazy">
                    </div>`
                ).join('');
                grid.querySelectorAll('.gallery-item').forEach(el => {
                    el.addEventListener('click', () => openLightbox(parseInt(el.dataset.index)));
                    el.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault();
                            openLightbox(parseInt(el.dataset.index)); } });
                });
            }

            function renderCertList() {
                const list = document.getElementById('certList');
                if (!list) return;
                list.innerHTML = certNames.map((name, i) =>
                    `<li class="flex items-center gap-2.5 text-sm text-slate-300 bg-white/[0.03] border border-white/5 rounded-lg px-3.5 py-2.5 hover:bg-cyan-500/5 hover:border-cyan-500/20 transition-all duration-300 cursor-default">
                        <i data-lucide="badge-check" class="w-4 h-4 text-cyan-400 shrink-0"></i>
                        <span>${name}</span>
                    </li>`
                ).join('');
                if (typeof lucide !== 'undefined') lucide.createIcons();
            }

            // ===== Lightbox =====
            function openLightbox(index) {
                currentLightboxIndex = index;
                const lb = document.getElementById('lightbox');
                const img = document.getElementById('lightboxImg');
                const counter = document.getElementById('lightboxCounter');
                if (!lb || !img) return;
                img.src = galleryImages[index];
                img.alt = '证书图片 ' + (index + 1);
                counter.textContent = (index + 1) + ' / ' + galleryImages.length;
                lb.classList.add('active');
                document.body.style.overflow = 'hidden';
                renderLbIcons();
            }

            function closeLightbox() {
                const lb = document.getElementById('lightbox');
                if (!lb) return;
                lb.classList.remove('active');
                document.body.style.overflow = '';
                currentLightboxIndex = -1;
            }

            function showPrevImage() {
                if (currentLightboxIndex > 0) openLightbox(currentLightboxIndex - 1);
                else openLightbox(galleryImages.length - 1);
            }

            function showNextImage() {
                if (currentLightboxIndex < galleryImages.length - 1) openLightbox(currentLightboxIndex + 1);
                else openLightbox(0);
            }

            function renderLbIcons() {
                setTimeout(() => { if (typeof lucide !== 'undefined') lucide.createIcons(); }, 0);
            }

            // ===== Toast =====
            let toastTimer = null;

            function showToast(msg) {
                const toast = document.getElementById('toast');
                const msgEl = document.getElementById('toastMsg');
                if (!toast || !msgEl) return;
                clearTimeout(toastTimer);
                msgEl.textContent = msg;
                toast.style.opacity = '1';
                toast.style.transform = 'translateY(0) scale(1)';
                if (typeof lucide !== 'undefined') lucide.createIcons();
                toastTimer = setTimeout(() => {
                    toast.style.opacity = '0';
                    toast.style.transform = 'translateY(16px) scale(0.95)';
                }, 2800);
            }

            function copyEmail() {
                const text = resume.email;
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(text).then(() => showToast('邮箱已复制到剪贴板')).catch(() => {
                        fallbackCopy(text);
                    });
                } else {
                    fallbackCopy(text);
                }
            }

            function fallbackCopy(text) {
                const ta = document.createElement('textarea');
                ta.value = text;
                ta.style.position = 'fixed';
                ta.style.opacity = '0';
                document.body.appendChild(ta);
                ta.select();
                try {
                    document.execCommand('copy');
                    showToast('邮箱已复制到剪贴板');
                } catch (e) {
                    showToast('复制失败，请手动复制');
                }
                document.body.removeChild(ta);
            }

            // ===== Tabs =====
            function initTabs(id) {
                const container = document.getElementById(id);
                if (!container) return;
                const tabs = container.querySelectorAll('[role="tab"]');
                const panels = [];
                tabs.forEach(t => {
                    const p = document.getElementById(t.getAttribute('aria-controls'));
                    if (p) panels.push(p);
                });

                function switchTab(i) {
                    tabs.forEach((t, j) => {
                        t.setAttribute('aria-selected', j === i);
                        t.classList.toggle('text-cyan-400', j === i);
                        t.classList.toggle('text-slate-400', j !== i);
                        t.style.borderBottomColor = j === i ? 'rgba(6,182,212,0.5)' : 'transparent';
                    });
                    panels.forEach((p, j) => {
                        p.classList.toggle('hidden', j !== i);
                    });
                }

                tabs.forEach((tab, i) => {
                    tab.addEventListener('click', () => switchTab(i));
                    tab.addEventListener('keydown', e => {
                        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
                            e.preventDefault();
                            switchTab((i + 1) % tabs.length);
                            tabs[(i + 1) % tabs.length].focus();
                        } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
                            e.preventDefault();
                            switchTab((i - 1 + tabs.length) % tabs.length);
                            tabs[(i - 1 + tabs.length) % tabs.length].focus();
                        }
                    });
                });
                switchTab(0);
            }

            // ===== Nav scroll =====
            document.querySelectorAll('a[href^="#"]').forEach(a => {
                a.addEventListener('click', function(e) {
                    const href = this.getAttribute('href');
                    if (href === '#') return;
                    e.preventDefault();
                    const t = document.getElementById(href.substring(1));
                    if (t) {
                        const nh = document.querySelector('header').offsetHeight;
                        window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - nh - 12,
                            behavior: 'smooth' });
                    }
                    // Close mobile nav
                    document.getElementById('navMobile')?.classList.remove('open');
                    document.getElementById('navOverlay')?.classList.remove('open');
                    document.getElementById('hamburgerBtn')?.setAttribute('aria-expanded', 'false');
                });
            });

            // ===== Mobile hamburger =====
            const hamburger = document.getElementById('hamburgerBtn');
            const navMobile = document.getElementById('navMobile');
            const navOverlay = document.getElementById('navOverlay');
            if (hamburger && navMobile && navOverlay) {
                hamburger.addEventListener('click', () => {
                    const open = navMobile.classList.toggle('open');
                    navOverlay.classList.toggle('open');
                    hamburger.setAttribute('aria-expanded', open);
                });
                navOverlay.addEventListener('click', () => {
                    navMobile.classList.remove('open');
                    navOverlay.classList.remove('open');
                    hamburger.setAttribute('aria-expanded', 'false');
                });
            }

            // ===== Lightbox events =====
            document.getElementById('lightboxClose')?.addEventListener('click', closeLightbox);
            document.getElementById('lightboxPrev')?.addEventListener('click', showPrevImage);
            document.getElementById('lightboxNext')?.addEventListener('click', showNextImage);
            document.getElementById('lightbox')?.addEventListener('click', function(e) {
                if (e.target === this) closeLightbox();
            });
            document.addEventListener('keydown', e => {
                if (document.getElementById('lightbox')?.classList.contains('active')) {
                    if (e.key === 'Escape') closeLightbox();
                    if (e.key === 'ArrowLeft') showPrevImage();
                    if (e.key === 'ArrowRight') showNextImage();
                }
            });

            // ===== Copy email =====
            document.getElementById('copyEmailBtn')?.addEventListener('click', copyEmail);

            // ===== Reveal scroll animations =====
            (function initReveal() {
                const els = document.querySelectorAll('.reveal, .glass-card, .project-card, .highlight-card, .skill-item, .tag, .gallery-item');
                if (!('IntersectionObserver' in window)) {
                    els.forEach(el => el.classList.add('visible'));
                    return;
                }
                const io = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                            io.unobserve(entry.target);
                        }
                    });
                }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
                els.forEach(el => io.observe(el));
            })();

            // ===== Init =====
            renderMainGallery();
            renderCertSideGallery();
            renderCertList();
            initTabs('expTabs');
            initTabs('projTabs');

            // Lucide icons
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }

            console.log('✅ 简历重构完毕 | 证书8项 | 图片8张 | Tailwind + Lucide 就绪');
        })();
    </script>

    <!-- ===== Dynamic Background Animation (dark glow + flowing waves) ===== -->
    <script>
        (function() {
            'use strict';
            const canvas = document.getElementById('bgCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            let W = 0,
                H = 0;
            const DPR = Math.min(window.devicePixelRatio || 1, 2);

            function resize() {
                W = window.innerWidth;
                H = window.innerHeight;
                canvas.width = W * DPR;
                canvas.height = H * DPR;
                ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
            }
            resize();
            window.addEventListener('resize', resize);

            // 慢动作光晕团: 位置(x,y)、半径、主色、相位
            const orbs = [
                { x: 0.18, y: 0.22, r: 0.45, hue: 190, ph: 0 },
                { x: 0.82, y: 0.30, r: 0.42, hue: 235, ph: 2.1 },
                { x: 0.60, y: 0.85, r: 0.50, hue: 265, ph: 4.2 },
                { x: 0.30, y: 0.75, r: 0.38, hue: 175, ph: 1.1 }
            ];

            // 流动波浪带参数
            const waves = [
                { amp: 0.05, speed: 0.28, lyr: 0.42, alpha: 0.16, hue: 188, off: 0 },
                { amp: 0.07, speed: -0.20, lyr: 0.58, alpha: 0.13, hue: 232, off: 2.6 },
                { amp: 0.04, speed: 0.34, lyr: 0.74, alpha: 0.11, hue: 262, off: 5.2 }
            ];

            let t = 0;

            function draw() {
                t += 0.016;
                ctx.clearRect(0, 0, W, H);
                const time = t;

                // 1) 流动波浪带 (aurora 风格的半透明正弦光带)
                waves.forEach(w => {
                    ctx.beginPath();
                    for (let x = 0; x <= W; x += 4) {
                        const p = x / W;
                        const y = H * (w.lyr + w.amp * Math.sin(p * Math.PI * 2.4 + time * w.speed + w.off) +
                            w.amp * 0.5 * Math.sin(p * Math.PI * 6 + time * w.speed * 1.7 + w.off * 2));
                        if (x === 0) ctx.moveTo(x, y);
                        else ctx.lineTo(x, y);
                    }
                    ctx.lineTo(W, H);
                    ctx.lineTo(0, H);
                    ctx.closePath();
                    const g = ctx.createLinearGradient(0, 0, 0, H);
                    g.addColorStop(0, 'hsla(' + w.hue + ', 85%, 55%, 0)');
                    g.addColorStop(0.08, 'hsla(' + w.hue + ', 85%, 55%, ' + w.alpha + ')');
                    g.addColorStop(w.lyr + 0.2, 'hsla(' + (w.hue + 30) + ', 80%, 60%, ' + (w.alpha * 0.4) + ')');
                    g.addColorStop(1, 'hsla(' + w.hue + ', 80%, 55%, 0)');
                    ctx.fillStyle = g;
                    ctx.fill();
                });

                // 2) 动态光晕 (缓慢漂移+呼吸的发光圆)
                ctx.globalCompositeOperation = 'lighter';
                orbs.forEach(o => {
                    const ox = W * (o.x + 0.055 * Math.sin(time * 0.22 + o.ph));
                    const oy = H * (o.y + 0.055 * Math.cos(time * 0.18 + o.ph * 1.3));
                    const r = Math.max(W, H) * o.r * (0.85 + 0.15 * Math.sin(time * 0.5 + o.ph));
                    const g = ctx.createRadialGradient(ox, oy, 0, ox, oy, r);
                    g.addColorStop(0, 'hsla(' + o.hue + ', 90%, 62%, 0.10)');
                    g.addColorStop(0.5, 'hsla(' + (o.hue + 20) + ', 85%, 58%, 0.05)');
                    g.addColorStop(1, 'hsla(' + o.hue + ', 85%, 55%, 0)');
                    ctx.fillStyle = g;
                    ctx.beginPath();
                    ctx.arc(ox, oy, r, 0, Math.PI * 2);
                    ctx.fill();
                });
                ctx.globalCompositeOperation = 'source-over';

                requestAnimationFrame(draw);
            }

            // 尊重用户减少动态偏好
            const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
            if (!reduce) draw();
        })();
    </script>

</body>
</html>
```

---

> 声明：本作品由本人独立完成，开发过程中使用 AI 工具辅助，符合赛事规定。
