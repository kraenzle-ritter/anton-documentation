# Passkeys 

## What are passkeys?

Passkeys are a modern and secure alternative to the conventional password. Instead of having to remember a password, you use:

- **Fingerprint** (Touch ID)
- **Face recognition** (Face ID)
- **PIN or screen lock** of your device
- **Hardware security key** (e.g. YubiKey)

Passkeys are more secure than passwords because they cannot be stolen, guessed or captured by phishing attacks.

## Prerequisites

- Your archive must have the passkey function activated
- A modern browser (Chrome, Safari, Firefox, Edge)
- A device with biometric authentication or a security key

## Setting up a passkey

1. **Log in with your password** (as usual)
2. **Open your profile** via the user menu
3. **Navigate to «Security» or «Passkeys»**
4. **Click «Add passkey»**
5. **Follow the instructions from your browser or device**:
   - Confirm with fingerprint, Face ID or PIN
   - The passkey is saved automatically on your device
6. **Assign a name** to the passkey (e.g. «MacBook office», «iPhone»)

> **Tip:** You can set up several passkeys for different devices.

## Logging in with a passkey

1. **Open Anton's login page**
2. **Click «Log in with passkey»**
3. **Confirm with your fingerprint, Face ID or PIN**
4. You are logged in – without a password!

## Managing passkeys

In your profile you can:

- **View all registered passkeys**
- **Rename passkeys** (for a better overview)
- **Delete passkeys** (if a device is lost, for example)

## Frequently asked questions

### Can I still use my password?
Yes, passkeys are an additional way to log in. Your password continues to work.

### What happens if a device is lost?
Log in with your password and delete the passkey of the lost device in your profile.

### Does the passkey work on other devices?
Depending on the system (iCloud, Google Password Manager, Windows Hello), passkeys can be synchronised across devices. Security keys are tied to the physical device.

### Is two-factor authentication still necessary?
Passkeys are considered very secure and can replace two-factor authentication – this depends on the settings of your archive.

## Advantages at a glance

| Password | Passkey |
|----------|---------|
| Can be forgotten | Always with you on your device |
| Can be stolen | Cryptographically protected |
| Risk of phishing | Immune to phishing |
| Complex rules | Simple to use |


## Technical background

Passkeys are based on the WebAuthn standard (FIDO2). On registration, a cryptographic key pair is created:
- The **private key** remains securely on your device
- The **public key** is stored in Anton

When logging in, your device proves that it possesses the private key – without ever transmitting it.

*Last updated: February 2026*
