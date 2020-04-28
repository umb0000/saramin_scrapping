from saram import get_jobs
from save import save_to_file

jobs = get_jobs()

save_to_file(jobs)
print('hi')