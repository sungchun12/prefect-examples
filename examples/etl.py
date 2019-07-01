#%%
from prefect import Flow, task
from prefect.schedules import CronSchedule


@task
def extract():
    return [1, 2, 3, 50]


@task
def transform(x):
    return [i * 10 for i in x]


@task
def load(y):
    print("Received y: {}".format(y))


with Flow("ETL") as flow:
    e = extract()
    t = transform(e)
    l = load(t)
    schedule = CronSchedule("0 0 * * *")  # setup a cron scheduler

flow_state = flow.run()  # set the flow run to an object to track state

flow.visualize(flow_state=flow_state)  # visualize how the data moves throughout the DAG

#%%
