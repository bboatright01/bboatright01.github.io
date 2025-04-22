DROP DATABASE IF EXISTS `c4c`;
CREATE DATABASE `c4c`;
USE `c4c`;

        CREATE TABLE Donors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(32),
            Description TEXT,
            Country VARCHAR(32),
            Email VARCHAR(64),
            username VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(256) NOT NULL
        );
        

        CREATE TABLE NGOs (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(128),
            Description TEXT,
            username VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(256) NOT NULL,
            Email VARCHAR(64),
            Address VARCHAR(256)
        );
        

        CREATE TABLE Campaigns (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(128),
            Description TEXT,
            Country VARCHAR(32),
            NGO_ID INT NOT NULL,
            Funding_Goal DECIMAL(15,2),
            FOREIGN KEY (NGO_ID) REFERENCES NGOs(id)
        );
        

        CREATE TABLE Donations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            DONOR_ID INT NOT NULL,
            CAMPAIGN_ID INT NOT NULL,
            Amount DECIMAL(15,2) NOT NULL,
            timestamp DATETIME,
            FOREIGN KEY (DONOR_ID) REFERENCES Donors(id),
            FOREIGN KEY (CAMPAIGN_ID) REFERENCES Campaigns(id)
        );
        

        CREATE TABLE Subscriptions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            DONOR_ID INT NOT NULL,
            CAMPAIGN_ID INT NOT NULL,
            FOREIGN KEY (DONOR_ID) REFERENCES Donors(id),
            FOREIGN KEY (CAMPAIGN_ID) REFERENCES Campaigns(id)
        );
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Sarah Thompson', 'Im a sustainability consultant from California passionate about making a global impact. I firmly believe that access to clean water and sustainable agriculture is a fundamental right. I donate to projects like ''Clean Water for Oromia'' and ''Andean Harvest Boost'' because I see them as seeds of change in communities that need them most. When not working or donating, I enjoy hiking and volunteering locally to support environmental causes.', 'USA',
                'sarah.thompson@email.com', 'donor1', 'pbkdf2:sha256:1000000$0OP23BeR$a4b7070da2b3bda7c8ac59fe9e02cbe3452265b4e68b905cad49368b0eed3665');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Jacques Dubois', 'Bonjour, Im Jacques, a software engineer based in Paris with a keen interest in educational equality around the world. My background in technology has shown me firsthand how digital literacy can change lives. I regularly support initiatives like ''Bangladesh Literacy Lift'' and ''Nepal Digital Bridge'' to help bridge the digital divide. Im here to connect with other global citizens who believe in empowering communities through education.', 'France',
                'jacques.dubois@email.com', 'donor2', 'pbkdf2:sha256:1000000$OhAEfTBG$c4c558801cc82294d7d2c93b4fb6041bcc2e2dcdffc523fc888f11fd371564ac');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Emily Rodriguez', 'Hello, Im Emily from London. As a social entrepreneur, Im dedicated to using my resources to empower those in need. I am particularly passionate about healthcare and clean water initiatives. Projects like ''Accra Bed Net Brigade'' and ''Lamu LifeStream Project'' have captured my heart. Im excited to join this community, share insights about social impact, and support transformative projects around the globe.', 'UK',
                'emily.rodriguez@email.com', 'donor3', 'pbkdf2:sha256:1000000$3G2AKqWL$592509f27d46f69646c620212a665ceeabc18bcb18ca287bbf3db33eec9103bf');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Anil Kapoor', 'Im Anil, a marketing strategist living in Toronto with roots that stretch around the world. My passion is philanthropy, especially when it comes to building community infrastructure and improving living conditions. I''m a proud supporter of projects like ''Clinic Care of Bahia'' and ''Bangladesh Resilient Roofs''. I believe that every small contribution can lead to large changes, and I''m here to contribute and learn from fellow donors.', 'Canada',
                'anil.kapoor@email.com', 'donor4', 'pbkdf2:sha256:1000000$f51kvVfE$7349a5facf670aac52cc6825cc8b1c55b56c65864017b8a10f8e95c9584157b1');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Maria Silva', 'Olá! Im Maria from Lisbon. With a background in international development, Ive always been drawn to initiatives that ensure basic human rights are met, from clean water to quality education. I''ve supported campaigns like ''Viviendo Saludable'' and ''Sabor de la Tierra'' because I truly believe in grassroots change. When Im not working, I love exploring different cultures and building connections with people who share my vision for a better world.', 'Portugal',
                'maria.silva@email.com', 'donor5', 'pbkdf2:sha256:1000000$DpeVaajP$bab46a988145b06346661c3cc450eb807c9fcbce71886ac3790032d36bd81e24');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Oliver Müller', 'Hallo! Im Oliver, an environmental economist from Berlin. My career has taught me the critical balance between economic growth and sustainable development. I actively support projects that promote clean water access, renewable energy, and sustainable agriculture. Campaigns like ''Rift Valley Refresh'' and ''Tanzanian Green Harvest'' inspire me to contribute and advocate for long-term change in vulnerable communities.', 'Germany',
                'oliver.mueller@email.com', 'donor6', 'pbkdf2:sha256:1000000$rAuffGRM$979269bb8f6c3a9fc184d09acc659404f15e3216fd3eb537f9340a8ee9ddfdb3');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Chloe Martin', 'G''day! Im Chloe, a freelance graphic designer based in Sydney with a deep commitment to social justice and global health. Im particularly drawn to initiatives that tackle public health challenges, such as vector-borne disease prevention and emergency healthcare. Projects like ''Kisumu Night Shield'' and ''Salud y Esperanza'' reflect my belief that every community deserves access to life-saving resources, and they motivate me to give what I can.', 'Australia',
                'chloe.martin@email.com', 'donor7', 'pbkdf2:sha256:1000000$kBctRsmX$10753cb40173ea445bbc21efc1ef3064a5ce01aae61b398bc86a9ce500f50e41');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Liam OConnor', 'Hi, Im Liam from Dublin. As a teacher, Im passionate about the power of education to uplift communities and transform lives. I regularly support educational campaigns such as ''India Future Pathways'' and ''Cambodian Classroom Revival''. For me, every donation is a chance to contribute to a future where learning is accessible to all, regardless of geography. Im proud to be part of a community that prioritizes global progress and inclusion.', 'Ireland',
                'liam.oconnor@email.com', 'donor8', 'pbkdf2:sha256:1000000$TLCOYGav$95e57eaf2ab42944e11f37430f94db39e27cd16b3b6c6acd54e2d736d43fc1dc');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Isabella Rossi', 'Ciao! Im Isabella, an artisan and small business owner from Milan who loves blending creativity with philanthropy. I enjoy supporting diverse causes, especially those aimed at empowering underserved communities in education, healthcare, and sustainable living. Projects like ''Nepal Digital Bridge'' and ''Clinic Care of Bahia'' resonate with me because they pave the way for brighter futures. Im excited to connect with other supporters and share stories of impact along the way.', 'Italy',
                'isabella.rossi@email.com', 'donor9', 'pbkdf2:sha256:1000000$iWWpSheW$1066a5f5c0c04a17a2296d2f0e849a5f56bdd7faa09241a752010576954bac61');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Benjamin Smith', 'Hello, Im Benjamin, a financial analyst from New York with a keen interest in international development. I believe that with strategic investments and community-focused interventions, we can tackle even the world''s biggest challenges. Ive contributed to initiatives such as ''Accra Bed Net Brigade'' and ''Nuevo Amanecer Health Centers'', and I continue to search for projects that effectively combine innovative solutions with a humanitarian focus. I look forward to being part of this global journey.', 'USA',
                'benjamin.smith@email.com', 'donor10', 'pbkdf2:sha256:1000000$jd7pZM9F$a8c0853d03901389d994c9b3080c041ad2e5047cd658400561343960cca2fb9d');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Mei-Ling Chen', 'Hello, Im Mei-Ling from Singapore. As an urban planner with a passion for sustainable community development, I actively seek out projects that not only address immediate needs but also lay the foundation for long-term change. I support initiatives that enhance access to quality education, healthcare, and clean water in emerging communities. Campaigns like ''Cambodian Classroom Revival'' and ''Clinic Care of Bahia'' inspire me to contribute because I believe that innovative design and infrastructure can truly transform lives.', 'Singapore',
                'mei-ling.chen@email.com', 'donor11', 'pbkdf2:sha256:1000000$Bs4OLeKL$51d55c3e3cd6c9ee7873b3598d77aa0625c1740600fd89437bd34cca862b42bb');
        

        INSERT INTO Donors (Name, Description, Country, Email, username, password)
        VALUES ('Tane Williams', 'Kia ora, Im Tane, a community organizer based in Wellington, New Zealand. My work in rural development has shown me how important it is to support sustainable projects that empower local voices and preserve unique cultures. Im particularly drawn to health and environmental initiatives, such as ''Kisumu Night Shield'' and ''Mozambique Organic Rise'', which are making a real difference in vulnerable regions. Im excited to join this platform to connect with like-minded individuals who are dedicated to creating global change through grassroots action.', 'New Zealand',
                'tane.williams@email.com', 'donor12', 'pbkdf2:sha256:1000000$IYMBoi0n$419c681c49283c5b7718cf475452e3845b56a0d08f95e607e3cda249084e2cc6');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('WaterWorks International', 'WaterWorks International is dedicated to combating the water crisis in Sub-Saharan Africa by delivering sustainable clean water solutions. Operating in rural communities across East and West Africa, this organization builds wells, installs advanced water-filtration systems, and conducts comprehensive hygiene and health education campaigns. By empowering local communities with the knowledge and infrastructure to maintain safe water sources, WaterWorks International actively reduces waterborne illnesses and fosters long-term community resilience.', 'ngo1',
                'pbkdf2:sha256:1000000$qTgF34yB$45d6abe89f99dc9fe89adc5255929b33a35e9ef07a36bff7c38c63f0973a98b3', 'contact@waterworksafrica.org', '123 Aqua Lane, Nairobi, Kenya, 00100');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('Food For All', 'Food For All is devoted to addressing chronic hunger and food insecurity throughout Latin America. The organization engages local communities in regions such as Central America and the Andes by developing sustainable community gardens, organizing food distribution drives, and supporting small-scale farmers with modern agricultural techniques and resources. Through hands-on community engagement and capacity building, Food For All not only meets immediate nutritional needs but also lays the groundwork for lasting economic development in the region.', 'ngo2',
                'pbkdf2:sha256:1000000$4YJ1B221$051d2da81cc99b6f713b8b42130b6a075d558657dd52eb1acbb056e0f6d5ed70', 'info@foodforalllatam.org', '456 Harvest Road, Buenos Aires, Argentina, C1000');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('Hope Builders', 'Hope Builders focuses its efforts on uplifting impoverished communities in less-developed parts of Asia. By operating in rural areas across South and Southeast Asia, the organization delivers essential housing solutions by constructing safe, affordable homes using locally sourced sustainable materials. In addition, Hope Builders provides critical services like access to clean water and sanitation, alongside community empowerment workshops that include vocational training and health education initiatives. Their mission is to create self-reliance and stimulate socio-economic growth at the grassroots level.', 'ngo3',
                'pbkdf2:sha256:1000000$P4ipgfGq$8e20f4d182bf5a8097ef986f7746bcd6db566e7a5a7c80d3de2aca24bdfc8fe2', 'contact@hopebuildersasia.org', '789 Hope Street, Manila, Philippines, 1000');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('Green Seeds Initiative', 'Green Seeds Initiative is dedicated to improving food security and promoting environmental sustainability in African rural communities. Focused on Sub-Saharan Africa, the NGO works directly with local farmers by providing training in modern, eco-friendly agricultural practices, supplying state-of-the-art agro-equipment, and supporting organic farming methods. Their efforts increase crop yields, bolster food availability, and nurture environmental stewardship, paving the way towards sustainable community development.', 'ngo4',
                'pbkdf2:sha256:1000000$ke5Xa8tq$1527a81aad3864fd57790df596768d51feaf8572ff85452245a1ea71a3185850', 'support@greenseedsafrica.org', '321 Greenway Drive, Accra, Ghana, 00233');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('Education Empowerment', 'Education Empowerment is committed to bridging the educational gap in remote and disadvantaged areas of Asia. The organization focuses on regions where access to quality education is scarce by building and renovating schools, offering scholarships, and implementing digital literacy programs that introduce innovative learning methodologies and technology. By empowering both children and adults through education and skills training, Education Empowerment is building a knowledgeable, skilled community capable of driving long-term local progress.', 'ngo5',
                'pbkdf2:sha256:1000000$y4lq6TDI$d3865689cd0fd5cacdd57414168122f7817c93769421e0b0a16647d097841521', 'info@educationempowermentasia.org', '654 Learning Lane, New Delhi, India, 110001');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('Health Horizons Clinics', 'Health Horizons Clinics aims to significantly improve healthcare access in rural Latin American communities by constructing modular clinics and offering high-quality medical services. Targeting regions with a high prevalence of preventable diseases, the organization focuses on setting up well-equipped local health centers, training community medical workers, and implementing vaccination drives. Their hands-on approach ensures that remote communities receive prompt medical attention and ongoing health education, leading to measurable improvements in public health outcomes.', 'ngo6',
                'pbkdf2:sha256:1000000$bC5xAzLe$96560c9d69a40862213f57efad03ec55df5df8cb850f57917e97767295102dc8', 'contact@healthhorizonslatam.org', '987 Wellness Avenue, São Paulo, Brazil, 01000-000');
        

        INSERT INTO NGOs (Name, Description, username, password, Email, Address)
        VALUES ('SafeSleep Initiative', 'SafeSleep Initiative is focused on reducing disease transmission and improving community health by distributing insecticide-treated bed nets in Africa. Operating primarily in tropical zones of Sub-Saharan Africa where vector-borne illnesses like malaria and dengue pose significant threats, this organization partners with local authorities and communities to distribute bed nets, conduct awareness campaigns on their proper use, and establish preventive health workshops. By providing these essential resources and education, SafeSleep Initiative helps mitigate the impact of vector-borne diseases and enhances overall community well-being.', 'ngo7',
                'pbkdf2:sha256:1000000$BL0e0nSk$9ac6e48b44845f31151e7862d24af6c7d7712d126c2543bd07ba9a8fe7cef1e0', 'info@safesleepafrica.org', '135 Safety Boulevard, Nairobi, Kenya, 00101');
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Clean Water for Oromia', 'This campaign is dedicated to installing sustainable water filtration systems and building new wells in rural areas of Ethiopias Oromia region. The project aims to improve access to clean water for multiple villages, reducing waterborne illnesses and providing a reliable supply for community use. Funds will be used for purchasing filtration equipment, drilling wells, and community health and hygiene training initiatives.', 'Ethiopia',
                1, 50000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Lamu LifeStream Project', 'Focused on Kenyas coastal Lamu County, this campaign targets drought-prone communities that are in need of reliable water sources. The project will establish solar-powered water pump systems and modernize existing water infrastructure. By providing consistent clean water access, the Lamu LifeStream Project hopes to boost community health and foster economic development in the region.', 'Kenya',
                1, 40000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Machinga Wells Initiative', 'In Malawis Machinga District, where communities struggle with scattered water points and erratic supply, this campaign aims to construct new boreholes and establish localized water filtration units. The goal is to reduce the dependency on unsafe water sources and empower the locals with practical training on maintenance and water conservation methods.', 'Malawi',
                1, 35000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Kwale Water Connect', 'Serving Kenyas Kwale County, this initiative seeks to connect isolated villages with sustainable, clean water through the installation of gravity-fed water systems and community-managed wells. The campaign intends to address the acute water scarcity challenges in the region, enabling improved health standards and resilience against drought conditions.', 'Kenya',
                1, 45000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Rift Valley Refresh', 'Targeting Kenyas Rift Valley Province, this campaign will deploy a comprehensive clean water strategy that involves building deep wells and establishing filtration points in multiple rural communities. The goal is to tackle water scarcity faced by farming communities while also incorporating sustainable practices to ensure long-term water security.', 'Kenya',
                1, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Andean Harvest Boost', 'This campaign is focused on the highland communities in the Cusco region of Peru. Food For All aims to provide training in sustainable farming techniques and supply quality seeds and agro-equipment to local small-scale farmers. The project is designed to enhance crop resilience against harsh mountain climates and boost food production during off-seasons, thereby reducing hunger and stimulating economic growth in these Andean communities.', 'Peru',
                2, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Amazon Fresh Initiative', 'Targeting remote communities along the Amazon River in Brazil, this initiative aims to introduce community gardens, improve local food distribution channels, and offer agricultural training tailored to tropical climates. By empowering local farmers with improved resources and knowledge, the campaign will help secure an abundant and nutritious food supply, while preserving traditional cultivation methods in the region.', 'Brazil',
                2, 65000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Sabor de la Tierra', 'Located in the rural outskirts of Honduras Olancho region, this campaign strives to revitalize smallholder farming in an area deeply affected by food scarcity and economic challenges. Food For All will implement modern irrigation systems, provide organic fertilizer, and conduct workshops on crop rotation and sustainable agriculture, ultimately aiming to improve both nutrition and local livelihoods.', 'Honduras',
                2, 45000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Caribbean Bounty Project', 'This campaign targets the agricultural communities in rural areas of the Dominican Republic. Food For All plans to establish community-supported agriculture (CSA) programs that connect local farmers directly with consumers. The funds will be used to set up local markets, enhance storage facilities for perishable produce, and offer educational programs aimed at improving farming practices in the Caribbean climate.', 'Dominican Republic',
                2, 50000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Patagonian Prosperity Plan', 'Focused on the rural regions of southern Chile near Patagonia, this campaign seeks to address seasonal food shortages by developing sustainable greenhouse projects and modernizing traditional farming infrastructure. Food For All will provide training on controlled-environment agriculture techniques, enabling communities to produce nutritious food year-round despite challenging environmental conditions.', 'Chile',
                2, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Rural Homes for Rajasthan', 'Focused on remote villages in Rajasthan, India, this campaign aims to construct safe, affordable homes using locally sourced, sustainable materials. Hope Builders will work directly with community members to design homes tailored to the local climate, while also integrating basic amenities such as clean water access and sanitation facilities. The initiative will empower residents through hands-on vocational training, making it a long-term solution to improve living conditions in these rural communities.', 'India',
                3, 70000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Kathmandu Shelter Initiative', 'Centered in the hilly outskirts of Nepals Kathmandu Valley, this campaign strives to rebuild and upgrade housing structures that were impacted by natural disasters. Hope Builders will focus on constructing resilient homes and community centers designed to withstand future seismic events. The project also includes training local builders in disaster-resilient construction techniques, ensuring that communities are better prepared for future challenges.', 'Nepal',
                3, 80000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Cambodian Community Living', 'In the rural provinces of Cambodia, many communities still lack access to secure housing and basic infrastructure. This campaign targets villages in the Kampong Cham region, where Hope Builders will construct sustainable homes, set up clean water facilities, and provide essential sanitation services. The initiative not only focuses on building robust physical structures but also on empowering community members with skills for long-term maintenance and development.', 'Cambodia',
                3, 65000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Bangladesh Resilient Roofs', 'Operating in the flood-prone areas of Bangladeshs Khulna Division, Hope Builders is launching a campaign to build elevated, durable housing that withstands extreme weather conditions. This project will implement innovative design solutions that protect families during monsoon floods, along with community workshops to educate residents on emergency preparedness and sustainable living practices.', 'Bangladesh',
                3, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Vietnam Village Renewal', 'Targeting rural communities in Vietnams Mekong Delta, this campaign focuses on constructing modern, affordable homes capable of withstanding the region''s frequent flooding and climate variations. Hope Builders will collaborate with local authorities to integrate essential health and sanitation services into each housing project, fostering safer and more sustainable living conditions for the villagers.', 'Vietnam',
                3, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Sustainable Roots: Kenya Initiative', 'This campaign targets the fertile Rift Valley region of Kenya, where small-scale farmers face challenges with soil degradation and erratic rainfall. Green Seeds Initiative plans to introduce regenerative agricultural practices and provide eco-friendly agro-equipment and organic fertilizers. The goal is to empower farmers with sustainable techniques that enhance crop yield, improve soil health, and secure long-term food production while preserving the local ecosystem.', 'Kenya',
                4, 50000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Senegal Agro-Future', 'Focused on the Casamance region of Senegal, this initiative aims to revitalize traditional farming practices with modern, sustainable methods that conserve water and enrich depleted soils. Farmers will receive training on organic farming practices, crop rotation, and the use of bio-fertilizers. The campaign seeks to boost agricultural productivity and ensure a reliable, nutritious food supply for local communities while promoting environmental stewardship.', 'Senegal',
                4, 45000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Tanzanian Green Harvest', 'Operating in the Arusha region of Tanzania, this campaign is designed to support local farmers as they transition to sustainable agriculture. Green Seeds Initiative will offer hands-on training in environmentally friendly agricultural practices, distribute high-quality organic seeds, and provide essential modern agro-tools. By combining traditional knowledge with modern sustainable techniques, the project aims to increase crop resilience to climate variability and improve overall food security in the region.', 'Tanzania',
                4, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Mozambique Organic Rise', 'This campaign is centered in Mozambiques Zambezia province, a region where farmers are challenged by soil erosion and unpredictable weather patterns. The initiative will introduce regenerative farming practices, such as intercropping and conservation agriculture, along with training sessions led by agricultural experts. By improving soil fertility and water retention, the project aims to help local farmers achieve a more reliable harvest, boost local economies, and promote environmental sustainability.', 'Mozambique',
                4, 48000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Ethiopian EcoAgro Project', 'Focused on Ethiopias Oromia region, this campaign addresses the urgent need to combat land degradation and improve food production. The project will deploy community workshops on sustainable land management, distribute organic inputs, and demonstrate innovative farming techniques tailored to arid and semi-arid conditions. The initiative aims to create a replicable model for sustainable agriculture in dryland areas, ultimately improving both livelihoods and environmental health.', 'Ethiopia',
                4, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Bangladesh Literacy Lift', 'Focused on rural communities in Bangladeshs Rajshahi Division, this campaign aims to build and renovate schools in under-resourced villages. Education Empowerment will supply modern learning materials, set up computer labs, and train local teachers in digital literacy methods. By enhancing both infrastructure and educational quality, the initiative strives to empower students and provide them with the skills needed for future opportunities.', 'Bangladesh',
                5, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Nepal Digital Bridge', 'Targeting remote areas of Nepals Karnali Province, this campaign is dedicated to bridging the digital divide in education. Education Empowerment plans to install internet-equipped learning centers and conduct training sessions for both teachers and students on modern technology use. The project aims to open up opportunities for remote learning, improve access to global educational resources, and foster a community of lifelong learners in isolated regions.', 'Nepal',
                5, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Indonesia Future Scholars', 'Operating in the rural heartland of Java, Indonesia, this campaign seeks to establish community-driven schools equipped with updated curricula focusing on science, technology, engineering, and mathematics (STEM). Education Empowerment will collaborate with local authorities to offer scholarships and run teacher training workshops. The goal is to nurture a generation of innovative thinkers and provide them with the tools needed to tackle local and national development challenges.', 'Indonesia',
                5, 70000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Cambodian Classroom Revival', 'Focused on the Battambang Province of Cambodia, this campaign targets aging school infrastructure while also modernizing the curriculum. Education Empowerment will renovate existing classrooms, introduce digital learning resources, and train teachers in innovative teaching strategies. This comprehensive approach aims to reignite interest in education, increase school enrollment, and enhance the quality of learning for children in rural areas.', 'Cambodia',
                5, 50000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('India Future Pathways', 'This campaign is tailored for remote areas in Indias Madhya Pradesh region, where access to quality education remains limited. Education Empowerment will build new schools and upgrade outdated facilities with modern classroom technology. The project also includes teacher training programs and community outreach initiatives to boost literacy and ensure that students have equitable access to educational opportunities in this underdeveloped region.', 'India',
                5, 65000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Viviendo Saludable', 'Focused on improving rural healthcare in Perus Cusco region, this campaign aims to construct modular clinics that provide essential medical services. Health Horizons Clinics will equip these centers with modern diagnostic tools and train local healthcare workers to tackle common health challenges. The project focuses on preventive care, maternal health, and vaccination programs in remote Andean communities, ensuring that quality care brings hope and resilience to highland families.', 'Peru',
                6, 70000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Clinic Care of Bahia', 'Set in Brazils vibrant state of Bahia, this initiative targets underserved coastal and hinterland communities. The project involves building sustainable clinics staffed with skilled medical professionals, focusing on reducing disease burdens with preventive medicine and community health education. Funds will be used to develop a network of satellite clinics that can address both acute and chronic conditions, significantly improving access to reliable healthcare services in the region.', 'Brazil',
                6, 65000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Salud y Esperanza', 'Operating in Guatemalas rural Quiché department, this campaign is designed to bring essential healthcare to communities with limited medical access. Health Horizons Clinics will construct primary care facilities, provide emergency services, and run health awareness workshops targeting common diseases. By fostering community partnerships, the project aims to build sustainable healthcare models that empower local residents through improved access to preventative and curative services.', 'Guatemala',
                6, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Nuevo Amanecer Health Centers', 'This campaign targets underserved areas in Colombias Nariño region, where geographical isolation and limited healthcare infrastructure pose serious challenges. By establishing multi-functional health centers equipped with telemedicine capabilities, Health Horizons Clinics seeks to bridge the gap between remote communities and urban medical expertise. The initiative focuses on improving maternal and child health, chronic disease management, and emergency care services to help pave the way for a healthier future.', 'Colombia',
                6, 75000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('San José Vital Clinics', 'Focused on El Salvadors San Salvador Department, this initiative aims to address disparities in local healthcare by constructing new clinics that deliver comprehensive care. The project includes setting up preventive care, nutritional counseling, and rehabilitation services for individuals affected by both communicable and noncommunicable diseases. By investing in state-of-the-art health facilities and educational health programs, San José Vital Clinics intends to foster a community-based approach to overall well-being and resilience.', 'El Salvador',
                6, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Kisumu Night Shield', 'Focused on Kenyas Kisumu County along the shores of Lake Victoria, this campaign aims to provide insecticide-treated bed nets to families living in malaria-prone rural areas. By distributing bed nets and conducting educational workshops on proper usage and maintenance, SafeSleep Initiative hopes to significantly reduce malaria transmission in the region. The project also trains local health workers to ensure sustainability and timely replacement of expired nets.', 'Kenya',
                7, 45000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Accra Bed Net Brigade', 'Targeting communities in Ghanas Greater Accra region, this campaign is dedicated to combating vector-borne illnesses in both urban and peri-urban areas. The funds raised will be used to purchase and distribute high-quality bed nets, with comprehensive community outreach programs designed to raise awareness about malaria prevention. Collaboration with local NGOs and health authorities will ensure that the initiative reaches even the most underserved neighborhoods.', 'Ghana',
                7, 50000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Dar es Salaam DreamSafe', 'Operating in Tanzanias bustling Dar es Salaam region, this campaign addresses the rising risk of mosquito-borne diseases in densely populated urban centers. By distributing insecticide-treated bed nets throughout vulnerable communities, along with targeted education campaigns in schools and community centers, SafeSleep Initiative aims to lower the incidence of malaria. The initiative also includes periodic monitoring to assess the long-term impact of net usage on public health.', 'Tanzania',
                7, 55000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Lagos LifeGuard Net', 'Set in Nigerias Lagos State, where rapid urbanization presents challenges in public health, this campaign focuses on supplying bed nets to families living in informal settlements and areas with limited healthcare access. By partnering with local community leaders, SafeSleep Initiative will distribute bed nets, train volunteers in proper installation and maintenance, and host health fairs to educate residents on combating vector-borne diseases. This comprehensive approach is designed to build a resilient community network focused on prevention.', 'Nigeria',
                7, 60000.0);
        

        INSERT INTO Campaigns (Name, Description, Country, NGO_ID, Funding_Goal)
        VALUES ('Kampala Health Sleeper Campaign', 'Located in the urban and peri-urban areas of Ugandas Kampala District, this campaign seeks to provide insecticide-treated bed nets to communities at high risk for malaria and other vector-borne illnesses. SafeSleep Initiative will facilitate community workshops on net usage and integrate educational sessions into local school curricula. By ensuring that vulnerable households receive reliable protection, this campaign aims to reduce disease transmission and enhance overall community health.', 'Uganda',
                7, 50000.0);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (1, 27);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (1, 14);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (1, 25);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (1, 22);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (1, 16);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (2, 16);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (2, 17);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (2, 5);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (2, 10);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (2, 28);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (3, 2);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (3, 5);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (3, 6);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (4, 22);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (4, 21);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (4, 33);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (5, 28);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (5, 35);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (6, 28);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (6, 25);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (6, 23);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (6, 35);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 35);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 7);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 29);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 15);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 14);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (7, 8);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (8, 19);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (8, 21);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (8, 14);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (9, 20);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (9, 28);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (9, 33);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (9, 13);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 18);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 20);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 2);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 10);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 22);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (10, 11);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (11, 21);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (11, 25);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (11, 20);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (12, 16);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (12, 35);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (12, 24);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (12, 28);
        

        INSERT INTO Subscriptions (DONOR_ID, CAMPAIGN_ID)
        VALUES (12, 3);

-- Sample Donations

INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 25, 44.42, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 17, 79.76, NOW());
 INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 2, 64.54, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 33, 90.62, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 35, 41.73, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (6, 23, 71.26, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (7, 35, 72.18, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (8, 21, 70.21, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (9, 33, 49.1, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (10, 20, 94.25, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (11, 25, 90.1, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (12, 28, 74.31, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 1, 150, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 1, 600, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 1, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (12, 1, 700, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 2, 500, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (11, 2, 800, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 2, 800, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 2, 100, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (8, 2, 100, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 2, 300, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 3, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (9, 3, 200, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 3, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 3, 300, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 4, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 4, 200, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (7, 4, 700, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 4, 200, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 4, 800, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 4, 200, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 5, 100, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (6, 5, 100, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 5, 500, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 5, 200, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 5, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (12, 5, 600, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 6, 500, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 6, 800, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (10, 6, 300, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 7, 400, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (1, 7, 150, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (4, 7, 500, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (5, 7, 600, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (3, 7, 600, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (2, 7, 300, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (12, 2, 7400.31, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (11, 2, 9000.1, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (9, 2, 4900.1, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (8, 2, 16000.15, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (7, 2, 18000.19, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (6, 1, 12000.22, NOW());
INSERT INTO Donations (DONOR_ID, CAMPAIGN_ID, Amount, timestamp) VALUES (7, 3, 5800.50, NOW());