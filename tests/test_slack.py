import pytest

from jobs import slack
from jobs.models import Job


JOBS = [
    Job(
        origin="https://indeed.com",
        title="Lead Software Engineer",
        company="Acumen LLC",
        location="Remote",
        description="Mentor less seniorengineersas needed. 7+ years of experience withsoftwaredevelopment technologies such as .",
        salary="Full-time",
        job_type="Full-time",
        apply_link="https://indeed.com/pagead/clk?mo=r&ad=-6NYlbfkN0DGW7oAII_n1CsFCfxPS3lfOvXVR0Xn2qfvMFNixl8toU8QpiZrjlELMH3WZ32QtQ8S6UZWecxt3A_WOvo4bTMKeyBLVpNs2Tdo3HrAx0hG6wul69mjCvt8-JYZD-bsfpltWVE8wd0l_FTeOTkoVFVQpkWT8mT6QsAfd9r0uGfzSyhptvM5tn7qekKLrk1hjIwDJKpwSr_CXhFSP7ChqV5JpOwlVV2OjJKkLp1lrzUWWoKeCAJqTdjacyN_sqGPAIZj05d1eQ3E8xO2QajXMX9OwLzCDjSGVG0rca497t9Cv6dxwpk9T9LhJdZJZAT0Cb6K0k4x49EIfxzumWoLm9_xOvLX7I3JpXS3l-Wxqw3q3fOImB9-MyzQy2v2QnI4cHKYBrHNXDDDXvAmbThBgx5kvth_xJ2r2mmYHUqxuSBdxKp6Y7dDAIfp3Si_RJSnkUi8bXg4xKkLojzC5kSDFzUkNdL6Gmp51zhW27cI4qMBqoajdTcgOSivZrBMfEkNmkazGLA_V_mE0Hgra2RlP7RYP_i91llwL47MxkcGTFIWhCPRzu681HOCBByrf1oFAyN4097aFK9qQ6uexbTaCI954F4WHlgVrhp7RXNvtFDXW9wqSDWn98M05pxDclx6gMDoCX7tnWwl4g==&xkcb=SoDN6_M3Go7b1mQlUh0LbzkdCdPP&p=0&fvj=1&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Software Engineer, Backend",
        company="Pinterest",
        location="Remote in San Francisco, CA",
        description="Experience in following best practices in writing reliable and maintainable code that may be used by many other engineers.",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=4a60afeecb5cf9db&bb=TlGHW-6xtWwm528EbjlB67oPjy_KPGjAJPHOX2ggGdYl9_FQ48_mN-ixfb1qGRzG&xkcb=SoB667M3Go7by3RvdJ0LbzkdCdPP&fccid=43014b1412e0a7b6&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="QA Engineer, Manual Tester",
        company="i2e Consulting",
        location="Remote",
        description="Proficient in MS Office software. Previous experience as aQAengineer. Meeting with thesoftwaredesigners and developers to determine quality assurance…",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=dc5d4e3e01feae81&bb=TlGHW-6xtWzbPR-41cr_tEAA0cK62KeyGMNR0pCxXikeiBcQny4Bp5Z8JgMUTGht&xkcb=SoBT67M3Go7by3RvdJ0JbzkdCdPP&fccid=1939f023cebd51e0&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Software Engineer, Customer Experience Engineering",
        company="Whatnot",
        location="Remote in Los Angeles, CA",
        description="Collaborate cross-functionally with other product engineering teams across multiplesoftwareprojects, apps, data systems and more.",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=66beba3a2b9953b9&bb=TlGHW-6xtWzTyuyPmAV1tO1eDoSSlaTr_38yeAFYXqIfQIb-iwwSq4BHg2kWbxVA&xkcb=SoBp67M3Go7by3RvdJ0PbzkdCdPP&fccid=bc4b3271ce7474f2&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Software Developer / Engineer",
        company="McKesson",
        location="Remote in Columbus, OH 43222",
        description="Proficient in development SQL database software. Our Tech Stack Ruby on Rails, React, PostgreSQL, Git, Redis, Sidekiq, Docker, RSpec.",
        salary="$99,500 - $165,800 a year",
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=1a1ca261017f27cd&bb=5l7d5FXMOla6wSth_pLFF20JQTg2JKXutTexrsn4FVNE2t1YBzPHpqlLvwewcjJA&xkcb=SoCL67M3Go7by3xvdJ0KbzkdCdPP&fccid=a7c5036618407010&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Junior Manual tester",
        company="Technimates LLC",
        location="Remote",
        description="Follow the appropriate testing strategy for each case. Create test plans and test condition. Explore features as they are being developed to identify design,…",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=2c62c5adfda46dec&bb=5l7d5FXMOlbVOo-x73zOZDL5i4VEVHnxWCdkiunqP_RYGG83DpUgmqQzOQGIXRoy&xkcb=SoCi67M3Go7by3xvdJ0IbzkdCdPP&fccid=414765fdd597aec4&cmp=Technimates-LLC&ti=Junior+Tester&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Mobile Engineer",
        company="Empower",
        location="Remote in Colorado",
        description="Troubleshoot and resolve complexsoftwareissues. 3+ years of experience insoftwaredevelopment. Collaborate with cross-functional teams to gather and refine…",
        salary="$84,000 - $118,575 a year",
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=450cd2b842f10ab5&bb=RrfPGDWQtabRmBI7FN4YAgqCZgKDkENDBHJDrYDRWRsg4LwL6pcq6vCe88SYnpNu&xkcb=SoAF67M3Go7by2RvdJ0KbzkdCdPP&fccid=796b5a2c2fc5984d&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Jr. QA Software Tester",
        company="Syntricate Technologies",
        location="Remote",
        description="Working with development colleagues to provide direct solutions, constructive feedback and input on thesoftwareto ensure it meets customer expectations.",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=dc9baba767b91afd&bb=P3Zc_vvO8VzyIAiPu1aJ6CHvU5E8Ii0XTUtKxSWzLbGeUX5bkamR8tI_KBV6Gt50&xkcb=SoD067M3Go7by2xvdJ0LbzkdCdPP&fccid=6a8862eed7fda9a3&cmp=Syntricate-Technologies&ti=Junior+Quality+Assurance+Tester&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="QA Tester",
        company="Bad Robot Games",
        location="Remote",
        description="Experience with Jira or equivalent bug trackingsoftware(DevTrack, etc.). Bad Robot Games is seeking a tester to execute test cases and scenarios with…",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=4f4c457be06e6c19&bb=P3Zc_vvO8VwyNWrH2Igaw-cF09d4N8rrAEfZLPEc9Ik1IdEYqII_TTM0NFY2wG1T&xkcb=SoDd67M3Go7by2xvdJ0JbzkdCdPP&fccid=3bbdf463d226a762&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Junior Software Tester",
        company="N-Tierty Inc.",
        location="Remote in Virginia",
        description="2+ years ofsoftwaredevelopment life cycle and testing experience. Test existing applications for compliance with upgrades and ensure new applications and…",
        salary="$50,000 - $60,000 a year",
        job_type="Full-time",
        apply_link="https://indeed.com/rc/clk?jk=8b9717b0785e10c6&bb=jm9pwHs0hXp0D0aPGLjiswqGt-WinrTK3jhiTxCndI0WNExkgMDa-GVy4vXaOMnr&xkcb=SoBC67M3Go7byxRvdJ0LbzkdCdPP&fccid=858b725a182d9d2b&cmp=N--Tierty-Inc.&ti=Junior+Software+Test+Engineer&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Junior Front End Engineer",
        company="minware",
        location="Remote",
        description="This helps organizations make better decisions with stronger alignment betweenengineersand executives. Minware provides engineering business metrics that show…",
        salary="$80,000 - $120,000 a year",
        job_type="Flextime",
        apply_link="https://indeed.com/rc/clk?jk=5dcb9ffc0e943e0b&bb=jm9pwHs0hXqNN_3re-KuIhVHaF2Qjn1MV2ZfZ8Vn56rksJ3LjCCAJ7YuSap9tAzk&xkcb=SoBr67M3Go7byxRvdJ0JbzkdCdPP&fccid=01b27327b9e5d576&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="QA Analyst/Tester- Entry Level",
        company="Syntricate Technologies",
        location="Remote",
        description="Executes the scoping, planning, and scheduling of testing activities. Develops and documents manual test scripts to effectively test new and existing…",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=cc65bf249be5a728&bb=WIQdW8K0J70EPCsh_I_sGPpFVcEKDIg2XPbz1lJ2hrTvYsgdoagLDOnYu6MQpW1w&xkcb=SoCz67M3Go7byxxvdJ0KbzkdCdPP&fccid=6a8862eed7fda9a3&cmp=Syntricate-Technologies&ti=Quality+Assurance+Tester&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Java Engineer",
        company="Oddball",
        location="Remote",
        description="May assistsoftwaredevelopers by analyzing user needs and designingsoftwaresolutions. Collaborate with stakeholders to analyze and designsoftwaresolutions.",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=754045953ba2a3ea&bb=WIQdW8K0J711X5IZvHojuICJEmmQVq99IvoOO5ONmnMiQeV-WSNfiHdu_o68caHr&xkcb=SoCa67M3Go7byxxvdJ0IbzkdCdPP&fccid=3e46386dfe396c15&cmp=Oddball&ti=Java+Developer&vjs=3",
    ),
    Job(
        origin="https://indeed.com",
        title="Software Engineer II - MPS Team",
        company="HealthTrio LLC",
        location="Remote in United States",
        description="Able to mentor or guide less experienced engineers. Receives guidance and coaching as needed from more senior engineers. Experience with Git and Maven.",
        salary=None,
        job_type=None,
        apply_link="https://indeed.com/rc/clk?jk=5cefb193ea089870&bb=1NhwKwcZ27dkwS-VpheaYTAJC5spJbx6YyPWdDRJmIuOAfE_WWx_PAQK3DNNNmAr&xkcb=SoAu67M3Go7bywRvdJ0ObzkdCdPP&fccid=ed61d40cc5e5cb35&vjs=3",
    ),
]


def test_create_job_block():
    job = JOBS[0]
    block = slack.create_job_block(job)

    text = block["text"]["text"]
    assert job.title in text
    assert job.company in text
    assert job.location in text
    assert job.salary in text

    assert block["type"] == "section"


def test_create_jobs_payload():
    payload = slack.create_jobs_payload(JOBS)
    assert len(payload["blocks"]) == 31


@pytest.mark.skipif(slack.config.SLACK_WEBHOOK_URL.endswith("cL4oP"), reason="Don't test with public channel")
def test_slack_post_to_channel():
    response = slack.post_to_channel("Hello, World!")
    assert response.ok


@pytest.mark.skipif(slack.config.SLACK_WEBHOOK_URL.endswith("cL4oP"), reason="Don't test with public channel")
def test_slack_post_to_jobs_with_blocks():
    response = slack.post_jobs_to_channel(JOBS)
    assert response.ok
