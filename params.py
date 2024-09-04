WANDB_ENTITY = "keisuke-kamata" # set this to team name if working in a team
WANDB_PROJECT = "mlops-course-001"
BDD_CLASSES = {i:c for i,c in enumerate(['background', 'road', 'traffic light', 'traffic sign', 'person', 'vehicle', 'bicycle'])}
RAW_DATA_AT = 'bdd_simple_1k'
PROCESSED_DATA_AT = 'bdd_simple_1k_split'