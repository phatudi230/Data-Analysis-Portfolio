import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration
STATIONS = ['Station_A', 'Station_B', 'Station_C', 'Station_D']
SHIFTS = ['Day', 'Night']

NUM_ORDERS = 2000  # Enough for meaningful analysis

# Station profiles - C is the bottleneck
STATION_CONFIG = {
    'Station_A': {
        'Day':   {'avg_time': 12, 'std': 2, 'defect_rate': 0.08},
        'Night': {'avg_time': 14, 'std': 3, 'defect_rate': 0.12},
    },
    'Station_B': {
        'Day':   {'avg_time': 11, 'std': 2, 'defect_rate': 0.07},
        'Night': {'avg_time': 12, 'std': 2, 'defect_rate': 0.09},
    },
    'Station_C': {  # Bottleneck of Death at Night
        'Day':   {'avg_time': 16, 'std': 3, 'defect_rate': 0.20},
        'Night': {'avg_time': 24, 'std': 6, 'defect_rate': 0.42},
    },
    'Station_D': {
        'Day':   {'avg_time': 13, 'std': 3, 'defect_rate': 0.10},
        'Night': {'avg_time': 16, 'std': 4, 'defect_rate': 0.18},
    },
}

records = []
base_time = datetime(2026, 4, 1, 6, 0)

for i in range(NUM_ORDERS):
    station = random.choice(STATIONS)
    shift = random.choice(SHIFTS)
    config = STATION_CONFIG[station][shift] 
    
    
    
    process_time = max(5, np.random.normal(
        config['avg_time'],
        config['std']
    ))
    
    labor_cost = round(random.uniform(25, 50), 2)
    defect_flag = 1 if random.random() < config['defect_rate'] else 0
    rework_time = process_time * 0.4 if defect_flag == 1 else 0
    total_time = process_time + rework_time
    
    if defect_flag == 1:
        status = 'Failed'
    elif total_time > 15:
        status = 'Delayed'
    else:
        status = 'Success'
    
    timestamp_start = base_time + timedelta(minutes=i*2)
    timestamp_end = timestamp_start + timedelta(minutes=total_time)
    
    records.append({
        'order_id': f'ORD-{1000+i}',
        'timestamp_start': timestamp_start,
        'timestamp_end': timestamp_end,
        'station_id': station,
        'shift': shift,
        'process_time_mins': round(process_time, 2),
        'rework_time_mins': round(rework_time, 2),
        'total_time_mins': round(total_time, 2),
        'labor_cost_per_hour': labor_cost,
        'defect_flag': defect_flag,
        'status': status,
        'rework_cost': round((rework_time/60) * labor_cost, 2) if defect_flag == 1 else 0,
        'delay_cost': round(((total_time-15)/60) * labor_cost, 2) if status == 'Delayed' else 0
    })

df = pd.DataFrame(records)
df.to_csv('globallink_operations.csv', index=False)
print(f"Generated {len(df)} orders")
print(df['status'].value_counts())
print(f"\nTotal Rework Cost: R{df['rework_cost'].sum():,.2f}")
print(f"Total Delay Cost: R{df['delay_cost'].sum():,.2f}")