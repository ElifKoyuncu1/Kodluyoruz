# Noktaları tanımla
points = [(0, 0), (3, 4), (5, 12), (8, 15)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# Mesafeleri hesapla
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = euclideanDistance(points[i], points[j])
        distances.append(d)

# Minimum mesafeyi bul
min_distance = min(distances)

# Sonucu yazdır
print("Minimum mesafe:", min_distance)
