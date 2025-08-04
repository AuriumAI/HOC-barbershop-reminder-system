# HOC-Barbershop-Reminder-System
Appointment reminder system for House of Cuts using SES and Lambda, with CodePipeline deploying updates automatically from GitHub
# 💈 Barbershop Appointment Reminder System

This project is a lightweight, serverless appointment reminder tool built on AWS. It's designed to automatically send email reminders to barbershop clients when their appointments are scheduled—helping reduce no-shows and improve operational efficiency.

## 🧠 Why This Exists

As a barber and cloud architect, I’ve seen firsthand how missed appointments can hurt small businesses. This project automates the reminder process using AWS-native tools, offering a no-maintenance solution that’s scalable and easy to replicate for other businesses.

## 🔧 What It Does
- Reads a list of client appointments from a JSON file (`appointments.json`)
- Sends personalized email reminders via Amazon SES
- Automatically re-deploys and runs when updated via GitHub using CI/CD
- Entire stack is provisioned using AWS CloudFormation (Infrastructure as Code)

## 🚀 Architecture Overview
```
GitHub Repo (appointments.json, code)
↓
AWS CodePipeline → CodeBuild → Package Code
↓
AWS Lambda Function
↓
Amazon SES → Sends Reminder Emails
```
## ⚙️ Tech Stack
- AWS Lambda (Python 3.11)
- Amazon SES (email sending)
- AWS CodePipeline + CodeBuild (CI/CD)
- AWS CloudFormation (IaC)
- GitHub (source + trigger)

## 📂 Repo Structure
```
barbershop-reminder-system/
├── appointments.json     # List of upcoming client appointments
├── lambda_function.py    # Lambda logic to send reminders
├── buildspec.yml         # Build instructions for CodeBuild
└── template.yaml         # CloudFormation template for full infrastructure
```
---
## 🛠️ Deployment Instructions

1. **Verify SES Sender Email**
   - Go to AWS SES → Verify your email (you'll receive a confirmation email)

2. **Deploy Infrastructure**
   - Use `template.yaml` in AWS CloudFormation
   - Input your verified email when prompted

3. **Configure CodePipeline**
   - Set up CodePipeline with:
     - Source: this GitHub repo
     - Build: CodeBuild with `buildspec.yml`

4. **Test the System**
   - Edit `appointments.json` → commit + push
   - Watch the pipeline deploy and Lambda send emails
   - Or manually trigger the Lambda from the AWS console

## 🧪 Example Appointment Entry

```json
{
  "name": "Jordan",
  "email": "jordan@example.com",
  "appointment_time": "2025-08-04T15:00:00"
}
