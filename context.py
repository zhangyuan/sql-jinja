class SystemContext():
  def job_id(self):
    return "1234"


class JobXContext(SystemContext):
  def __init__(self):
    self.indicator = 1
