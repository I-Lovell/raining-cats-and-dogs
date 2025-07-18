DROP TABLE IF EXISTS cat_icons;
DROP SEQUENCE IF EXISTS cat_icons_id_seq;

CREATE SEQUENCE IF NOT EXISTS cat_icons_id_seq;
CREATE TABLE cat_icons (
    id SERIAL PRIMARY KEY,
    code INT,
    weather_type VARCHAR(225),
    icon_path VARCHAR(225),
    alt_text VARCHAR(225)
);

INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (0, 'Clear Sky', '/static/images/0_clearsky.png', 'A happy cat representing the sun');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (1, 'Mainly Clear', '/static/images/1_mainlyclear.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (2, 'Partly Cloudy', '/static/images/2_partlycloudy.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (3, 'Overcast', '/static/images/3_overcast.png', 'A chubby grey cat representing a cloud');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (45, 'Fog', '/static/images/45_fog.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (48, 'Depositing Rime Fog', '/static/images/48_rimefog.png', 'A chubby grey cat representing a cloud');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (51, 'Light Drizzle', '/static/images/drizzle.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (53, 'Moderate Drizzle', '/static/images/drizzle.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (55, 'Dense Drizzle', '/static/images/drizzle.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (56, 'Light Freezing Drizzle', '/static/images/freezingdrizzle.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (57, 'Dense Freezing Drizzle', '/static/images/freezingdrizzle.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (61, 'Light Rain', '/static/images/61_lightrain.png', 'A grumpy grey cat representing a rain cloud with one rain drop');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (63, 'Moderate Rain', '/static/images/63_moderaterain.png', 'A grumpy grey cat representing a rain cloud with two rain drops');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (65, 'Heavy Rain', '/static/images/65_heavyrain.png', 'A grumpy grey cat representing a rain cloud with three rain drops');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (66, 'Light Freezing Rain', '/static/images/66_lightfreezingrain.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (67, 'Heavy Freezing Rain', '/static/images/65_heavyfreezingrain.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (71, 'Light Snow', '/static/images/71_lightsnow.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (73, 'Moderate Snow', '/static/images/73_moderatesnow.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (75, 'Heavy Snow', '/static/images/75_heavysnow.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (77, 'Snow Grains', '/static/images/77_snowgrains.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (80, 'Light Rain Showers', '/static/images/80_lightrainshowers.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (81, 'Moderate Rain Showers', '/static/images/81_moderaterainshowers.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (82, 'Violent Rain Showers', '/static/images/82_violentrainshowers.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (85, 'Slight Snow Showers', '/static/images/85_slightsnowshowers.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (86, 'Heavy Snow Showers', '/static/images/86_heavysnowshowers.png', ' ');
INSERT INTO cat_icons (code, weather_type, icon_path, alt_text) VALUES (95, 'Thunderstorm', '/static/images/95_thunderstorm.png', ' ');


