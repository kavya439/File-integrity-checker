# File-integrity-checker
COMPANY:CODTECH IT SOLUTIONS
NAME:P.KAVYANJALI
INTERN ID:CT06DZ757
DOMAIN:CYBER SECURITY & ETHICAL HACKING
DURATION:6 WEEKS
MENTOR:NEELA SANTHOSH KUMAR

*DESCRIPTION:*
A File Integrity Checker (FIC) is a security tool used to monitor and verify the integrity of files and directories on a computer system. Its primary function is to detect unauthorized changes, whether accidental or malicious, to critical system files, configuration files, or application data. The checker does this by comparing the current state of files against a known good baseline and reporting any modifications, additions, or deletions.It ensures the integrity and security of files by tracking any modifications, additions, or deletions over time.
When first run, the FIC generates a baseline database of file metadata. This typically includes file hashes (e.g., SHA-256), sizes, permissions, ownership, and timestamps. Over time, the system periodically or continuously checks these files and compares them against the baseline.

*How It Works*
The process typically involves:
1.Baseline Creation: The system scans selected directories and stores metadata and cryptographic checksums (hashes) of each file.
2.Periodic Scanning or Real-Time Monitoring: Depending on configuration, the tool either runs scheduled checks or watches files in real-time for changes.
3.Comparison & Reporting: Differences between current file states and the baseline are recorded and reported, often with classifications: modified, added, or deleted.
4.Alerting & Logging: The tool logs all detected changes and can alert system administrators through email, SMS, or integration with SIEM systems.

*What’s Used:*
os – To go through files and folders.
hashlib – To create SHA-256 hashes.
json – To save and load the hashes in a file (hashes.json).

Conclusion:
A File Integrity Checker is a critical tool in a system administrator’s and security professional’s toolkit. By detecting modified, added, and deleted files, it provides clear visibility into the integrity of systems and serves as an early-warning system for potential compromise. When configured properly and used as part of a comprehensive cybersecurity strategy, FICs greatly enhance an organization’s ability to maintain secure and resilient computing environments.A File Integrity Checker becomes a key part of protecting computers and keeping the system secure and stable.



