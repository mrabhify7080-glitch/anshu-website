$files = @(
    'd:\ansu\website\index.html',
    'd:\ansu\website\AnshuProperties.com.html',
    'd:\ansu\website\about.html',
    'd:\ansu\website\properties.html',
    'd:\ansu\website\services.html',
    'd:\ansu\website\contact.html',
    'd:\ansu\website\blog.html',
    'd:\ansu\website\landing-page.html',
    'd:\ansu\website\js\ragini-assistant.js',
    'd:\ansu\website\js\priya-assistant.js'
)

foreach ($file in $files) {
    if (Test-Path $file) {
        $content = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
        
        # Meta & Header descriptions
        $content = $content.Replace('offering VDA approved & UP RERA registered plots', 'offering 100% verified & clear-title plots')
        $content = $content.Replace('offering VDA approved &amp; UP RERA registered plots', 'offering 100% verified &amp; clear-title plots')
        $content = $content.Replace('VDA approved plots Varanasi', 'verified plots Varanasi')
        $content = $content.Replace('Explore VDA Approved & UP RERA Registered plots', 'Explore 100% Verified & Clear-Title plots')
        $content = $content.Replace('Explore VDA Approved &amp; UP RERA Registered plots', 'Explore 100% Verified &amp; Clear-Title plots')
        $content = $content.Replace('Explore VDA approved plots in Varanasi', 'Explore 100% verified residential plots in Varanasi')
        $content = $content.Replace('Buy VDA approved plots and UP RERA registered properties', 'Buy 100% verified clear-title plots and registered properties')
        $content = $content.Replace('Buy VDA Approved plots and UP RERA registered residential', 'Buy 100% verified clear-title residential')
        $content = $content.Replace('Buy VDA Approved plots', 'Buy 100% Verified Plots')
        $content = $content.Replace('VDA Approved Plots', 'Verified Residential Plots')
        $content = $content.Replace('VDA Approved plots', 'Verified Residential plots')
        $content = $content.Replace('VDA approved plots', 'verified residential plots')
        $content = $content.Replace('VDA approved plot', 'verified residential plot')
        $content = $content.Replace('We specialize in VDA Approved plots and RERA registered properties', 'We specialize in 100% verified clear-title plots and registered properties')
        $content = $content.Replace('Specializing in VDA Approved &amp; UP RERA Registered plots', 'Specializing in 100% Verified &amp; Clear-Title plots')
        $content = $content.Replace('Specializing in VDA Approved & UP RERA Registered plots', 'Specializing in 100% Verified & Clear-Title plots')
        $content = $content.Replace('Specializing in VDA Approved', 'Specializing in 100% Verified & Clear-Title')
        $content = $content.Replace('Expert tips on VDA approved plots, UP RERA verification', 'Expert tips on verified plots, land title verification')
        $content = $content.Replace('VDA plot verification, UP RERA guidelines', 'Plot title verification, land registry guidelines')
        $content = $content.Replace('VDA plot verification guide', 'Plot legal verification guide')
        $content = $content.Replace('VDA plot buying, UP RERA legal desk', 'Residential plot buying, legal title desk')
        $content = $content.Replace('chat on WhatsApp for VDA approved plots and site visit bookings', 'chat on WhatsApp for verified plots and site visit bookings')
        
        # Hero & Trust stats
        $content = $content.Replace('brings you VDA Approved &amp; UP RERA Registered plots', 'brings you 100% legally verified &amp; clear-title plots')
        $content = $content.Replace('brings you VDA Approved & UP RERA Registered plots', 'brings you 100% legally verified & clear-title plots')
        $content = $content.Replace('<span>VDA &amp; RERA Vetted</span>', '<span>100% Legally Vetted</span>')
        $content = $content.Replace('<span>VDA & RERA Vetted</span>', '<span>100% Legally Vetted</span>')
        $content = $content.Replace('alt="VDA Approved Plot in Varanasi"', 'alt="Verified Residential Plot in Varanasi"')
        $content = $content.Replace('<strong>VDA Approved</strong><span>Varanasi Development Authority</span>', '<strong>100% Clear Title</strong><span>Immediate Registry &amp; Mutation</span>')
        $content = $content.Replace('<strong>VDA Approved</strong>', '<strong>100% Clear Title</strong>')
        $content = $content.Replace('<span>Varanasi Development Authority</span>', '<span>Immediate Registry &amp; Mutation</span>')
        $content = $content.Replace('VDA &amp; RERA Approved Plots', 'Verified &amp; Clear-Title Plots')
        $content = $content.Replace('VDA & RERA Approved Plots', 'Verified & Clear-Title Plots')
        $content = $content.Replace('<h4>VDA Approved Plots</h4>', '<h4>Verified Residential Plots</h4>')
        $content = $content.Replace('<h3>VDA Approved Plots</h3>', '<h3>Verified Residential Plots</h3>')
        $content = $content.Replace('<h4>VDA Approved Plot Buying</h4>', '<h4>Prime Residential Plot Buying</h4>')
        $content = $content.Replace('<option>VDA Approved Plot</option>', '<option>Residential Plot</option>')
        $content = $content.Replace('<span class="pc-badge">VDA Approved</span>', '<span class="pc-badge">Verified Plot</span>')
        $content = $content.Replace('| VDA &amp; RERA Approved', '| 100% Clear Title')
        $content = $content.Replace('| VDA & RERA Approved', '| 100% Clear Title')
        $content = $content.Replace('VDA Approved Residential Plot in Shivpur', 'Prime Residential Plot in Shivpur')
        $content = $content.Replace('We offer VDA plots, independent homes', 'We offer verified residential plots, independent homes')
        $content = $content.Replace('VDA Approved Plots &amp; Homes', 'Verified Plots &amp; Homes')
        $content = $content.Replace('VDA Approved Plots & Homes', 'Verified Plots & Homes')
        $content = $content.Replace('strict VDA and RERA audits', 'strict legal title and revenue record audits')
        $content = $content.Replace('guided site visit for VDA approved plots in Varanasi', 'guided site visit for verified plots in Varanasi')
        $content = $content.Replace('Finding a genuine VDA approved plot near Kal Bhairav Mandir', 'Finding a genuine clear-title plot near Kal Bhairav Mandir')
        $content = $content.Replace('Got Questions About <br>VDA Approved Land?', 'Got Questions About <br>Plot Buying &amp; Registry?')
        $content = $content.Replace('Got Questions About VDA Approved Land?', 'Got Questions About Plot Buying &amp; Registry?')
        $content = $content.Replace('RERA aur VDA approval kaise verify karein?', 'Plot ki registry aur legal papers kaise verify karein?')
        $content = $content.Replace('VDA approved plots ka sanction map aur khatauni records hum client ko site visit par verify karwate hain.', 'Plots ke khatauni records, 143 legal clearance aur registry papers hum client ko site visit par verify karwate hain.')
        $content = $content.Replace('alt="VDA Guide"', 'alt="Plot Verification Guide"')
        $content = $content.Replace('A practical checklist covering VDA sanction maps, 143 clearance, and khatauni records.', 'A practical checklist covering Section 143 clearance, mutation, and khatauni records.')
        
        # Services & About
        $content = $content.Replace('Shortlisting legally sanctioned VDA residential &amp; commercial layouts in Shivpur', 'Shortlisting verified, clear-title residential &amp; commercial layouts in Shivpur')
        $content = $content.Replace('legally vetted, VDA approved, and RERA registered properties', 'legally vetted, clear-title, and verified registered properties')
        $content = $content.Replace('In-house legal team verifies VDA map approvals, khatauni records, and registry papers.', 'In-house legal team verifies legal titles, khatauni records, mutation, and registry papers.')
        $content = $content.Replace('Looking for VDA approved plot, villa, budget details, etc.', 'Looking for verified residential plot, villa, budget details, etc.')
        
        # Blog
        $content = $content.Replace('<span class="badge-premium">VDA Approval</span>', '<span class="badge-premium">Plot Verification</span>')
        $content = $content.Replace('1. VDA Approved Plot Kya Hota Hai Aur Yeh Kyun Zaruri Hai?', '1. Clear Title Residential Plot Kya Hota Hai Aur Registry Kaise Check Karein?')
        $content = $content.Replace('<strong>VDA (Varanasi Development Authority)</strong> approved plot ka matlab hai ki zameen ka layout naksha government ke master plan ke hisaab se officially pass aur sanctioned hai.', '<strong>Clear Title &amp; Verified Plot</strong> ka matlab hai ki zameen par koi purana vivad, bank mortgage ya legal issue nahi hai aur tehsil me registry aur dakhil kharij (mutation) instant hoti hai.')
        $content = $content.Replace('<li><strong>No Demolition Risk:</strong> VDA approved layout par ghar banane me future me koi sarkar dwara demolition ya legal notice ka khatra nahi hota.</li>', '<li><strong>Direct Registry &amp; Dakhil Kharij:</strong> 100% legal title zameen par turant sub-registrar office me registry aur khatauni me naam darj ho jata hai.</li>')
        $content = $content.Replace('Nationalized banks (SBI, HDFC, ICICI, Bank of Baroda) sirf VDA approved zameen par easily plot &amp; home loan sanction karte hain.', 'Nationalized banks (SBI, HDFC, ICICI, Bank of Baroda) clear title aur Section 143 sanctioned zameen par easily plot &amp; home loan sanction karte hain.')
        $content = $content.Replace('Anshu Property par hum sirf 100% VDA vetted residential layouts aur clear title zameen hi sell karte hain.', 'Anshu Property par hum sirf 100% legally vetted residential layouts aur clear title zameen hi sell karte hain.')
        $content = $content.Replace('<li><strong>VDA Sanctioned Layout Map:</strong> VDA dawra approved naksha.</li>', '<li><strong>Sanctioned Layout Map &amp; Demarcation:</strong> Patwari aur revenue officer dwara verified boundary map.</li>')
        $content = $content.Replace('agar aapki zameen VDA approved aur clear title hai', 'agar aapki zameen legally vetted aur clear title hai')
        $content = $content.Replace('Have Questions Regarding Land Registry or VDA Approval?', 'Have Questions Regarding Land Registry or Title Verification?')
        
        # Assistants
        $content = $content.Replace('"Is your plot VDA Approved or UP RERA Registered?"', '"What is your plot requirement or preferred location?"')
        $content = $content.Replace('VDA Approved / RERA Registered', '100% Clear Title / Ready Registry')
        $content = $content.Replace('VDA / RERA Approved', 'Clear Title / Ready Registry')
        $content = $content.Replace('VDA Approved plots list', 'Verified plots list')
        $content = $content.Replace('VDA plots list', 'Plots list')
        $content = $content.Replace('VDA Approved plots', 'Verified plots')
        $content = $content.Replace('VDA plots', 'Plots')
        $content = $content.Replace('VDA Approval Guide', 'Plot Verification Guide')
        $content = $content.Replace('How to Check VDA Approval for Plots in Varanasi (2026 Guide)', 'How to Verify Land Registry & Clear Title in Varanasi (2026 Guide)')
        $content = $content.Replace('VDA masterplan sanctions', '143 sanction and registry papers')
        $content = $content.Replace('VDA masterplan compliance', 'clear-title compliance')
        $content = $content.Replace('VDA masterplan updates', 'real estate updates')
        $content = $content.Replace('VDA plot options', 'plot options')
        $content = $content.Replace('VDA plot sales', 'residential plot sales')
        $content = $content.Replace('VDA Approved Plot Sales', 'Verified Plot Sales')
        $content = $content.Replace('VDA/RERA approved property', 'clear-title & verified property')
        $content = $content.Replace('VDA', 'Verified')
        
        [System.IO.File]::WriteAllText($file, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Processed $file"
    }
}
