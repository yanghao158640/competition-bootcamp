# RST 竞赛训练营 · 入营筛选赛题提交

**作者：杨豫豪（YYH）**
**学校 / 专业：河南城建学院 · 环境工程专业（2026级）**
**联系方式：177 1989 1195 ｜ 2813573523@qq.com ｜ 河南郑州**

---

# 必做题：个人在线简历

## 🌐 在线访问地址（已部署上线 · 加分项）

https://sweet-sunshine-cd0b26.netlify.app

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
<html lang="zh-CN" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>杨豫豪 - 个人简历</title>
    <!--
      ============================================================
      RST 竞赛训练营 · 必做题：个人在线简历
      作者：杨豫豪（YYH）  河南城建学院 · 环境工程（2026级）
      技术：纯原生 HTML / CSS / JavaScript，零外部依赖
      特性：响应式（PC/移动端）、深浅主题切换、选项卡交互、
            证书画廊 + 灯箱浏览、一键复制邮箱、打印优化
      ============================================================
    -->
    <style>
        :root {
            --bg: #eef2f8;
            --bg-card: rgba(255, 255, 255, 0.75);
            --bg-nav: rgba(255, 255, 255, 0.72);
            --text: #1a2540;
            --text-secondary: #5a6a8a;
            --text-muted: #94a3b8;
            --border: rgba(226, 232, 240, 0.7);
            --primary: #2563eb;
            --primary-light: #3b82f6;
            --accent: #0891b2;
            --accent-light: #06b6d4;
            --hero-bg: linear-gradient(135deg, #e0e7ff 0%, #dbeafe 30%, #cffafe 60%, #e0e7ff 100%);
            --card-shadow: 0 2px 8px rgba(37, 99, 235, 0.06), 0 1px 3px rgba(0, 0, 0, 0.04);
            --card-shadow-hover: 0 12px 32px rgba(37, 99, 235, 0.12), 0 4px 12px rgba(0, 0, 0, 0.06);
            --tag-bg: rgba(219, 234, 254, 0.7);
            --tag-text: #2563eb;
            --progress-bg: #e2e8f0;
            --progress-fill: linear-gradient(90deg, #2563eb, #06b6d4);
            --badge-outline: rgba(186, 230, 253, 0.6);
            --divider: rgba(241, 245, 249, 0.8);
            --hero-dot: rgba(59, 130, 246, 0.1);
            --nav-blur: blur(20px) saturate(180%);
            --tab-inactive: rgba(241, 245, 249, 0.6);
            --tab-hover: rgba(226, 232, 240, 0.8);
            --scrollbar-thumb: #94a3b8;
            --scrollbar-track: transparent;
            --gallery-placeholder: #e2e8f0;
            --lightbox-bg: rgba(8, 15, 35, 0.95);
            --tech-grid: rgba(37, 99, 235, 0.04);
            --tech-glow-1: rgba(59, 130, 246, 0.08);
            --tech-glow-2: rgba(6, 182, 212, 0.06);
            --tech-glow-3: rgba(139, 92, 246, 0.05);
            --card-border-glow: rgba(59, 130, 246, 0.12);
        }
        [data-theme="dark"] {
            --bg: #080d1e;
            --bg-card: rgba(20, 30, 55, 0.6);
            --bg-nav: rgba(8, 13, 30, 0.82);
            --text: #d6dfea;
            --text-secondary: #8b9bbf;
            --text-muted: #4a5a7a;
            --border: rgba(56, 78, 120, 0.35);
            --primary: #3b82f6;
            --primary-light: #60a5fa;
            --accent: #22d3ee;
            --accent-light: #67e8f9;
            --hero-bg: linear-gradient(135deg, #0a1228 0%, #0a1638 30%, #061a2e 60%, #0a1228 100%);
            --card-shadow: 0 2px 12px rgba(0, 0, 0, 0.4), 0 1px 4px rgba(0, 0, 0, 0.25);
            --card-shadow-hover: 0 12px 36px rgba(59, 130, 246, 0.15), 0 4px 12px rgba(0, 0, 0, 0.35);
            --tag-bg: rgba(30, 58, 95, 0.5);
            --tag-text: #93bbfd;
            --progress-bg: rgba(51, 65, 85, 0.6);
            --progress-fill: linear-gradient(90deg, #3b82f6, #22d3ee);
            --badge-outline: rgba(30, 58, 95, 0.6);
            --divider: rgba(30, 41, 59, 0.7);
            --hero-dot: rgba(96, 165, 250, 0.06);
            --nav-blur: blur(20px) saturate(180%);
            --tab-inactive: rgba(30, 41, 59, 0.5);
            --tab-hover: rgba(51, 65, 85, 0.6);
            --scrollbar-thumb: #3b4a6b;
            --scrollbar-track: transparent;
            --gallery-placeholder: #334155;
            --lightbox-bg: rgba(0, 0, 0, 0.96);
            --tech-grid: rgba(59, 130, 246, 0.06);
            --tech-glow-1: rgba(59, 130, 246, 0.1);
            --tech-glow-2: rgba(6, 182, 212, 0.08);
            --tech-glow-3: rgba(139, 92, 246, 0.07);
            --card-border-glow: rgba(59, 130, 246, 0.15);
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        html {
            scroll-behavior: smooth;
            scroll-padding-top: 80px;
        }
        @media (prefers-reduced-motion: reduce) {
            html {
                scroll-behavior: auto;
            }
            * {
                animation-duration: 0.01ms !important;
                transition-duration: 0.01ms !important;
            }
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.7;
            -webkit-font-smoothing: antialiased;
            transition: background-color 0.35s, color 0.35s;
            min-height: 100vh;
            overflow-x: hidden;
            position: relative;
        }
        /* 科技感动态网格背景 */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image:
                linear-gradient(var(--tech-grid) 1px, transparent 1px),
                linear-gradient(90deg, var(--tech-grid) 1px, transparent 1px);
            background-size: 48px 48px;
            pointer-events: none;
            z-index: 0;
            -webkit-mask-image: radial-gradient(ellipse 80% 60% at 50% 40%, #000 30%, transparent 100%);
            mask-image: radial-gradient(ellipse 80% 60% at 50% 40%, #000 30%, transparent 100%);
        }
        /* 科技感浮动光晕 */
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background:
                radial-gradient(circle at 15% 25%, var(--tech-glow-1), transparent 45%),
                radial-gradient(circle at 85% 35%, var(--tech-glow-2), transparent 40%),
                radial-gradient(circle at 50% 80%, var(--tech-glow-3), transparent 50%);
            pointer-events: none;
            z-index: 0;
            animation: glowDrift 20s ease-in-out infinite alternate;
        }
        @keyframes glowDrift {
            0%   { transform: translate(0, 0) scale(1); }
            50%  { transform: translate(-15px, 20px) scale(1.05); }
            100% { transform: translate(20px, -15px) scale(1); }
        }
        @media (prefers-reduced-motion: reduce) {
            body::after { animation: none; }
        }
        /* 噪点纹理叠层（通过独立div实现，不覆盖body::before网格） */
        .noise-overlay {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            z-index: 1;
            opacity: 0.035;
            mix-blend-mode: multiply;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
        }
        [data-theme="dark"] .noise-overlay {
            opacity: 0.05;
            mix-blend-mode: screen;
        }
        /* 光标跟随聚光灯 */
        .spotlight {
            position: fixed;
            top: 0;
            left: 0;
            width: 480px;
            height: 480px;
            border-radius: 50%;
            pointer-events: none;
            z-index: 2;
            background: radial-gradient(circle, var(--tech-glow-1) 0%, transparent 65%);
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: opacity 0.4s ease;
            mix-blend-mode: screen;
            will-change: transform;
        }
        body:hover .spotlight {
            opacity: 1;
        }
        @media (pointer: coarse) {
            .spotlight { display: none; }
        }
        /* 滚动进入动画基础 */
        .reveal {
            opacity: 0;
            transform: translateY(24px);
            transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1), transform 0.7s cubic-bezier(0.22, 1, 0.36, 1);
            will-change: transform, opacity;
        }
        .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .reveal-delay-1 { transition-delay: 0.08s; }
        .reveal-delay-2 { transition-delay: 0.16s; }
        .reveal-delay-3 { transition-delay: 0.24s; }
        .reveal-delay-4 { transition-delay: 0.32s; }
        /* 3D tilt 卡片容器 */
        .tilt-card {
            transform-style: preserve-3d;
            perspective: 900px;
            transition: transform 0.3s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.3s cubic-bezier(0.23, 1, 0.32, 1);
            will-change: transform;
        }
        .tilt-card .tilt-inner {
            transform: translateZ(24px);
            transform-style: preserve-3d;
        }
        /* 磁吸按钮 */
        .magnet-btn {
            transition: transform 0.15s cubic-bezier(0.23, 1, 0.32, 1), box-shadow 0.25s ease;
            will-change: transform;
        }
        /* 背景装饰线 */
        .deco-lines {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            z-index: 0;
            overflow: hidden;
            opacity: 0.4;
        }
        .deco-line {
            position: absolute;
            background: linear-gradient(90deg, transparent, var(--card-border-glow), transparent);
            height: 1px;
        }
        .deco-line:nth-child(1) { top: 18%; left: 0; width: 40%; animation: lineSlide 18s linear infinite; }
        .deco-line:nth-child(2) { top: 52%; right: 0; width: 35%; animation: lineSlide 22s linear infinite reverse; }
        .deco-line:nth-child(3) { top: 78%; left: 10%; width: 30%; animation: lineSlide 26s linear infinite; }
        .deco-line-v {
            position: absolute;
            background: linear-gradient(180deg, transparent, var(--card-border-glow), transparent);
            width: 1px;
        }
        .deco-line-v:nth-child(4) { left: 12%; top: 0; height: 30%; animation: lineSlideV 20s linear infinite; }
        .deco-line-v:nth-child(5) { right: 18%; top: 30%; height: 28%; animation: lineSlideV 24s linear infinite reverse; }
        @keyframes lineSlide {
            0%   { transform: translateX(-20%); opacity: 0; }
            15%  { opacity: 1; }
            85%  { opacity: 1; }
            100% { transform: translateX(20%); opacity: 0; }
        }
        @keyframes lineSlideV {
            0%   { transform: translateY(-20%); opacity: 0; }
            15%  { opacity: 1; }
            85%  { opacity: 1; }
            100% { transform: translateY(20%); opacity: 0; }
        }
        @media print {
            .noise-overlay, .spotlight, .deco-lines { display: none !important; }
            .reveal { opacity: 1 !important; transform: none !important; }
        }
        @media (prefers-reduced-motion: reduce) {
            .spotlight, .deco-lines, .reveal { animation: none !important; transition: none !important; }
            .reveal { opacity: 1 !important; transform: none !important; }
        }
        body::-webkit-scrollbar {
            width: 6px;
        }
        body::-webkit-scrollbar-track {
            background: var(--scrollbar-track);
        }
        body::-webkit-scrollbar-thumb {
            background: var(--scrollbar-thumb);
            border-radius: 3px;
        }
        body.lightbox-open {
            overflow: hidden;
        }
        .navbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: var(--bg-nav);
            backdrop-filter: var(--nav-blur);
            -webkit-backdrop-filter: var(--nav-blur);
            border-bottom: 1px solid var(--border);
            padding: 0 24px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.35s;
        }
        .navbar-brand {
            font-weight: 700;
            font-size: 1.15rem;
            color: var(--primary);
            letter-spacing: -0.01em;
            white-space: nowrap;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .navbar-brand .brand-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent);
            display: inline-block;
        }
        .navbar-links {
            display: flex;
            align-items: center;
            gap: 6px;
            list-style: none;
            flex-wrap: wrap;
        }
        .navbar-links a {
            text-decoration: none;
            color: var(--text-secondary);
            font-size: 0.875rem;
            font-weight: 500;
            padding: 6px 13px;
            border-radius: 8px;
            transition: all 0.2s;
            white-space: nowrap;
        }
        .navbar-links a:hover,
        .navbar-links a:focus-visible {
            color: var(--primary);
            background: var(--tag-bg);
            outline: none;
        }
        .navbar-links a:focus-visible {
            box-shadow: 0 0 0 2px var(--primary-light);
        }
        .navbar-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .btn-icon {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: 1px solid var(--border);
            background: var(--bg-card);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-secondary);
            transition: all 0.2s;
            font-size: 1rem;
        }
        .btn-icon:hover {
            background: var(--tag-bg);
            color: var(--primary);
            border-color: var(--primary-light);
            transform: translateY(-1px);
            box-shadow: var(--card-shadow);
        }
        .btn-icon:focus-visible {
            outline: 2px solid var(--primary-light);
            outline-offset: 2px;
        }
        .hamburger {
            display: none;
            background: none;
            border: none;
            cursor: pointer;
            padding: 4px;
            color: var(--text);
        }
        .hamburger span {
            display: block;
            width: 22px;
            height: 2px;
            background: var(--text);
            margin: 5px 0;
            border-radius: 2px;
            transition: all 0.3s;
        }
        .main-container {
            max-width: 880px;
            margin: 0 auto;
            padding: 80px 20px 40px;
            position: relative;
            z-index: 1;
        }
        .hero {
            position: relative;
            background: var(--hero-bg);
            border-radius: 20px;
            padding: 48px 40px;
            margin-bottom: 32px;
            text-align: center;
            overflow: hidden;
            border: 1px solid var(--border);
            transition: all 0.35s;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            box-shadow: 0 8px 40px var(--card-border-glow), inset 0 1px 0 rgba(255, 255, 255, 0.06);
        }
        .hero::before {
            content: '';
            position: absolute;
            top: -80px;
            right: -80px;
            width: 280px;
            height: 280px;
            border-radius: 50%;
            background: radial-gradient(circle, var(--tech-glow-1), transparent 70%);
            pointer-events: none;
        }
        .hero::after {
            content: '';
            position: absolute;
            bottom: -60px;
            left: -60px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: radial-gradient(circle, var(--tech-glow-2), transparent 70%);
            pointer-events: none;
        }
        .hero-avatar {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2rem;
            font-weight: 700;
            color: #fff;
            position: relative;
            z-index: 1;
            box-shadow: 0 8px 32px var(--card-border-glow), 0 0 0 4px var(--bg);
            overflow: hidden;
            border: 3px solid transparent;
            background-image: linear-gradient(var(--bg), var(--bg)), linear-gradient(135deg, var(--primary), var(--accent));
            background-origin: border-box;
            background-clip: content-box, border-box;
        }
        [data-theme="dark"] .hero-avatar {
            border-color: #1e293b;
        }
        .hero-avatar .avatar-text {
            font-size: 2rem;
            font-weight: 700;
            color: #fff;
            line-height: 1;
        }
        .hero h1 {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: -0.02em;
            margin-bottom: 4px;
            position: relative;
            z-index: 1;
            color: var(--text);
        }
        .hero .subtitle {
            font-size: 1rem;
            color: var(--text-secondary);
            margin-bottom: 16px;
            position: relative;
            z-index: 1;
        }
        .hero .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            justify-content: center;
            margin-bottom: 20px;
            position: relative;
            z-index: 1;
        }
        .tag {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 5px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
            background: var(--tag-bg);
            color: var(--tag-text);
            border: 1px solid var(--badge-outline);
            transition: all 0.25s;
            white-space: nowrap;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
        }
        .tag:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 16px var(--card-border-glow);
            border-color: var(--card-border-glow);
        }
        .hero .contact-row {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
            position: relative;
            z-index: 1;
        }
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 600;
            cursor: pointer;
            text-decoration: none;
            border: none;
            transition: all 0.2s;
            white-space: nowrap;
            font-family: inherit;
        }
        .btn-primary {
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #fff;
            box-shadow: 0 2px 12px var(--card-border-glow);
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 24px var(--card-border-glow);
            filter: brightness(1.1);
        }
        .btn-outline {
            background: var(--bg-card);
            color: var(--primary);
            border: 1.5px solid var(--primary);
        }
        .btn-outline:hover {
            background: var(--tag-bg);
            transform: translateY(-2px);
            box-shadow: var(--card-shadow);
        }
        .btn:focus-visible {
            outline: 2px solid var(--primary-light);
            outline-offset: 2px;
        }
        .highlights {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 16px;
            margin-bottom: 32px;
        }
        .highlight-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 22px 18px;
            text-align: center;
            transition: all 0.25s;
            box-shadow: var(--card-shadow);
        }
        .highlight-card:hover {
            transform: translateY(-4px);
            box-shadow: var(--card-shadow-hover);
            border-color: var(--primary-light);
        }
        .highlight-card .hl-number {
            font-size: 2.4rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: var(--primary);
            line-height: 1;
            margin-bottom: 6px;
        }
        .highlight-card .hl-label {
            font-size: 0.85rem;
            color: var(--text-secondary);
        }
        .highlight-card .hl-icon {
            font-size: 1.5rem;
            margin-bottom: 6px;
        }
        .section {
            margin-bottom: 32px;
        }
        .section-title {
            font-size: 1.25rem;
            font-weight: 700;
            letter-spacing: -0.01em;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--text);
        }
        .section-title::before {
            content: '';
            width: 4px;
            height: 22px;
            border-radius: 2px;
            background: linear-gradient(180deg, var(--primary), var(--accent));
            flex-shrink: 0;
            box-shadow: 0 0 8px var(--card-border-glow);
        }
        .tab-container {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 14px;
            overflow: hidden;
            box-shadow: var(--card-shadow);
            transition: all 0.35s;
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
        }
        .tab-container:hover {
            border-color: var(--card-border-glow);
            box-shadow: var(--card-shadow-hover);
        }
        .tab-list {
            display: flex;
            border-bottom: 1px solid var(--border);
            background: var(--divider);
            overflow-x: auto;
            scrollbar-width: none;
        }
        .tab-list::-webkit-scrollbar {
            display: none;
        }
        .tab-btn {
            flex-shrink: 0;
            padding: 13px 22px;
            font-size: 0.9rem;
            font-weight: 500;
            border: none;
            background: transparent;
            cursor: pointer;
            color: var(--text-secondary);
            transition: all 0.2s;
            font-family: inherit;
            white-space: nowrap;
            border-bottom: 2px solid transparent;
            margin-bottom: -1px;
        }
        .tab-btn:hover {
            color: var(--text);
            background: var(--tab-hover);
        }
        .tab-btn[aria-selected="true"] {
            color: var(--primary);
            font-weight: 600;
            border-bottom-color: var(--primary);
            background: var(--bg-card);
        }
        .tab-btn:focus-visible {
            outline: 2px solid var(--primary-light);
            outline-offset: -2px;
            z-index: 1;
        }
        .tab-panel {
            display: none;
            padding: 20px 24px;
            animation: fadeSlideIn 0.3s ease;
        }
        .tab-panel[aria-hidden="false"] {
            display: block;
        }
        @keyframes fadeSlideIn {
            from {
                opacity: 0;
                transform: translateY(8px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .exp-item {
            padding: 16px 0;
            border-bottom: 1px solid var(--divider);
        }
        .exp-item:last-child {
            border-bottom: none;
        }
        .exp-header {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 6px;
        }
        .exp-title {
            font-weight: 600;
            color: var(--text);
            font-size: 0.95rem;
        }
        .exp-date {
            font-size: 0.8rem;
            color: var(--text-muted);
            white-space: nowrap;
        }
        .exp-org {
            font-size: 0.85rem;
            color: var(--text-secondary);
            margin-bottom: 8px;
        }
        .exp-points {
            list-style: none;
            padding: 0;
        }
        .exp-points li {
            position: relative;
            padding-left: 18px;
            margin-bottom: 5px;
            font-size: 0.875rem;
            color: var(--text-secondary);
            line-height: 1.6;
        }
        .exp-points li::before {
            content: '•';
            position: absolute;
            left: 2px;
            color: var(--accent);
            font-weight: 700;
        }
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
        }
        .project-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 18px;
            transition: all 0.25s;
            box-shadow: var(--card-shadow);
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            position: relative;
            overflow: hidden;
        }
        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--primary), var(--accent), transparent);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .project-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--card-shadow-hover);
            border-color: var(--card-border-glow);
        }
        .project-card:hover::before {
            opacity: 1;
        }
        .project-card .proj-name {
            font-weight: 700;
            font-size: 0.95rem;
            color: var(--text);
            margin-bottom: 4px;
        }
        .project-card .proj-tech {
            font-size: 0.78rem;
            color: var(--primary);
            margin-bottom: 8px;
            display: flex;
            flex-wrap: wrap;
            gap: 4px;
        }
        .project-card .proj-tech span {
            background: var(--tag-bg);
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.72rem;
        }
        .project-card .proj-desc {
            font-size: 0.82rem;
            color: var(--text-secondary);
            line-height: 1.5;
            flex-grow: 1;
        }
        /* 画廊与证书共用图片样式 */
        .gallery-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
        }
        .gallery-item {
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            cursor: pointer;
            aspect-ratio: 4 / 3;
            background: var(--gallery-placeholder);
            border: 1px solid var(--border);
            transition: all 0.3s;
            box-shadow: var(--card-shadow);
            -webkit-tap-highlight-color: transparent;
            outline: none;
        }
        .gallery-item:hover {
            transform: translateY(-4px) scale(1.02);
            box-shadow: 0 12px 36px var(--card-border-glow), 0 4px 12px rgba(0,0,0,0.1);
            border-color: var(--card-border-glow);
        }
        .gallery-item:focus-visible {
            outline: 2px solid var(--primary-light);
            outline-offset: 2px;
        }
        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.4s;
        }
        .gallery-item:hover img {
            transform: scale(1.06);
        }
        .gallery-item .gallery-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.05));
            opacity: 0;
            transition: opacity 0.3s;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 12px;
            pointer-events: none;
        }
        .gallery-item:hover .gallery-overlay,
        .gallery-item:focus-visible .gallery-overlay {
            opacity: 1;
        }
        .gallery-overlay span {
            color: #fff;
            font-size: 0.78rem;
            font-weight: 500;
            background: rgba(0, 0, 0, 0.5);
            padding: 4px 12px;
            border-radius: 12px;
            backdrop-filter: blur(4px);
        }
        .img-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: var(--gallery-placeholder);
            color: var(--text-muted);
            font-size: 2rem;
        }
        /* 证书区布局 */
        .cert-with-gallery {
            display: flex;
            gap: 24px;
            align-items: flex-start;
        }
        .cert-gallery-side {
            flex-shrink: 0;
            width: 320px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
        }
        .cert-gallery-side .gallery-item {
            aspect-ratio: 3 / 4;
            border-radius: 10px;
        }
        .cert-list-wrapper {
            flex: 1;
            min-width: 0;
        }
        .cert-list {
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 10px;
        }
        .cert-list li {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 12px 16px;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: all 0.25s;
            box-shadow: var(--card-shadow);
            color: var(--text);
            line-height: 1.4;
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
        }
        .cert-list li:hover {
            border-color: var(--card-border-glow);
            transform: translateY(-2px);
            box-shadow: var(--card-shadow-hover);
            background: var(--tag-bg);
        }
        .cert-list .cert-icon {
            font-size: 1.2rem;
            flex-shrink: 0;
        }
        @media (max-width: 768px) {
            .cert-with-gallery {
                flex-direction: column;
            }
            .cert-gallery-side {
                width: 100%;
                grid-template-columns: repeat(4, 1fr);
                gap: 8px;
            }
            .cert-gallery-side .gallery-item {
                aspect-ratio: 3 / 4;
            }
            .gallery-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
            }
        }
        .skill-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .skill-category h4 {
            font-size: 0.9rem;
            font-weight: 600;
            margin-bottom: 12px;
            color: var(--text);
        }
        .skill-item {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 10px;
        }
        .skill-item .skill-name {
            width: 100px;
            font-size: 0.82rem;
            font-weight: 500;
            color: var(--text-secondary);
            text-align: right;
        }
        .skill-item .skill-bar-wrap {
            flex: 1;
            height: 7px;
            background: var(--progress-bg);
            border-radius: 4px;
            overflow: hidden;
        }
        .skill-item .skill-bar-fill {
            height: 100%;
            border-radius: 4px;
            background: var(--progress-fill);
            transition: width 0.8s cubic-bezier(0.22, 0.61, 0.36, 1);
            position: relative;
            overflow: hidden;
        }
        .skill-item .skill-bar-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            animation: shimmer 2.5s infinite;
        }
        @keyframes shimmer {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        .skill-item .skill-level {
            width: 40px;
            font-size: 0.75rem;
            color: var(--text-muted);
            text-align: left;
        }
        .footer {
            text-align: center;
            padding: 24px 20px;
            font-size: 0.78rem;
            color: var(--text-muted);
            border-top: 1px solid var(--border);
            margin-top: 16px;
        }
        .back-to-top {
            position: fixed;
            bottom: 28px;
            right: 28px;
            width: 42px;
            height: 42px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--primary), var(--accent));
            color: #fff;
            border: none;
            cursor: pointer;
            font-size: 1.2rem;
            box-shadow: 0 4px 20px var(--card-border-glow);
            opacity: 0;
            transform: translateY(20px);
            pointer-events: none;
            transition: all 0.3s;
            z-index: 999;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .back-to-top.visible {
            opacity: 1;
            transform: translateY(0);
            pointer-events: auto;
        }
        .back-to-top:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 22px rgba(30, 64, 175, 0.45);
        }
        .back-to-top:focus-visible {
            outline: 2px solid #fff;
            outline-offset: 2px;
        }
        .toast {
            position: fixed;
            bottom: 80px;
            left: 50%;
            transform: translateX(-50%) translateY(20px);
            background: #1e293b;
            color: #fff;
            padding: 10px 22px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 500;
            z-index: 2000;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
        [data-theme="dark"] .toast {
            background: #e2e8f0;
            color: #0f172a;
        }
        .toast.show {
            opacity: 1;
            transform: translateX(-50%) translateY(0);
        }
        .lightbox-overlay {
            position: fixed;
            inset: 0;
            z-index: 10000;
            background: var(--lightbox-bg);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            cursor: pointer;
        }
        .lightbox-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }
        .lightbox-content {
            position: relative;
            max-width: 90vw;
            max-height: 88vh;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: default;
            animation: lightboxZoomIn 0.35s cubic-bezier(0.22, 0.61, 0.36, 1);
        }
        @keyframes lightboxZoomIn {
            from {
                opacity: 0;
                transform: scale(0.9);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        .lightbox-content img {
            max-width: 90vw;
            max-height: 85vh;
            object-fit: contain;
            border-radius: 10px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
            user-select: none;
            -webkit-user-drag: none;
        }
        .lightbox-close {
            position: fixed;
            top: 20px;
            right: 24px;
            z-index: 10001;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: none;
            background: rgba(255, 255, 255, 0.15);
            color: #fff;
            font-size: 1.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.25s;
            backdrop-filter: blur(8px);
        }
        .lightbox-close:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: rotate(90deg);
        }
        .lightbox-nav {
            position: fixed;
            top: 50%;
            z-index: 10001;
            transform: translateY(-50%);
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: none;
            background: rgba(255, 255, 255, 0.15);
            color: #fff;
            font-size: 1.4rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.25s;
            backdrop-filter: blur(8px);
        }
        .lightbox-nav:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateY(-50%) scale(1.08);
        }
        .lightbox-prev {
            left: 20px;
        }
        .lightbox-next {
            right: 20px;
        }
        .lightbox-counter {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10001;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.85rem;
            font-weight: 500;
            background: rgba(0, 0, 0, 0.4);
            padding: 6px 16px;
            border-radius: 20px;
            backdrop-filter: blur(6px);
            pointer-events: none;
        }
        @media (max-width: 768px) {
            .navbar {
                padding: 0 14px;
                height: 52px;
            }
            .navbar-links {
                display: none;
                position: absolute;
                top: 52px;
                left: 0;
                right: 0;
                background: var(--bg-nav);
                backdrop-filter: var(--nav-blur);
                -webkit-backdrop-filter: var(--nav-blur);
                flex-direction: column;
                gap: 2px;
                padding: 8px 14px;
                border-bottom: 1px solid var(--border);
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
            }
            .navbar-links.open {
                display: flex;
            }
            .navbar-links a {
                padding: 10px 14px;
                border-radius: 8px;
                width: 100%;
            }
            .hamburger {
                display: block;
            }
            .hero {
                padding: 32px 18px;
                border-radius: 14px;
            }
            .hero h1 {
                font-size: 1.5rem;
            }
            .highlights {
                grid-template-columns: repeat(2, 1fr);
                gap: 10px;
            }
            .highlight-card .hl-number {
                font-size: 1.8rem;
            }
            .skill-grid {
                grid-template-columns: 1fr;
            }
            .project-grid {
                grid-template-columns: 1fr;
            }
            .gallery-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 8px;
            }
            .tab-btn {
                padding: 10px 14px;
                font-size: 0.8rem;
            }
            .tab-panel {
                padding: 14px 12px;
            }
            .main-container {
                padding: 64px 12px 24px;
            }
            .back-to-top {
                bottom: 16px;
                right: 16px;
                width: 36px;
                height: 36px;
                font-size: 1rem;
            }
            .cert-list {
                grid-template-columns: 1fr;
            }
            .lightbox-close {
                top: 12px;
                right: 12px;
                width: 38px;
                height: 38px;
                font-size: 1.2rem;
            }
            .lightbox-nav {
                width: 38px;
                height: 38px;
                font-size: 1.1rem;
            }
            .lightbox-prev {
                left: 8px;
            }
            .lightbox-next {
                right: 8px;
            }
            .lightbox-counter {
                bottom: 16px;
                font-size: 0.75rem;
                padding: 5px 12px;
            }
        }
        @media (max-width: 400px) {
            .highlights {
                grid-template-columns: 1fr 1fr;
                gap: 8px;
            }
            .highlight-card {
                padding: 14px 10px;
            }
            .highlight-card .hl-number {
                font-size: 1.5rem;
            }
            .highlight-card .hl-label {
                font-size: 0.75rem;
            }
            .hero .tag-row {
                gap: 5px;
            }
            .tag {
                padding: 4px 10px;
                font-size: 0.7rem;
            }
            .btn {
                padding: 8px 14px;
                font-size: 0.8rem;
            }
            .skill-item .skill-name {
                width: 70px;
                font-size: 0.72rem;
            }
            .cert-gallery-side {
                grid-template-columns: repeat(2, 1fr);
                gap: 6px;
            }
            .cert-gallery-side .gallery-item {
                aspect-ratio: 3 / 4;
            }
            .gallery-grid {
                grid-template-columns: repeat(2, 1fr);
                gap: 6px;
            }
        }
        @media print {
            html {
                scroll-padding-top: 0;
            }
            body {
                background: #fff !important;
                color: #1e293b !important;
                font-size: 11pt;
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }
            body::before,
            body::after {
                display: none !important;
            }
            .navbar,
            .back-to-top,
            .hamburger,
            .btn-icon,
            .navbar-actions,
            .toast,
            .lightbox-overlay,
            .lightbox-close,
            .lightbox-nav,
            .lightbox-counter,
            .gallery-overlay {
                display: none !important;
            }
            body.lightbox-open {
                overflow: auto !important;
            }
            .main-container {
                max-width: 100%;
                padding: 0 !important;
                margin: 0 !important;
            }
            .hero {
                background: #fff !important;
                border: none !important;
                border-radius: 0 !important;
                padding: 16px 0 !important;
                text-align: left !important;
                margin-bottom: 12px !important;
            }
            .hero::before,
            .hero::after {
                display: none !important;
            }
            .hero-avatar {
                border: 2px solid #e2e8f0 !important;
                box-shadow: none !important;
            }
            .hero h1 {
                font-size: 1.6rem !important;
                color: #1e293b !important;
            }
            .hero .subtitle {
                color: #475569 !important;
            }
            .hero .tag-row {
                justify-content: flex-start !important;
            }
            .tag {
                background: #f1f5f9 !important;
                color: #1e40af !important;
                border: 1px solid #e2e8f0 !important;
            }
            .hero .contact-row {
                justify-content: flex-start !important;
            }
            .btn-outline {
                background: #fff !important;
                color: #1e40af !important;
                border: 1px solid #1e40af !important;
            }
            .btn-primary {
                background: #1e40af !important;
                color: #fff !important;
            }
            .highlights {
                grid-template-columns: repeat(4, 1fr) !important;
                gap: 8px !important;
                page-break-inside: avoid;
            }
            .highlight-card {
                box-shadow: none !important;
                border: 1px solid #e2e8f0 !important;
                background: #fff !important;
                border-radius: 6px !important;
                padding: 10px !important;
            }
            .section {
                page-break-inside: avoid;
                margin-bottom: 16px !important;
            }
            .tab-container {
                border: 1px solid #e2e8f0 !important;
                box-shadow: none !important;
                background: #fff !important;
            }
            .tab-list {
                background: #f8fafc !important;
            }
            .tab-panel {
                display: block !important;
                padding: 10px 14px !important;
            }
            .tab-btn[aria-selected="false"] {
                display: none !important;
            }
            .project-card,
            .cert-list li {
                box-shadow: none !important;
                border: 1px solid #e2e8f0 !important;
                background: #fff !important;
                page-break-inside: avoid;
            }
            .cert-with-gallery {
                flex-direction: row !important;
            }
            .cert-gallery-side {
                width: 280px !important;
                grid-template-columns: repeat(2, 1fr) !important;
            }
            .gallery-item {
                border: 1px solid #e2e8f0 !important;
                box-shadow: none !important;
            }
            .footer {
                border-top: 1px solid #e2e8f0 !important;
                color: #94a3b8 !important;
            }
            @page {
                margin: 1.5cm;
            }
        }
    </style>
</head>
<body>
    <nav class="navbar" role="navigation" aria-label="主导航">
        <a href="#hero" class="navbar-brand"><span class="brand-dot"></span>杨豫豪</a>
        <ul class="navbar-links" id="navLinks" role="menubar">
            <li><a href="#hero" role="menuitem">首页</a></li>
            <li><a href="#highlights" role="menuitem">亮点</a></li>
            <li><a href="#experience" role="menuitem">经历</a></li>
            <li><a href="#projects" role="menuitem">项目</a></li>
            <li><a href="#skills" role="menuitem">技能</a></li>
            <li><a href="#hobbies" role="menuitem">爱好</a></li>
            <li><a href="#gallery" role="menuitem">掠影</a></li>
            <li><a href="#certs" role="menuitem">证书</a></li>
            <li><a href="#contact" role="menuitem">联系</a></li>
        </ul>
        <div class="navbar-actions">
            <button class="btn-icon" id="themeToggle" aria-label="切换深色/浅色模式"><span id="themeIcon">🌙</span></button>
            <button class="btn-icon" id="printBtn" aria-label="打印简历">🖨️</button>
            <button class="hamburger" id="hamburgerBtn" aria-label="展开菜单" aria-expanded="false"><span></span><span></span><span></span></button>
        </div>
    </nav>
    <main class="main-container" id="mainContent">
        <section class="hero reveal" id="hero" aria-labelledby="hero-heading">
            <div class="hero-avatar">
                <span class="avatar-text">杨</span>
            </div>
            <h1 id="hero-heading">杨豫豪</h1>
            <p class="subtitle">河南城建学院 · 环境工程专业（2026级）| AI工具实践者</p>
            <div class="tag-row">
                <span class="tag">🤖 AI对话与内容生成</span>
                <span class="tag">💻 AI辅助编程</span>
                <span class="tag">📋 知识管理</span>
                <span class="tag">🎨 基础演示设计</span>
                <span class="tag">🌱 环境工程</span>
            </div>
            <div class="contact-row">
                <button class="btn btn-primary" id="copyEmailBtn">📧 复制邮箱</button>
                <a href="tel:17719891195" class="btn btn-outline">📞 拨打电话</a>
            </div>
        </section>
        <section class="section" id="highlights" aria-labelledby="hl-title">
            <h2 class="section-title" id="hl-title">亮点成果</h2>
            <div class="highlights">
                <div class="highlight-card"><div class="hl-icon">🛠️</div><div class="hl-number">7+</div><div class="hl-label">款AI工具熟练运用</div></div>
                <div class="highlight-card"><div class="hl-icon">📜</div><div class="hl-number">8</div><div class="hl-label">项AI领域认证</div></div>
                <div class="highlight-card"><div class="hl-icon">🐍</div><div class="hl-number">多个</div><div class="hl-label">Python实践项目</div></div>
                <div class="highlight-card"><div class="hl-icon">📝</div><div class="hl-number">1篇+</div><div class="hl-label">文章被校内文学社刊采用</div></div>
            </div>
        </section>
        <section class="section" id="experience" aria-labelledby="exp-title">
            <h2 class="section-title" id="exp-title">经历</h2>
            <div class="tab-container" id="expTabs">
                <div class="tab-list" role="tablist" aria-label="经历分类">
                    <button class="tab-btn" role="tab" aria-selected="true" aria-controls="exp-panel-0">实践经历</button>
                    <button class="tab-btn" role="tab" aria-selected="false" aria-controls="exp-panel-1">教育背景</button>
                </div>
                <div class="tab-panel" role="tabpanel" aria-hidden="false" id="exp-panel-0">
                    <div class="exp-item">
                        <div class="exp-header"><span class="exp-title">AI辅助学习与创作实践</span><span class="exp-date">2024.09 – 至今</span></div>
                        <div class="exp-org">自主学习项目</div>
                        <ul class="exp-points">
                            <li>利用 DeepSeek 与 Kimi 系统梳理数理化知识体系，生成专题复习提纲与错题解析。</li>
                            <li>运用通义千问与豆包完成多次读后感、时事评论，部分文章被校内文学社刊采用。</li>
                            <li>借助 Trae 完成多个 Python 入门项目，包括自动整理文件夹脚本、成绩统计工具等。</li>
                            <li>使用 WorkBuddy 和 IMA 建立个人数字工作台，形成可追溯的个人知识库。</li>
                            <li>基于AI工具辅助，完成数套校园活动海报设计及PPT制作，获得师生认可。</li>
                        </ul>
                    </div>
                </div>
                <div class="tab-panel" role="tabpanel" aria-hidden="true" id="exp-panel-1">
                    <div class="exp-item">
                        <div class="exp-header"><span class="exp-title">河南城建学院 · 环境工程</span><span class="exp-date">2026.09 入学</span></div>
                        <div class="exp-org">本科 | 工学</div>
                        <ul class="exp-points">
                            <li>高考总分 493 分，全省位次前 20%。</li>
                            <li>已被河南城建学院环境工程专业录取，预计 2026 年 9 月入学。</li>
                            <li>高中期间自学多种AI工具，并将AI融入日常学习与创作。</li>
                            <li>自学吴恩达《机器学习》入门内容，对AI技术有持续学习热情。</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <section class="section" id="projects" aria-labelledby="proj-title">
            <h2 class="section-title" id="proj-title">实践项目</h2>
            <div class="tab-container" id="projTabs">
                <div class="tab-list" role="tablist" aria-label="项目分类">
                    <button class="tab-btn" role="tab" aria-selected="true" aria-controls="proj-panel-0">🤖 AI工具类</button>
                    <button class="tab-btn" role="tab" aria-selected="false" aria-controls="proj-panel-1">🎨 设计类</button>
                </div>
                <div class="tab-panel" role="tabpanel" aria-hidden="false" id="proj-panel-0">
                    <div class="project-grid">
                        <div class="project-card"><div class="proj-name">📂 自动整理文件夹脚本</div><div class="proj-tech"><span>Python</span><span>Trae</span></div><div class="proj-desc">借助AI完成脚本，按文件类型自动归类，提升日常文件管理效率。</div></div>
                        <div class="project-card"><div class="proj-name">📊 成绩统计分析工具</div><div class="proj-tech"><span>Python</span><span>Pandas</span></div><div class="proj-desc">支持多科目成绩录入、均分计算与排名生成，应用于实际学习场景。</div></div>
                        <div class="project-card"><div class="proj-name">📝 AI辅助写作工作流</div><div class="proj-tech"><span>DeepSeek</span><span>Kimi</span></div><div class="proj-desc">设计AI辅助写作流程，产出读后感及时事评论，部分被校内文学社刊采用。</div></div>
                    </div>
                </div>
                <div class="tab-panel" role="tabpanel" aria-hidden="true" id="proj-panel-1">
                    <div class="project-grid">
                        <div class="project-card"><div class="proj-name">🎨 校园活动海报设计</div><div class="proj-tech"><span>AI辅助设计</span></div><div class="proj-desc">利用AI工具完成数套海报，用于校内活动宣传并获得积极反馈。</div></div>
                        <div class="project-card"><div class="proj-name">📽️ 演示文稿制作</div><div class="proj-tech"><span>PowerPoint</span></div><div class="proj-desc">AI辅助生成大纲并优化排版，独立完成多套演示文稿用于班级展示。</div></div>
                    </div>
                </div>
            </div>
        </section>
        <section class="section" id="skills" aria-labelledby="skills-title">
            <h2 class="section-title" id="skills-title">技能矩阵</h2>
            <div class="tab-container" style="padding:20px 24px">
                <div class="skill-grid">
                    <div class="skill-category"><h4>🤖 AI对话与内容生成</h4>
                        <div class="skill-item"><span class="skill-name">DeepSeek</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:85%"></div></div><span class="skill-level">熟练</span></div>
                        <div class="skill-item"><span class="skill-name">Kimi</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:80%"></div></div><span class="skill-level">熟练</span></div>
                        <div class="skill-item"><span class="skill-name">通义千问</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:80%"></div></div><span class="skill-level">熟练</span></div>
                        <div class="skill-item"><span class="skill-name">豆包</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:75%"></div></div><span class="skill-level">掌握</span></div>
                    </div>
                    <div class="skill-category"><h4>💻 AI辅助编程与效率</h4>
                        <div class="skill-item"><span class="skill-name">Trae</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:70%"></div></div><span class="skill-level">掌握</span></div>
                        <div class="skill-item"><span class="skill-name">WorkBuddy</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:70%"></div></div><span class="skill-level">掌握</span></div>
                        <div class="skill-item"><span class="skill-name">IMA</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:65%"></div></div><span class="skill-level">掌握</span></div>
                        <div class="skill-item"><span class="skill-name">PowerPoint</span><div class="skill-bar-wrap"><div class="skill-bar-fill" style="width:60%"></div></div><span class="skill-level">基础</span></div>
                    </div>
                </div>
            </div>
        </section>
        <!-- ============ 特长与爱好 ============ -->
        <section class="section" id="hobbies" aria-labelledby="hobbies-title">
            <h2 class="section-title" id="hobbies-title">特长与爱好</h2>
            <div class="tab-container" style="padding:20px 24px">
                <div class="tag-row" style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center">
                    <span class="tag">✍️ 写作（文章被校内文学社刊采用）</span>
                    <span class="tag">🎨 海报与演示设计</span>
                    <span class="tag">🐍 Python 小项目实践</span>
                    <span class="tag">🤖 AI 工具探索（自学吴恩达《机器学习》）</span>
                    <span class="tag">📚 阅读与时事评论</span>
                </div>
            </div>
        </section>
        <section class="section" id="gallery" aria-labelledby="gallery-title">
            <h2 class="section-title" id="gallery-title">个人掠影</h2>
            <div class="tab-container" style="padding:20px 24px">
                <p style="font-size:0.82rem;color:var(--text-muted);margin-bottom:14px;text-align:center">📷 点击图片可放大查看 · 共 8 张</p>
                <div class="gallery-grid" id="galleryGrid" role="list" aria-label="个人照片画廊"></div>
            </div>
        </section>
        <section class="section" id="certs" aria-labelledby="certs-title">
            <h2 class="section-title" id="certs-title">获奖与证书</h2>
            <div class="tab-container" style="padding:20px 24px">
                <div class="cert-with-gallery">
                    <div class="cert-gallery-side" id="certGallerySide" role="list" aria-label="证书配图"></div>
                    <div class="cert-list-wrapper">
                        <h4 style="margin-bottom:14px;color:var(--text);font-size:0.95rem;">📜 AI领域证书（8项）</h4>
                        <ul class="cert-list" id="certList"></ul>
                        <p style="font-size:0.8rem;color:var(--text-muted);margin-top:10px;">※ 具体证书名称已根据提供信息更新</p>
                    </div>
                </div>
            </div>
        </section>
        <section class="section" id="contact" aria-labelledby="contact-title">
            <h2 class="section-title" id="contact-title">联系方式</h2>
            <div class="tab-container" style="padding:20px 24px;text-align:center">
                <p style="margin-bottom:8px;color:var(--text)">📧 邮箱：<span id="displayEmail" style="font-weight:600;color:var(--primary)"></span></p>
                <p style="margin-bottom:8px;color:var(--text)">📞 手机：17719891195</p>
                <p style="color:var(--text-secondary)">📍 河南郑州</p>
                <button class="btn btn-primary" id="copyEmailBtn2" style="margin-top:10px">📋 一键复制邮箱</button>
            </div>
        </section>
    </main>
    <div class="lightbox-overlay" id="lightboxOverlay" aria-hidden="true" role="dialog" aria-modal="true" aria-label="图片灯箱">
        <button class="lightbox-close" id="lightboxClose" aria-label="关闭灯箱">✕</button>
        <button class="lightbox-nav lightbox-prev" id="lightboxPrev" aria-label="上一张">‹</button>
        <button class="lightbox-nav lightbox-next" id="lightboxNext" aria-label="下一张">›</button>
        <div class="lightbox-content" id="lightboxContent"></div>
        <div class="lightbox-counter" id="lightboxCounter" aria-live="polite"></div>
    </div>
    <footer class="footer">© 2026 杨豫豪 | 更新于 2026年8月 | 此简历为个人学习与求职用途</footer>
    <button class="back-to-top" id="backToTop" aria-label="返回顶部">↑</button>
    <div class="toast" id="toast" aria-live="polite"></div>
    <div class="noise-overlay" aria-hidden="true"></div>
    <div class="spotlight" id="spotlight" aria-hidden="true"></div>
    <div class="deco-lines" aria-hidden="true">
        <span class="deco-line"></span>
        <span class="deco-line"></span>
        <span class="deco-line"></span>
        <span class="deco-line-v"></span>
        <span class="deco-line-v"></span>
    </div>
    <script>
        (function() {
            const resume = {
                name: '杨豫豪',
                email: '2813573523@qq.com',
                phone: '17719891195',
                location: '河南郑州',
                university: '河南城建学院',
                major: '环境工程',
                gaokaoScore: 493,
                gaokaoPercentile: '前20%',
                enrollmentYear: '2026',
                aiTools: ['DeepSeek', 'Kimi', '通义千问', '豆包', 'Trae', 'WorkBuddy', 'IMA'],
                certCount: 8,
                highlights: [
                    { icon: '🛠️', number: '7+', label: '款AI工具熟练运用' },
                    { icon: '📜', number: '8', label: '项AI领域认证' },
                    { icon: '🐍', number: '多个', label: 'Python实践项目' },
                    { icon: '📝', number: '1篇+', label: '文章被校内文学社刊采用' }
                ],
                galleryImages: [
                    { src: './1.jpg', alt: '个人照片 1' },
                    { src: './2.jpg', alt: '个人照片 2' },
                    { src: './3.jpg', alt: '个人照片 3' },
                    { src: './4.jpg', alt: '个人照片 4' },
                    { src: './5.jpg', alt: '个人照片 5' },
                    { src: './6.jpg', alt: '个人照片 6' },
                    { src: './7.jpg', alt: '个人照片 7' },
                    { src: './8.jpg', alt: '个人照片 8' }
                ],
                certList: [
                    'Datawhale & 科大讯飞联合颁发的 Prompt Engineer 证书',
                    '华为人工智能初识微认证',
                    '阿里达摩院高级人工智能训练师',
                    'Datawhale & 文付宝百宝箱联合颁发的 Agent Engineer 能力认证证书',
                    'Datawhale & 豆包 MarsCode 联合颁发的 AI + 编程能力认证证书',
                    '国际培训中心（ITCILO）人工智能证书',
                    'Datawhale & 科大讯飞星愿 MaaS 平台联合颁发的 Fine-tuning Engineer 能力认证证书',
                    '玻尔「AI4S Cup - Python 基础能力认证」AI 证书'
                ]
            };

            const themeToggle = document.getElementById('themeToggle');
            const themeIcon = document.getElementById('themeIcon');
            const printBtn = document.getElementById('printBtn');
            const backToTop = document.getElementById('backToTop');
            const toast = document.getElementById('toast');
            const hamburgerBtn = document.getElementById('hamburgerBtn');
            const navLinks = document.getElementById('navLinks');
            const displayEmail = document.getElementById('displayEmail');
            const copyEmailBtn = document.getElementById('copyEmailBtn');
            const copyEmailBtn2 = document.getElementById('copyEmailBtn2');
            const html = document.documentElement;
            const galleryGrid = document.getElementById('galleryGrid');
            const certGallerySide = document.getElementById('certGallerySide');
            const certListEl = document.getElementById('certList');
            const lightboxOverlay = document.getElementById('lightboxOverlay');
            const lightboxContent = document.getElementById('lightboxContent');
            const lightboxClose = document.getElementById('lightboxClose');
            const lightboxPrev = document.getElementById('lightboxPrev');
            const lightboxNext = document.getElementById('lightboxNext');
            const lightboxCounter = document.getElementById('lightboxCounter');

            let currentImageIndex = 0;

            const emailUser = '2813573523';
            const emailDomain = 'qq.com';
            const fullEmail = emailUser + '@' + emailDomain;
            if (displayEmail) displayEmail.textContent = fullEmail;

            function createImageItem(imgData, index) {
                const item = document.createElement('div');
                item.className = 'gallery-item';
                item.setAttribute('role', 'listitem');
                item.setAttribute('tabindex', '0');
                item.setAttribute('aria-label', imgData.alt + ' - 点击放大');
                item.dataset.imgIndex = index;
                const img = document.createElement('img');
                img.src = imgData.src;
                img.alt = imgData.alt;
                img.loading = 'lazy';
                img.setAttribute('draggable', 'false');
                img.onerror = function() {
                    const placeholder = document.createElement('div');
                    placeholder.className = 'img-placeholder';
                    placeholder.innerHTML = '🖼️';
                    item.innerHTML = '';
                    item.appendChild(placeholder);
                };
                const overlay = document.createElement('div');
                overlay.className = 'gallery-overlay';
                const overlayText = document.createElement('span');
                overlayText.textContent = '🔍 查看大图';
                overlay.appendChild(overlayText);
                item.appendChild(img);
                item.appendChild(overlay);
                item.addEventListener('click', () => openLightbox(index));
                item.addEventListener('keydown', (e) => {
                    if (e.key === 'Enter' || e.key === ' ') {
                        e.preventDefault();
                        openLightbox(index);
                    }
                });
                return item;
            }

            function renderMainGallery() {
                if (!galleryGrid) return;
                galleryGrid.innerHTML = '';
                resume.galleryImages.forEach((imgData, idx) => {
                    const item = createImageItem(imgData, idx);
                    galleryGrid.appendChild(item);
                });
            }

            function renderCertSideGallery() {
                if (!certGallerySide) return;
                certGallerySide.innerHTML = '';
                resume.galleryImages.forEach((imgData, idx) => {
                    const item = createImageItem(imgData, idx);
                    certGallerySide.appendChild(item);
                });
            }

            function renderCertList() {
                if (!certListEl) return;
                certListEl.innerHTML = '';
                resume.certList.forEach(certName => {
                    const li = document.createElement('li');
                    li.innerHTML = `<span class="cert-icon">🏅</span> ${certName}`;
                    certListEl.appendChild(li);
                });
            }

            function openLightbox(index) {
                if (index < 0 || index >= resume.galleryImages.length) return;
                currentImageIndex = index;
                updateLightboxImage();
                lightboxOverlay.classList.add('active');
                lightboxOverlay.setAttribute('aria-hidden', 'false');
                document.body.classList.add('lightbox-open');
                lightboxClose.focus();
            }

            function closeLightbox() {
                lightboxOverlay.classList.remove('active');
                lightboxOverlay.setAttribute('aria-hidden', 'true');
                document.body.classList.remove('lightbox-open');
                lightboxContent.innerHTML = '';
                lightboxCounter.textContent = '';
            }

            function updateLightboxImage() {
                const imgData = resume.galleryImages[currentImageIndex];
                lightboxContent.innerHTML = '';
                const img = document.createElement('img');
                img.src = imgData.src;
                img.alt = imgData.alt;
                img.setAttribute('draggable', 'false');
                img.onerror = () => lightboxContent.innerHTML =
                    '<div style="color:#fff;font-size:3rem;text-align:center">🖼️</div>';
                lightboxContent.appendChild(img);
                lightboxCounter.textContent = (currentImageIndex + 1) + ' / ' + resume.galleryImages.length;
            }

            function showPrevImage() {
                currentImageIndex = (currentImageIndex - 1 + resume.galleryImages.length) % resume.galleryImages.length;
                updateLightboxImage();
            }

            function showNextImage() {
                currentImageIndex = (currentImageIndex + 1) % resume.galleryImages.length;
                updateLightboxImage();
            }

            lightboxClose.addEventListener('click', closeLightbox);
            lightboxPrev.addEventListener('click', (e) => { e.stopPropagation();
                showPrevImage(); });
            lightboxNext.addEventListener('click', (e) => { e.stopPropagation();
                showNextImage(); });
            lightboxOverlay.addEventListener('click', (e) => { if (e.target === lightboxOverlay) closeLightbox(); });
            document.addEventListener('keydown', (e) => {
                if (!lightboxOverlay.classList.contains('active')) return;
                if (e.key === 'Escape') { e.preventDefault();
                    closeLightbox(); } else if (e.key === 'ArrowLeft') { e.preventDefault();
                    showPrevImage(); } else if (e.key === 'ArrowRight') { e.preventDefault();
                    showNextImage(); } else if (e.key === 'Home') { e.preventDefault();
                    currentImageIndex = 0;
                    updateLightboxImage(); } else if (e.key === 'End') { e.preventDefault();
                    currentImageIndex = resume.galleryImages.length - 1;
                    updateLightboxImage(); }
            });
            let touchStartX = 0;
            lightboxOverlay.addEventListener('touchstart', (e) => touchStartX = e.changedTouches[0].screenX, { passive: true });
            lightboxOverlay.addEventListener('touchend', (e) => {
                const diff = touchStartX - e.changedTouches[0].screenX;
                if (Math.abs(diff) > 60) diff > 0 ? showNextImage() : showPrevImage();
            }, { passive: true });

            function getTheme() {
                return localStorage.getItem('resume-theme') || (window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' :
                    'light');
            }

            function applyTheme(t) {
                html.setAttribute('data-theme', t);
                themeIcon.textContent = t === 'dark' ? '☀️' : '🌙';
                localStorage.setItem('resume-theme', t);
            }
            themeToggle.addEventListener('click', () => { applyTheme(html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark'); });
            applyTheme(getTheme());
            window.matchMedia('(prefers-color-scheme:dark)').addEventListener('change', (e) => { if (!localStorage.getItem(
                    'resume-theme')) applyTheme(e.matches ? 'dark' : 'light'); });

            printBtn.addEventListener('click', () => window.print());

            function updateBackToTop() { backToTop.classList.toggle('visible', window.scrollY > 500); }
            window.addEventListener('scroll', updateBackToTop, { passive: true });
            backToTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
            updateBackToTop();

            let toastTimer;

            function showToast(msg) { clearTimeout(toastTimer);
                toast.textContent = msg;
                toast.classList.add('show');
                toastTimer = setTimeout(() => toast.classList.remove('show'), 2000); }

            function copyEmail() {
                if (navigator.clipboard) navigator.clipboard.writeText(fullEmail).then(() => showToast('✅ 邮箱已复制！')).catch(
                    () => fallbackCopy());
                else fallbackCopy();
            }

            function fallbackCopy() {
                const ta = document.createElement('textarea');
                ta.value = fullEmail;
                ta.style.position = 'fixed';
                ta.style.left = '-9999px';
                document.body.appendChild(ta);
                ta.select();
                try { document.execCommand('copy');
                    showToast('✅ 邮箱已复制！'); } catch (e) { showToast('⚠️ 复制失败：' + fullEmail); }
                document.body.removeChild(ta);
            }
            copyEmailBtn.addEventListener('click', copyEmail);
            copyEmailBtn2.addEventListener('click', copyEmail);

            hamburgerBtn.addEventListener('click', () => { const o = navLinks.classList.toggle('open');
                hamburgerBtn.setAttribute('aria-expanded', o); });
            navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { navLinks.classList.remove('open');
                hamburgerBtn.setAttribute('aria-expanded', 'false'); }));
            document.addEventListener('click', (e) => { if (!navLinks.contains(e.target) && e.target !== hamburgerBtn) { navLinks
                    .classList.remove('open');
                hamburgerBtn.setAttribute('aria-expanded', 'false'); } });
            document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && navLinks.classList.contains('open')) { navLinks
                    .classList.remove('open');
                hamburgerBtn.focus(); } });

            function initTabs(id) {
                const c = document.getElementById(id);
                if (!c) return;
                const tabs = c.querySelectorAll('.tab-btn');
                const panels = c.querySelectorAll('.tab-panel');

                function switchTab(i) { tabs.forEach((t, j) => { t.setAttribute('aria-selected', j === i);
                        t.setAttribute('tabindex', j === i ? '0' : '-1'); });
                    panels.forEach((p, j) => p.setAttribute('aria-hidden', j !== i)); }
                c.querySelector('.tab-list').addEventListener('click', (e) => { const b = e.target.closest('.tab-btn'); if (b) { const i =
                        Array.from(tabs).indexOf(b); if (i >= 0) switchTab(i); } });
                c.querySelector('.tab-list').addEventListener('keydown', (e) => {
                    const cur = document.activeElement;
                    if (!cur || !cur.classList.contains('tab-btn')) return;
                    const i = Array.from(tabs).indexOf(cur);
                    let ni = i;
                    if (e.key === 'ArrowRight') { e.preventDefault();
                        ni = (i + 1) % tabs.length; } else if (e.key === 'ArrowLeft') { e.preventDefault();
                        ni = (i - 1 + tabs.length) % tabs.length; } else if (e.key === 'Home') { e.preventDefault();
                        ni = 0; } else if (e.key === 'End') { e.preventDefault();
                        ni = tabs.length - 1; }
                    if (ni !== i) { tabs[ni].focus();
                        switchTab(ni); }
                });
                switchTab(0);
            }
            initTabs('expTabs');
            initTabs('projTabs');

            document.querySelectorAll('.navbar-links a[href^="#"]').forEach(a => a.addEventListener('click', function(e) {
                e.preventDefault();
                const t = document.getElementById(this.getAttribute('href').substring(1));
                if (t) { const nh = document.querySelector('.navbar').offsetHeight;
                    window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - nh - 10, behavior: 'smooth' }); }
            }));

            if (window.location.hash) setTimeout(() => { const t = document.querySelector(window.location.hash); if (t) { const nh =
                        document.querySelector('.navbar').offsetHeight;
                    window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - nh - 10, behavior: 'smooth' }); } },
                300);

            renderMainGallery();
            renderCertSideGallery();
            renderCertList();

            /* === 点缀效果：滚动渐入 === */
            (function addRevealClass() {
                const sections = document.querySelectorAll('.section, .hero');
                sections.forEach((sec, i) => {
                    sec.classList.add('reveal');
                    if (i > 0) sec.classList.add('reveal-delay-' + Math.min(i, 4));
                });
                document.querySelectorAll('.highlight-card').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + (i + 1)));
                document.querySelectorAll('.project-card').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + ((i % 3) + 1)));
                document.querySelectorAll('.cert-list li').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + ((i % 4) + 1)));
                document.querySelectorAll('.skill-item').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + ((i % 4) + 1)));
                document.querySelectorAll('.gallery-item').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + ((i % 4) + 1)));
                document.querySelectorAll('.tag').forEach((el, i) => el.classList.add('reveal', 'reveal-delay-' + ((i % 4) + 1)));

                if (!('IntersectionObserver' in window)) {
                    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
                    return;
                }
                const io = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            entry.target.classList.add('visible');
                            io.unobserve(entry.target);
                        }
                    });
                }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
                document.querySelectorAll('.reveal').forEach(el => io.observe(el));
            })();

            /* === 点缀效果：3D tilt卡片 === */
            (function initTilt() {
                const cards = document.querySelectorAll('.project-card, .cert-list li, .highlight-card, .tab-container');
                const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                const coarse = window.matchMedia('(pointer: coarse)').matches;
                if (reduce || coarse) return;
                cards.forEach(card => {
                    card.classList.add('tilt-card');
                    const max = 6;
                    card.addEventListener('mousemove', (e) => {
                        const r = card.getBoundingClientRect();
                        const x = e.clientX - r.left;
                        const y = e.clientY - r.top;
                        const px = (x / r.width - 0.5) * 2;
                        const py = (y / r.height - 0.5) * 2;
                        card.style.transform = `perspective(900px) rotateX(${-py * max}deg) rotateY(${px * max}deg) translateZ(2px)`;
                    });
                    card.addEventListener('mouseleave', () => {
                        card.style.transform = '';
                    });
                });
            })();

            /* === 点缀效果：磁吸按钮 === */
            (function initMagnet() {
                const btns = document.querySelectorAll('.btn, .tag, .back-to-top');
                const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
                const coarse = window.matchMedia('(pointer: coarse)').matches;
                if (reduce || coarse) return;
                btns.forEach(b => {
                    b.classList.add('magnet-btn');
                    const strength = 10;
                    b.addEventListener('mousemove', (e) => {
                        const r = b.getBoundingClientRect();
                        const cx = r.left + r.width / 2;
                        const cy = r.top + r.height / 2;
                        const dx = e.clientX - cx;
                        const dy = e.clientY - cy;
                        b.style.transform = `translate(${dx * 0.15}px, ${dy * 0.15}px)`;
                    });
                    b.addEventListener('mouseleave', () => { b.style.transform = ''; });
                });
            })();

            /* === 点缀效果：光标跟随聚光灯 === */
            (function initSpotlight() {
                const s = document.getElementById('spotlight');
                if (!s) return;
                const coarse = window.matchMedia('(pointer: coarse)').matches;
                if (coarse) { s.style.display = 'none'; return; }
                let tx = window.innerWidth / 2;
                let ty = window.innerHeight / 2;
                let x = tx, y = ty;
                document.addEventListener('mousemove', (e) => { tx = e.clientX; ty = e.clientY; }, { passive: true });
                function loop() {
                    x += (tx - x) * 0.12;
                    y += (ty - y) * 0.12;
                    s.style.transform = `translate(${x}px, ${y}px) translate(-50%, -50%)`;
                    requestAnimationFrame(loop);
                }
                loop();
            })();

            console.log('✅ 简历已加载 | 证书8项 | 图片8张 | 点缀效果就绪');
        })();
    </script>
</body>
</html>

```

---

> 声明：本作品由本人独立完成，开发过程中使用 AI 工具辅助，符合赛事规定。
