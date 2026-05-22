from django.core.management.base import BaseCommand
from Portfolio.models import ComplianceLaw

class Command(BaseCommand):
    help = 'Seeds the database with Indian Labor Laws data'

    def handle(self, *args, **kwargs):
        laws_data = [
            {
                'category': 'Social Security & Welfare Acts',
                'name': "Employees' Provident Funds & Miscellaneous Provisions Act, 1952",
                'official_link': 'https://www.epfindia.gov.in/',
                'pdf_link': 'https://www.epfindia.gov.in/site_docs/PDFs/Downloads_PDFs/EPFO_Act_1952.pdf',
                'key_details': 'Mandates three combined safety nets: the retirement Provident Fund (EPF), the pension scheme (EPS), and structural life insurance coverage (EDLI). Contributions are shared between employers and employees (standard rate is 12%). Applies to establishments with 20 or more employees.'
            },
            {
                'category': 'Social Security & Welfare Acts',
                'name': "Employees' State Insurance Act, 1948",
                'official_link': 'https://www.esic.gov.in/',
                'pdf_link': 'https://www.esic.gov.in/Attachments/Act/ESI_ACT_1948.pdf',
                'key_details': 'Offers localized health insurance coverage, comprehensive medical benefits, and cash payouts during sickness, temporary/permanent disabilities, or death from industrial accidents. Applies to non-seasonal factories and specific service sectors employing 10 or more people. The statutory contribution rates stand at 3.25% for employers and 0.75% for workers earning up to Rs. 21,000 per month.'
            },
            {
                'category': 'Social Security & Welfare Acts',
                'name': 'Payment of Gratuity Act, 1972',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15174/1/payment_of_gratuity_act%2C_1972.pdf',
                'key_details': 'A mandatory terminal benefit given as a lump sum to employees upon separation (retirement, resignation, or superannuation) after completing a minimum of 5 years of continuous service. It is computed as 15 days of the last-drawn basic wage for every year of completed work, capped up to a maximum limit of Rs. 20 Lakhs. Applicable to establishments with 10 or more workers.'
            },
            {
                'category': 'Social Security & Welfare Acts',
                'name': 'Payment of Bonus Act, 1965',
                'official_link': 'https://labour.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/ThePaymentofBonusAct1965.pdf',
                'key_details': 'Requires specific accounting establishments to allocate a percentage of their annual allocable profits back to employees as a bonus. The statutory minimum bonus sits at 8.33% of wages, while the upper threshold is capped at 20%. Applies to any factory or commercial entity with 20 or more workers on any given operating day within the fiscal year.'
            },

            {
                'category': 'General Commercial, Operational & Wages Compliance',
                'name': 'Minimum Wages Act, 1948',
                'official_link': 'https://clc.gov.in/',
                'pdf_link': 'https://clc.gov.in/clc/sites/default/files/MinimumWagesact.pdf',
                'key_details': 'Empowers both state governments and central authorities to dynamically fix, review, and enforce base hourly or daily wage rates across listed scheduled employments. This ensures businesses cannot pay workers below the regional subsistence line.'
            },
            {
                'category': 'General Commercial, Operational & Wages Compliance',
                'name': 'Shops & Commercial Establishments Act (State-Specific)',
                'official_link': 'https://labour.delhi.gov.in/',
                'pdf_link': 'https://labour.delhi.gov.in/sites/default/files/Shops-and-Establishment-Act.pdf',
                'key_details': 'Enacted independently by individual state governments. It serves as the baseline operating architecture for non-factory commercial setups (offices, IT parks, retail shops, hotels). It dictates statutory guidelines on working shifts, rest time intervals, mandatory weekly off-days, and overtime wage calculations.'
            },
            {
                'category': 'General Commercial, Operational & Wages Compliance',
                'name': 'POSH Act, 2013 (Prevention of Sexual Harassment)',
                'official_link': 'https://wcd.nic.in/',
                'pdf_link': 'https://wcd.nic.in/sites/default/files/Sexual-Harassment-at-Workplace-Act.pdf',
                'key_details': 'Mandates a zero-tolerance structure against sexual harassment of women across all workspaces. Any company employing 10 or more staff members is legally required to establish an Internal Complaints Committee (ICC) to address complaints, document hearings, and maintain safe working environments.'
            },
            {
                'category': 'General Commercial, Operational & Wages Compliance',
                'name': 'Contract Labour (Regulation & Abolition) Act, 1970',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/17117/1/contract_labour_%28regulation_and_abolition%29_act%2C_1970.pdf',
                'key_details': 'Regulates the service conditions of contract workers in registered firms and aims to prevent their exploitation. It allows appropriate governments to completely abolish the use of contract labor in core, hazardous, or perennial operations. Standard central threshold applies to establishments or contractors employing 20 or more contract laborers.'
            },
            {
                'category': 'General Commercial, Operational & Wages Compliance',
                'name': 'Maternity Benefit Act, 1961',
                'official_link': 'https://labour.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/TheMaternityBenefitAct1961.pdf',
                'key_details': 'Ensures protection of employment and health for women before and after childbirth. It mandates 26 weeks of fully paid maternity leave for the first two children (and 12 weeks for subsequent children). Establishments with 50 or more employees must also provide a creche facility within a specified distance.'
            },

            {
                'category': 'The New Labor Codes Framework (Passed 2019–2020)',
                'name': 'The Code on Wages, 2019',
                'official_link': 'https://egazette.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/CodeonWages2019.pdf',
                'key_details': 'Replaces 4 historical acts: Minimum Wages Act, Payment of Wages Act, Payment of Bonus Act, and Equal Remuneration Act. It institutes a statutory national "Floor Wage" to standardize wage baselines across different regions.'
            },
            {
                'category': 'The New Labor Codes Framework (Passed 2019–2020)',
                'name': 'The Industrial Relations Code, 2020',
                'official_link': 'https://egazette.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/IR_Code_2020.pdf',
                'key_details': 'Consolidates the Industrial Disputes Act, Trade Unions Act, and Industrial Employment (Standing Orders) Act. It changes the threshold for industrial establishments to lay off workers or close operations without prior government approval from 100 workers to 300 workers.'
            },
            {
                'category': 'The New Labor Codes Framework (Passed 2019–2020)',
                'name': 'The Code on Social Security, 2020',
                'official_link': 'https://egazette.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/SS_Code_2020.pdf',
                'key_details': 'Amalgamates 9 laws including EPF, ESI, Gratuity, and Maternity Benefit. It formally expands social security coverage to platform workers, unorganized workers, and gig workers.'
            },
            {
                'category': 'The New Labor Codes Framework (Passed 2019–2020)',
                'name': 'The Occupational Safety, Health and Working Conditions Code, 2020',
                'official_link': 'https://egazette.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/OSH_Code_2020.pdf',
                'key_details': 'Consolidates 13 acts (including Factories Act, Mines Act, Plantation Labour, and Contract Labour). It standardizes safety, health, and welfare rules across sectors, creates a single pan-India registration process, and establishes a statutory right to an annual health checkup for workers over a specified age.'
            },

            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Beedi and Cigar Workers (Conditions of Employment) Act, 1966',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15197/1/beedi_and_cigar_workers_%28conditions_of_employment%29_act%2C_1966.pdf',
                'key_details': 'Focuses on health and safety for workers in the tobacco/beedi industry, setting standards for workspaces, ventilation, cleanliness, and maximum working hours to prevent industrial health hazards.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Cine-Workers Welfare Fund Act, 1981',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15234/1/cine-workers_welfare_fund_act%2C_1981.pdf',
                'key_details': 'Finances healthcare, housing, and educational assistance for low-income cinema technicians and artists through a cess levied on cinematograph films.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Dock Workers (Safety, Health and Welfare) Act, 1986',
                'official_link': 'https://shipmin.gov.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15254/1/dock_workers_%28safety%2C_health_and_welfare%29_act%2C_1986.pdf',
                'key_details': 'Outlines strict safety protocols, emergency tracking, and physical safety standards for maritime workers handling heavy machinery and cargo operations across public and private ports.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Motor Transport Workers Act, 1961',
                'official_link': 'https://morth.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15284/1/motor_transport_workers_act%2C_1961.pdf',
                'key_details': 'Outlines requirements for rest rooms, running shift durations, medical equipment access, and daily hours of work for drivers, conductors, and cleaners working in commercial transport undertakings.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Plantation Labour Act, 1951',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15312/1/plantation_labour_act%2C_1951.pdf',
                'key_details': 'Regulates working conditions for laborers on tea, coffee, rubber, and cardamom estates. It mandates that estate owners provide clean drinking water, medical facilities, housing, and educational access for families living on-site.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Working Journalists and Other Newspaper Employees Act, 1955',
                'official_link': 'https://labour.gov.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15367/1/working_journalists_act%2C_1955.pdf',
                'key_details': 'Regulates shift patterns, casual leave provisions, and service conditions for print journalists, and establishes a statutory Wage Board framework to periodically revise salary structures.'
            },
            {
                'category': 'Sector-Specific & Special Welfare Acts',
                'name': 'Mines Act, 1952',
                'official_link': 'https://dgms.gov.in/',
                'pdf_link': 'https://dgms.gov.in/writereaddata/UploadFiles/Mines_Act_1952.pdf',
                'key_details': 'Regulates safety, health, and working standards for laborers in underground and open-cast mining operations. It sets limits on consecutive shifts, mandates structural safety checks, and bans underground employment for minors.'
            },
            {
                'category': 'Skill Development & Social Justice Laws',
                'name': 'Apprentices Act, 1961',
                'official_link': 'https://www.dgt.gov.in/',
                'pdf_link': 'https://www.dgt.gov.in/sites/default/files/ApprenticesAct1961.pdf',
                'key_details': 'Governs formal vocational training programs across industries. It requires designated firms to hire a minimum quota of apprentices, follow an official training curriculum, and pay a state-regulated monthly stipend.'
            },
            {
                'category': 'Skill Development & Social Justice Laws',
                'name': 'Child Labour (Prohibition and Regulation) Act, 1986',
                'official_link': 'https://labour.gov.in/',
                'pdf_link': 'https://labour.gov.in/sites/default/files/ChildLabourAct1986.pdf',
                'key_details': 'Prohibits the employment of children under 14 years of age in all commercial occupations (with narrow exceptions for family businesses without missing school). It also bans adolescents aged 14 to 18 from working in hazardous industries like mining or chemical manufacturing.'
            },
            {
                'category': 'Skill Development & Social Justice Laws',
                'name': 'Bonded Labour System (Abolition) Act, 1976',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15187/1/bonded_labour_system_abolition_act%2C_1976.pdf',
                'key_details': 'Formally abolishes the bonded labor system across India. The law voids all traditional debt-bondage agreements, cancels outstanding financial liabilities tied to forced labor, and criminalizes the practice.'
            },
            {
                'category': 'Industrial Relations & Dispute Resolution',
                'name': 'Industrial Disputes Act, 1947',
                'official_link': 'https://clc.gov.in/',
                'pdf_link': 'https://clc.gov.in/clc/sites/default/files/IndustrialDisputesAct.pdf',
                'key_details': 'Provides the legal framework for resolving industrial conflicts through conciliation, arbitration, or labor courts. It sets strict rules for legal strikes, lockouts, retrenchment processes, and lay-offs.'
            },
            {
                'category': 'Industrial Relations & Dispute Resolution',
                'name': 'Trade Unions Act, 1926',
                'official_link': 'https://www.indiacode.nic.in/',
                'pdf_link': 'https://www.indiacode.nic.in/bitstream/123456789/15332/1/trade_unions_act%2C_1926.pdf',
                'key_details': 'Outlines the legal procedure for registering and running labor unions. It provides registered trade unions with corporate status and grants union executives civil immunity from prosecution for actions taken during legitimate collective bargaining disputes.'
            },
            {
                'category': 'Industrial Relations & Dispute Resolution',
                'name': 'Industrial Employment (Standing Orders) Act, 1946',
                'official_link': 'https://clc.gov.in/',
                'pdf_link': 'https://clc.gov.in/clc/sites/default/files/IndustrialEmploymentStandingOrdersAct.pdf',
                'key_details': 'Requires industrial employers to formally define and post terms of employment, including shift schedules, attendance rules, leave protocols, misconduct classifications, and disciplinary procedures. Applies to industrial establishments with 100 or more workers (reduced to 50 in certain states).'
            }
        ]

        ComplianceLaw.objects.all().delete()

        created_count = 0
        for law in laws_data:
            ComplianceLaw.objects.create(**law)
            created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {created_count} labor laws into the database.'))
