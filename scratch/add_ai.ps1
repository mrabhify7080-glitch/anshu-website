$css = @"
        /* ==========================================================================
           AI FEMALE ASSISTANT (PRIYA) WIDGET STYLES
           ========================================================================== */
        #ai-assistant-wrapper {
            position: fixed;
            bottom: 25px;
            left: 25px;
            z-index: 99999;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        #ai-tooltip-bubble {
            position: absolute;
            bottom: 75px;
            left: 0;
            width: 270px;
            background: #FFFFFF;
            color: #1B2A41;
            padding: 12px 16px;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.18);
            border: 2px solid #C89B3C;
            font-size: 0.88rem;
            line-height: 1.4;
            animation: aiBounceIn 0.5s ease;
        }

        #ai-tooltip-bubble::after {
            content: '';
            position: absolute;
            bottom: -10px;
            left: 25px;
            border-width: 10px 10px 0 10px;
            border-style: solid;
            border-color: #C89B3C transparent transparent transparent;
        }

        .ai-close-bubble {
            position: absolute;
            top: 4px;
            right: 8px;
            font-size: 16px;
            cursor: pointer;
            color: #888;
        }

        #ai-trigger-btn {
            display: flex;
            align-items: center;
            gap: 12px;
            background: #1B2A41;
            color: #FFFFFF;
            padding: 8px 18px 8px 8px;
            border-radius: 50px;
            border: 2px solid #C89B3C;
            box-shadow: 0 8px 25px rgba(27, 42, 65, 0.35);
            cursor: pointer;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        #ai-trigger-btn:hover {
            transform: translateY(-4px) scale(1.03);
            box-shadow: 0 12px 30px rgba(200, 155, 60, 0.4);
        }

        .ai-avatar-container {
            position: relative;
            width: 48px;
            height: 48px;
            border-radius: 50%;
            border: 2px solid #C89B3C;
            flex-shrink: 0;
        }

        .ai-avatar-img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
        }

        .ai-online-status {
            position: absolute;
            bottom: 0;
            right: 0;
            width: 13px;
            height: 13px;
            background-color: #25D366;
            border: 2px solid #1B2A41;
            border-radius: 50%;
        }

        .ai-trigger-text {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
        }

        .ai-name {
            font-weight: 700;
            font-size: 0.92rem;
            color: #FFFFFF;
        }

        .ai-status-text {
            font-size: 0.72rem;
            color: #C89B3C;
            font-weight: 600;
        }

        /* Chat Window Modal */
        #ai-chat-window {
            position: fixed;
            bottom: 90px;
            left: 25px;
            width: 360px;
            max-width: calc(100vw - 40px);
            height: 480px;
            background: #FFFFFF;
            border-radius: 20px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.25);
            border: 2px solid #C89B3C;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            z-index: 100000;
            transition: all 0.3s ease;
        }

        .ai-chat-hidden {
            opacity: 0;
            pointer-events: none;
            transform: translateY(20px) scale(0.95);
        }

        .ai-chat-header {
            background: #1B2A41;
            color: #FFFFFF;
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid #C89B3C;
        }

        .ai-header-user {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .ai-chat-name {
            font-size: 1rem;
            color: #FFFFFF;
            font-weight: 700;
            margin: 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .ai-badge-tag {
            font-size: 0.68rem;
            background: rgba(200, 155, 60, 0.25);
            color: #C89B3C;
            padding: 2px 8px;
            border-radius: 8px;
        }

        .ai-chat-sub {
            font-size: 0.75rem;
            color: #A0AEC0;
            margin: 0;
        }

        .ai-chat-close-btn {
            background: none;
            border: none;
            color: #FFFFFF;
            font-size: 24px;
            cursor: pointer;
            line-height: 1;
        }

        .ai-chat-messages {
            flex: 1;
            padding: 16px;
            overflow-y: auto;
            background: #F9F6F0;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .ai-msg {
            max-width: 85%;
            display: flex;
            flex-direction: column;
        }

        .ai-msg-bot {
            align-self: flex-start;
        }

        .ai-msg-user {
            align-self: flex-end;
        }

        .ai-msg-bubble {
            padding: 12px 16px;
            border-radius: 16px;
            font-size: 0.88rem;
            line-height: 1.45;
        }

        .ai-msg-bot .ai-msg-bubble {
            background: #FFFFFF;
            color: #1B2A41;
            border-bottom-left-radius: 4px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.05);
            border: 1px solid #E2E8F0;
        }

        .ai-msg-user .ai-msg-bubble {
            background: #1B2A41;
            color: #FFFFFF;
            border-bottom-right-radius: 4px;
        }

        .ai-msg-time {
            font-size: 0.68rem;
            color: #888;
            margin-top: 4px;
            align-self: flex-end;
        }

        .ai-quick-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 6px;
        }

        .ai-chip {
            background: #FFFFFF;
            border: 1px solid #C89B3C;
            color: #1B2A41;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        .ai-chip:hover {
            background: #C89B3C;
            color: #FFFFFF;
        }

        .ai-chat-footer {
            padding: 10px 14px;
            background: #FFFFFF;
            border-top: 1px solid #E2E8F0;
            display: flex;
            gap: 8px;
        }

        #ai-chat-input {
            flex: 1;
            border: 1px solid #CBD5E0;
            border-radius: 25px;
            padding: 10px 16px;
            font-size: 0.88rem;
            outline: none;
        }

        #ai-chat-input:focus {
            border-color: #C89B3C;
        }

        #ai-send-btn {
            background: #1B2A41;
            color: #C89B3C;
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #ai-send-btn:hover {
            background: #C89B3C;
            color: #1B2A41;
        }

        @keyframes aiBounceIn {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
"@

$htmlJs = @"
    <!-- ==========================================================================
         AI FEMALE ASSISTANT (PRIYA) WIDGET
         ========================================================================== -->
    <div id="ai-assistant-wrapper">
        <!-- Tooltip Bubble -->
        <div id="ai-tooltip-bubble">
            <span class="ai-close-bubble" onclick="document.getElementById('ai-tooltip-bubble').style.display='none'">&times;</span>
            <div class="ai-bubble-content">
                <span class="ai-wave">👋</span> <strong>Namaste!</strong> Main Priya (AI Assistant) hoon. Plot ya Site Visit Help chahiye?
            </div>
        </div>

        <!-- Floating Trigger Button -->
        <button id="ai-trigger-btn" onclick="toggleAIChat()" aria-label="Open AI Property Assistant">
            <div class="ai-avatar-container">
                <img src="assets/ai_female_assistant.jpg" alt="Priya - AI Assistant" class="ai-avatar-img">
                <span class="ai-online-status"></span>
            </div>
            <div class="ai-trigger-text">
                <span class="ai-name">Priya (AI)</span>
                <span class="ai-status-text">Ask Anything</span>
            </div>
        </button>

        <!-- AI Chat Window -->
        <div id="ai-chat-window" class="ai-chat-hidden">
            <div class="ai-chat-header">
                <div class="ai-header-user">
                    <div class="ai-avatar-container" style="width:40px; height:40px;">
                        <img src="assets/ai_female_assistant.jpg" alt="Priya AI Support" class="ai-avatar-img">
                        <span class="ai-online-status"></span>
                    </div>
                    <div>
                        <h4 class="ai-chat-name">Priya <span class="ai-badge-tag">AI Support</span></h4>
                        <p class="ai-chat-sub">Anshu Property Virtual Assistant</p>
                    </div>
                </div>
                <button class="ai-chat-close-btn" onclick="toggleAIChat()">&times;</button>
            </div>

            <div class="ai-chat-messages" id="ai-chat-messages">
                <div class="ai-msg ai-msg-bot">
                    <div class="ai-msg-bubble">
                        Namaste! 🙏 Main <strong>Priya</strong>, Anshu Property ki AI Assistant hoon.<br><br>
                        Varanasi, Allahabad, Bihar ya MP mein kisi bhi VDA plot, rate ya Free Site Visit ke baare mein mujhse puchein!
                    </div>
                    <span class="ai-msg-time">Just now</span>
                </div>

                <div class="ai-quick-chips">
                    <button class="ai-chip" onclick="sendQuickChip('VDA Approved plots list')">📍 VDA Approved Plots</button>
                    <button class="ai-chip" onclick="sendQuickChip('Free Site Visit kaise book karein?')">🚗 Free Site Visit</button>
                    <button class="ai-chip" onclick="sendQuickChip('Plot prices & Bank Loan')">💰 Price & Loan Info</button>
                    <button class="ai-chip" onclick="sendQuickChip('Direct Anshu Dubey se WhatsApp par baat karni hai')">💬 WhatsApp Anshu Dubey</button>
                </div>
            </div>

            <div class="ai-chat-footer">
                <input type="text" id="ai-chat-input" placeholder="Apna sawal yahan likhein..." onkeypress="handleAIKeyPress(event)">
                <button id="ai-send-btn" onclick="sendAIMessage()">
                    <i class="fa-solid fa-paper-plane"></i>
                </button>
            </div>
        </div>
    </div>

    <script>
    function toggleAIChat() {
        var win = document.getElementById('ai-chat-window');
        var bubble = document.getElementById('ai-tooltip-bubble');
        if (bubble) bubble.style.display = 'none';
        if (win.classList.contains('ai-chat-hidden')) {
            win.classList.remove('ai-chat-hidden');
        } else {
            win.classList.add('ai-chat-hidden');
        }
    }

    function sendQuickChip(text) {
        appendUserMsg(text);
        processAIResponse(text);
    }

    function handleAIKeyPress(e) {
        if (e.key === 'Enter') {
            sendAIMessage();
        }
    }

    function sendAIMessage() {
        var input = document.getElementById('ai-chat-input');
        var text = input.value.trim();
        if (!text) return;
        input.value = '';
        appendUserMsg(text);
        processAIResponse(text);
    }

    function appendUserMsg(text) {
        var container = document.getElementById('ai-chat-messages');
        var div = document.createElement('div');
        div.className = 'ai-msg ai-msg-user';
        div.innerHTML = '<div class="ai-msg-bubble">' + escapeHTML(text) + '</div><span class="ai-msg-time">Just now</span>';
        container.appendChild(div);
        container.scrollTop = container.scrollHeight;
    }

    function appendBotMsg(htmlText) {
        var container = document.getElementById('ai-chat-messages');
        var div = document.createElement('div');
        div.className = 'ai-msg ai-msg-bot';
        div.innerHTML = '<div class="ai-msg-bubble">' + htmlText + '</div><span class="ai-msg-time">Just now</span>';
        container.appendChild(div);
        container.scrollTop = container.scrollHeight;
    }

    function processAIResponse(query) {
        var q = query.toLowerCase();
        setTimeout(function() {
            if (q.includes('vda') || q.includes('plot') || q.includes('location')) {
                appendBotMsg('Humare paas Varanasi Ring Road, Shivpur, Babatpur Highway par VDA Approved plots hain complete legal registry papers ke sath.<br><br><a href="https://wa.me/918303727724?text=Mujhe%20VDA%20plots%20list%20chahiye" target="_blank" style="color:#C89B3C; font-weight:700;">👉 Direct WhatsApp Par Plots List Dekhein</a>');
            } else if (q.includes('visit') || q.includes('site') || q.includes('free') || q.includes('car')) {
                appendBotMsg('Humari taraf se Free Car Site Visit facility bilkul free hai! Aap jab chahein site dekhne chal sakte hain.<br><br><a href="https://wa.me/918303727724?text=Mujhe%20Free%20Site%20Visit%20book%20karni%20hai" target="_blank" style="color:#25D366; font-weight:700;">🚗 Abhi Free Site Visit Book Karein</a>');
            } else if (q.includes('price') || q.includes('rate') || q.includes('loan') || q.includes('bank')) {
                appendBotMsg('Plots starting attractive budgets mein hain aur sabhi major Banks se Loan Approval support milta hai.<br><br>Direct owner Anshu Dubey ji se baat karein: <a href="tel:+918303727724" style="color:#C89B3C; font-weight:700;">📞 +91 83037 27724</a>');
            } else {
                appendBotMsg('Aapka sawal Anshu Dubey ji ko forward kar diya gaya hai. Direct baat karne ke liye WhatsApp par message karein:<br><br><a href="https://wa.me/918303727724?text=Namaste%20Anshu%20ji,%20mujhe%20jankari%20chahiye" target="_blank" style="color:#25D366; font-weight:700;">💬 Direct WhatsApp Open Karein</a>');
            }
        }, 500);
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, function(tag) {
            return {'&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'}[tag] || tag;
        });
    }
    </script>
"@

$files = @("d:\ansu\website\landing-page.html", "d:\ansu\website\index.html", "d:\ansu\website\AnshuProperties.com.html")

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding UTF8
        if ($content -notmatch "ai-assistant-wrapper") {
            if ($content -match "</style>") {
                $content = $content -replace "</style>", "$css`n</style>"
            } elseif ($content -match "</head>") {
                $content = $content -replace "</head>", "<style>$css</style>`n</head>"
            }

            if ($content -match "</body>") {
                $content = $content -replace "</body>", "$htmlJs`n</body>"
            }

            Set-Content $file -Value $content -Encoding UTF8
            Write-Host "Updated $file"
        }
    }
}
