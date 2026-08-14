/* ==========================================================================
   RAGINI AI CHAT ASSISTANT - GLOBAL JAVASCRIPT & CONVERSATION ENGINE
   ========================================================================== */

(function () {
    // Ensure CSS is loaded
    if (!document.getElementById('ragini-assistant-css')) {
        const link = document.createElement('link');
        link.id = 'ragini-assistant-css';
        link.rel = 'stylesheet';
        link.href = 'css/ragini-assistant.css';
        document.head.appendChild(link);
    }

    // State management
    const state = {
        mode: null, // 'buy' or 'sell'
        step: 0,
        data: {
            mode: '',
            location: '',
            budget: '',
            sizeType: '',
            urgency: '',
            vdaStatus: '',
            expectedPrice: '',
            docsStatus: '',
            name: '',
            phone: ''
        }
    };

    // Inject HTML structure on DOM ready
    function initRaginiWidget() {
        if (document.getElementById('ragini-widget-container')) return;

        const widgetHTML = `
            <div id="ragini-widget-container">
                <!-- Floating Tooltip Bubble -->
                <div id="ragini-tooltip">
                    <span class="ragini-tooltip-close" onclick="document.getElementById('ragini-tooltip').style.display='none'">&times;</span>
                    <div>
                        <strong>Namaste!</strong> I am Ragini, Anshu Property AI Assistant. Are you looking to buy or sell property?
                    </div>
                </div>

                <!-- Floating Gold Trigger Button -->
                <button id="ragini-trigger-btn" onclick="toggleRaginiChat()" aria-label="Chat with Ragini AI Assistant">
                    <img src="assets/ai_female_assistant.jpg" alt="Ragini AI Assistant" class="ragini-trigger-img">
                    <span class="ragini-online-dot"></span>
                </button>

                <!-- Chat Box Window -->
                <div id="ragini-chat-box" class="ragini-hidden">
                    <!-- Navy Header -->
                    <div class="ragini-header">
                        <div class="ragini-header-left">
                            <div class="ragini-header-avatar">
                                <img src="assets/ai_female_assistant.jpg" alt="Ragini AI Assistant">
                            </div>
                            <div class="ragini-header-info">
                                <h4>Ragini <span style="font-size:0.68rem; background:rgba(200,155,60,0.25); color:#C89B3C; padding:2px 8px; border-radius:8px;">AI Support</span></h4>
                                <div class="ragini-status-indicator">
                                    <span class="ragini-status-dot"></span> Online | Anshu Property
                                </div>
                            </div>
                        </div>
                        <button class="ragini-close-btn" onclick="toggleRaginiChat()">&times;</button>
                    </div>

                    <!-- Messages Body (Ivory Background) -->
                    <div class="ragini-messages-body" id="ragini-msg-container">
                        <!-- Initial Greeting -->
                        <div class="ragini-msg-row ragini-msg-left">
                            <div class="ragini-bubble">
                                Namaste! 🙏 Welcome to <strong>Anshu Property</strong>.<br><br>
                                I am <strong>Ragini</strong>, your virtual real estate guide. How can I help you today?
                            </div>
                            <span class="ragini-msg-time">Just now</span>
                        </div>
                    </div>

                    <!-- Input Footer -->
                    <div class="ragini-footer">
                        <input type="text" id="ragini-input" placeholder="Type your answer here..." onkeypress="handleRaginiKeyPress(event)">
                        <button id="ragini-send-btn" onclick="sendRaginiUserMessage()">
                            <i class="fa-solid fa-paper-plane"></i>
                        </button>
                    </div>
                </div>
            </div>
        `;

        document.body.insertAdjacentHTML('beforeend', widgetHTML);

        // Start initial conversation step after small delay
        setTimeout(startInitialFlow, 400);
    }

    // Toggle Chat Window
    window.toggleRaginiChat = function () {
        const box = document.getElementById('ragini-chat-box');
        const tooltip = document.getElementById('ragini-tooltip');
        if (tooltip) tooltip.style.display = 'none';

        if (box.classList.contains('ragini-hidden')) {
            box.classList.remove('ragini-hidden');
            document.getElementById('ragini-input').focus();
        } else {
            box.classList.add('ragini-hidden');
        }
    };
    
    // Alias for backward compatibility
    window.togglePriyaChat = window.toggleRaginiChat;

    // Initial Conversation Step
    function startInitialFlow() {
        appendBotMsgWithChips(
            "Please select your requirement to get started:",
            [
                { label: "🏡 I want to BUY Property (Plot Khareedna)", value: "buy" },
                { label: "🔑 I want to SELL Property (Plot Bechna)", value: "sell" }
            ]
        );
    }

    // User selected buy or sell
    window.handleRaginiChoice = function (choice) {
        if (choice === 'buy') {
            state.mode = 'buy';
            state.data.mode = 'BUYER';
            appendUserMsg("I want to BUY Property");
            setTimeout(() => askBuyStep(1), 500);
        } else if (choice === 'sell') {
            state.mode = 'sell';
            state.data.mode = 'SELLER';
            appendUserMsg("I want to SELL Property");
            setTimeout(() => askSellStep(1), 500);
        }
    };
    
    window.handlePriyaChoice = window.handleRaginiChoice;

    // BUYER QUESTION FLOW
    function askBuyStep(stepNum) {
        state.step = stepNum;

        if (stepNum === 1) {
            appendBotMsgWithChips(
                "Great! Which location or area are you interested in?",
                [
                    { label: "📍 Varanasi Ring Road / Shivpur", value: "Varanasi Ring Road / Shivpur" },
                    { label: "📍 Babatpur Highway / Airport Road", value: "Babatpur Highway" },
                    { label: "📍 Allahabad / Prayagraj Region", value: "Allahabad" },
                    { label: "📍 Bihar / Madhya Pradesh", value: "Bihar / MP" }
                ]
            );
        } else if (stepNum === 2) {
            appendBotMsgWithChips(
                "Got it! What is your estimated budget for the plot?",
                [
                    { label: "💰 ₹15 Lakhs - ₹30 Lakhs", value: "15-30 Lakhs" },
                    { label: "💰 ₹30 Lakhs - ₹60 Lakhs", value: "30-60 Lakhs" },
                    { label: "💰 ₹60 Lakhs+", value: "60L+" },
                    { label: "💰 Need Budget Guidance", value: "Flexible" }
                ]
            );
        } else if (stepNum === 3) {
            appendBotMsgWithChips(
                "What type and size of plot are you looking for?",
                [
                    { label: "🏡 Residential Plot (1000 - 2000 sq ft)", value: "Residential 1000-2000 sqft" },
                    { label: "🏢 Commercial / Highway Plot", value: "Commercial Plot" },
                    { label: "🌳 Larger Land / Farmhouse", value: "Large Land" }
                ]
            );
        } else if (stepNum === 4) {
            appendBotMsgWithChips(
                "How soon are you planning to finalize your plot?",
                [
                    { label: "⚡ Immediately (Within 15 days)", value: "Immediate" },
                    { label: "📅 Within 1 to 3 Months", value: "1-3 Months" },
                    { label: "🔍 Just Exploring & Researching", value: "Exploring" }
                ]
            );
        } else if (stepNum === 5) {
            appendBotMsg("Thank you! Lastly, please share your <strong>Full Name</strong> and <strong>Phone Number</strong> so Mr. Anshu Dubey can send you full plot maps and legal details.");
        }
    }

    // SELLER QUESTION FLOW
    function askSellStep(stepNum) {
        state.step = stepNum;

        if (stepNum === 1) {
            appendBotMsg("Where is your plot located and what is the approximate size (sq ft / biswa)?");
        } else if (stepNum === 2) {
            appendBotMsgWithChips(
                "Is your plot VDA Approved or UP RERA Registered?",
                [
                    { label: "✅ VDA Approved / RERA Registered", value: "VDA / RERA Approved" },
                    { label: "📄 Freehold / Private Land", value: "Freehold Land" },
                    { label: "❓ Not sure / Need Verification", value: "Unsure" }
                ]
            );
        } else if (stepNum === 3) {
            appendBotMsg("What is your expected selling price for the property?");
        } else if (stepNum === 4) {
            appendBotMsgWithChips(
                "Are all registry, khatauni, and title documents clear and ready?",
                [
                    { label: "✅ Yes, 100% Clear & Ready", value: "Docs Ready" },
                    { label: "⏳ In Process / Need Assistance", value: "Docs In Process" }
                ]
            );
        } else if (stepNum === 5) {
            appendBotMsg("Got it! Please enter your <strong>Full Name</strong> and <strong>Phone Number</strong> so we can evaluate your property and connect with you directly.");
        }
    }

    // Handle Manual Input Submissions
    window.handleRaginiKeyPress = function (e) {
        if (e.key === 'Enter') {
            sendRaginiUserMessage();
        }
    };
    window.handlePriyaKeyPress = window.handleRaginiKeyPress;

    window.sendRaginiUserMessage = function () {
        const input = document.getElementById('ragini-input');
        const text = input.value.trim();
        if (!text) return;
        input.value = '';

        appendUserMsg(text);
        processUserText(text);
    };
    window.sendPriyaUserMessage = window.sendRaginiUserMessage;

    function processUserText(text) {
        if (state.mode === 'buy') {
            if (state.step === 5) {
                state.data.namePhone = text;
                parseNamePhone(text);
                completeLeadFlow();
                return;
            }
        } else if (state.mode === 'sell') {
            if (state.step === 1) {
                state.data.location = text;
                setTimeout(() => askSellStep(2), 500);
                return;
            } else if (state.step === 3) {
                state.data.expectedPrice = text;
                setTimeout(() => askSellStep(4), 500);
                return;
            } else if (state.step === 5) {
                state.data.namePhone = text;
                parseNamePhone(text);
                completeLeadFlow();
                return;
            }
        }

        const q = text.toLowerCase();
        setTimeout(() => {
            if (q.includes('price') || q.includes('rate') || q.includes('cost')) {
                appendBotMsg("Our plots start from attractive price points depending on location. Would you like to check specific VDA plots on WhatsApp?<br><br><a href='https://wa.me/918303727724?text=Hello%20Anshu%20ji,%20I%20want%20to%20know%20plot%20prices' target='_blank' style='color:#25D366; font-weight:700;'>💬 Connect on WhatsApp (+91 83037 27724)</a>");
            } else if (q.includes('contact') || q.includes('phone') || q.includes('anshu')) {
                appendBotMsg("You can connect directly with owner <strong>Mr. Anshu Dubey</strong>:<br>📞 Call: <strong>+91 83037 27724</strong><br>✉️ Email: <strong>anshudubey3409@gmail.com</strong><br><br><a href='https://wa.me/918303727724' target='_blank' style='color:#25D366; font-weight:700;'>💬 Open Direct WhatsApp Chat</a>");
            } else {
                appendBotMsg("Thank you for your message! For detailed custom inquiries, you can reach Mr. Anshu Dubey directly on WhatsApp:<br><br><a href='https://wa.me/918303727724?text=Hello%20Anshu%20ji,%20I%20have%20a%20question%20about%20property' target='_blank' style='color:#25D366; font-weight:700;'>💬 Chat Directly on WhatsApp (+91 83037 27724)</a>");
            }
        }, 500);
    }

    function parseNamePhone(text) {
        state.data.name = text;
        const phoneMatch = text.match(/[0-9]{10}/);
        if (phoneMatch) {
            state.data.phone = phoneMatch[0];
        }
    }

    // Option Button Click Handler
    window.selectChipValue = function (val, label) {
        if (val === 'buy' || val === 'sell') {
            handleRaginiChoice(val);
            return;
        }

        appendUserMsg(label);

        if (state.mode === 'buy') {
            if (state.step === 1) {
                state.data.location = val;
                setTimeout(() => askBuyStep(2), 500);
            } else if (state.step === 2) {
                state.data.budget = val;
                setTimeout(() => askBuyStep(3), 500);
            } else if (state.step === 3) {
                state.data.sizeType = val;
                setTimeout(() => askBuyStep(4), 500);
            } else if (state.step === 4) {
                state.data.urgency = val;
                setTimeout(() => askBuyStep(5), 500);
            }
        } else if (state.mode === 'sell') {
            if (state.step === 2) {
                state.data.vdaStatus = val;
                setTimeout(() => askSellStep(3), 500);
            } else if (state.step === 4) {
                state.data.docsStatus = val;
                setTimeout(() => askSellStep(5), 500);
            }
        }
    };

    // Complete Lead & Trigger Notification
    function completeLeadFlow() {
        const lead = state.data;

        // Save to LocalStorage
        try {
            const existingLeads = JSON.parse(localStorage.getItem('anshu_property_leads') || '[]');
            existingLeads.push({ ...lead, timestamp: new Date().toISOString() });
            localStorage.setItem('anshu_property_leads', JSON.stringify(existingLeads));
        } catch (e) {
            console.error('LocalStorage save error', e);
        }

        // Format WhatsApp Message for instant owner notification
        let summaryMsg = `🚨 *NEW WEBSITE LEAD (RAGINI AI ASSISTANT)* 🌐\n-------------------------\n`;
        summaryMsg += `📋 *Type:* ${lead.mode}\n`;
        if (lead.mode === 'BUYER') {
            summaryMsg += `📍 *Location:* ${lead.location}\n💰 *Budget:* ${lead.budget}\n🏡 *Plot Type:* ${lead.sizeType}\n⚡ *Timeline:* ${lead.urgency}\n`;
        } else {
            summaryMsg += `📍 *Location & Size:* ${lead.location}\n📄 *VDA/RERA:* ${lead.vdaStatus}\n💰 *Expected Price:* ${lead.expectedPrice}\n📝 *Docs:* ${lead.docsStatus}\n`;
        }
        summaryMsg += `👤 *Contact Info:* ${lead.name}\n`;
        summaryMsg += `-------------------------\n🌐 *Source:* AnshuProperties.com (Ragini AI Chat)`;

        const encodedWhatsApp = encodeURIComponent(summaryMsg);
        const waLink = `https://wa.me/918303727724?text=${encodedWhatsApp}`;

        appendBotMsg(`
            🎉 <strong>Thank You! Your details have been submitted.</strong><br><br>
            Redirecting you directly to WhatsApp...<br><br>
            <a href="${waLink}" target="_blank" style="display:inline-flex; align-items:center; gap:8px; background:#25D366; color:#FFF; padding:10px 18px; border-radius:20px; font-weight:700; text-decoration:none;">
                <i class="fa-brands fa-whatsapp" style="font-size:1.2rem;"></i> Open WhatsApp Now
            </a>
        `);

        // Automatically open WhatsApp directly
        setTimeout(function() {
            window.open(waLink, '_blank') || (window.location.href = waLink);
        }, 600);
    }

    // UI Append Helper Functions
    function appendUserMsg(text) {
        const container = document.getElementById('ragini-msg-container');
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const html = `
            <div class="ragini-msg-row ragini-msg-right">
                <div class="ragini-bubble">${escapeHTML(text)}</div>
                <span class="ragini-msg-time">${time}</span>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', html);
        container.scrollTop = container.scrollHeight;
    }

    function appendBotMsg(htmlContent) {
        const container = document.getElementById('ragini-msg-container');
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const html = `
            <div class="ragini-msg-row ragini-msg-left">
                <div class="ragini-bubble">${htmlContent}</div>
                <span class="ragini-msg-time">${time}</span>
            </div>
        `;
        container.insertAdjacentHTML('beforeend', html);
        container.scrollTop = container.scrollHeight;
    }

    function appendBotMsgWithChips(questionText, chipsArray) {
        let chipsHTML = `<div class="ragini-options-grid">`;
        chipsArray.forEach(chip => {
            chipsHTML += `
                <button class="ragini-opt-btn" onclick="selectChipValue('${chip.value}', '${chip.label}')">
                    <span>${chip.label}</span>
                    <i class="fa-solid fa-chevron-right" style="font-size:0.75rem;"></i>
                </button>
            `;
        });
        chipsHTML += `</div>`;

        appendBotMsg(`<div>${questionText}</div>${chipsHTML}`);
    }

    function escapeHTML(str) {
        return str.replace(/[&<>'"]/g, tag => ({
            '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;'
        }[tag] || tag));
    }

    // Run Initialization on Load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initRaginiWidget);
    } else {
        initRaginiWidget();
    }
})();
