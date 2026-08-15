"""Research-informed synthetic inputs based on FAO crop-factor tables."""
SOURCE = "FAO Crop water needs: https://www.fao.org/4/s2022e/s2022e07.htm"
SOIL = {"sandy": {"trigger": 60, "retention": .85}, "loamy": {"trigger": 52, "retention": 1.0}, "clay": {"trigger": 45, "retention": 1.15}}
CROPS = {
 "tomato": {"stages": [("initial",.45),("development",.75),("mid_season",1.15),("late",.80)], "temp":(18,36), "humidity":(35,85)},
 "potato": {"stages": [("initial",.45),("development",.75),("mid_season",1.15),("late",.85)], "temp":(12,30), "humidity":(40,90)},
 "cucumber": {"stages": [("initial",.45),("development",.70),("mid_season",.90),("late",.75)], "temp":(18,38), "humidity":(40,90)},
 "pepper": {"stages": [("initial",.35),("development",.70),("mid_season",1.05),("late",.90)], "temp":(18,36), "humidity":(35,85)},
 "onion": {"stages": [("initial",.50),("development",.75),("mid_season",1.05),("late",.85)], "temp":(12,34), "humidity":(30,85)},
}
FEATURES = ["soil_moisture_pct", "temperature_c", "humidity_pct", "flow_rate_lpm", "growth_stage", "soil_type", "recent_irrigation_l"]
