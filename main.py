from pylenium.driver import Pylenium, PyleniumConfig

from jobs import ai, indeed, slack


def create_jobs_lookup(all_jobs) -> dict:
    """To make it easier to find relevant jobs within all jobs, we'll create a lookup table."""
    jobs_lookup = {}
    for job in all_jobs:
        key = f"{job.company} | {job.title}"
        if key not in jobs_lookup:
            jobs_lookup[key] = job
    return jobs_lookup


def main():
    # 1. Use Pylenium to scrape jobs from Indeed
    py = Pylenium(PyleniumConfig())
    scraped_jobs = indeed.scrape(py, indeed.REMOTE_QA_ENGINEER)

    # 2. Use AI to filter out irrelevant jobs
    relevant_jobs = ai.get_relevant_jobs(scraped_jobs)
    ai_ranked_jobs = ai.convert_relevant_jobs_to_list(relevant_jobs)

    # 3. Use lookup to match relevant jobs with scraped jobs
    lookup = create_jobs_lookup(scraped_jobs)
    jobs = [job for j in ai_ranked_jobs if (job := lookup.get(f"{j['company']} | {j['title']}"))]

    # 4. Post jobs to Slack
    slack.post_jobs_to_channel(jobs)


if __name__ == "__main__":
    main()
