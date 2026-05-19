# Common Application Layer Protocols

## 📊 Summary based on the 80/20 principle

### 1. Application protocols define purpose, port and security level
The essence of the 80/20 principle is this: at the application layer, the protocol determines which task is performed and how secure it is. Email protocols, file transfer and remote access – including their standard ports and security differences – are particularly important.

### 2. Step-by-step core process
1. First, determine the intended use: sending email, retrieving email, transferring files or accessing systems.
2. Assign the appropriate protocol, for example SMTP, IMAP, FTP or SSH.
3. Check the standard port, as it appears constantly in firewalls, logs and packet captures.
4. Then assess whether the protocol uses plain text or encryption.
5. Give preference to secure variants such as IMAPS, FTPS, SFTP or SSH over outdated plaintext protocols.

### 3. Interactive mode / Tool usage
These protocols become particularly clear when you sort them by function and risk. The most important practical question is almost always: What function does the protocol fulfil, and is the connection secure or open to eavesdropping?

### 4. Key concepts with code examples
- **SMTP:** Sends emails from the client to the mail server or between mail servers.
- **POP3 and IMAP:** Retrieve emails, but with very different operating models.
- **FTP:** Transfers files, but is insecure in its basic version.
- **SSH:** Secure remote access with encryption.
- **RDP:** Graphical remote access, primarily in a Windows environment.

```bash
ssh analyst@example-server

# Example of a classic FTP call
ftp ftp.dlptest.com
```

### 5. Comparison: Insecure legacy protocols vs. secure alternatives
- **Telnet** transmits login credentials in plain text, **SSH** encrypts the entire session.
- **FTP** sends data and login credentials in the clear by default, **FTPS** or **SFTP** protect the transfer.
- **POP3** often downloads emails locally, **IMAP** keeps them synchronised on the server across multiple devices.

### 6. Why is this important / Benefits
Those familiar with these protocols can analyse traffic more quickly, identify suspicious ports, detect misconfigurations and make better decisions regarding secure services.

**Quick-start checklist**
- ☐ I can distinguish between SMTP, POP3 and IMAP in terms of their functionality.
- ☐ I know why FTP and Telnet are considered insecure.
- ☐ I know SSH as a secure alternative for remote access.
- ☐ I can roughly identify typical ports such as 22, 21, 23, 25, 143, 993 and 3389.
- ☐ I understand that ‘same destination’ does not automatically mean ‘same security level’.

**Key point**
When it comes to application protocols, it is not enough to know what they are for; you also need to know whether they transmit data securely or in plain text.

---

## Table 1: Tools used
| Tool | Purpose |
|---|---|
| SSH Client | Secure remote access to systems |
| FTP Client | Classic tool for file transfers |
| Mail Client | Uses SMTP as well as POP3 or IMAP for email communication |
| Remote Desktop Client | Provides graphical access to remote systems via RDP |

## Table 2: Technical Terms
| Term | Meaning |
|---|---|
| SMTP | Protocol for sending emails |
| POP3 | Protocol for retrieving emails with a focus on local download |
| IMAP | Protocol for server-based management and synchronisation of emails |
| FTP | Classic protocol for file transfer |
| SSH | Encrypted protocol for remote login and other services |
| RDP | Protocol for graphical remote access to remote systems |

## Table 3: Key terms
| Term | Meaning |
|---|---|
| retrieve | retrieve |
| submission | submission |
| plaintext | plain text |
| encrypted | encrypted |
| remote access | remote access |
| sync | synchronise |


