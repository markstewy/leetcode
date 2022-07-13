class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity){}
    
    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1;
        }
        moveToHead(key);
        return cache[head].value;
    }
    
    void put(int key, int value) {
        if (elementCount == 0) {
            head = key;
            tail = key;
            cache[key] = Element(value);
            elementCount++;
            return;
        }
        // map contains key
        if (cache.find(key) != cache.end()) {
            // overwrite value
            cache[key].value = value;
            moveToHead(key);

        } else {
            // map doesn't contain key
            cache[key] = Element(value);
            cache[head].prev = key;
            cache[key].next = head;
            head = key;
            if (elementCount >= capacity) {
                int temp = tail;
                tail = cache[tail].prev;
                cache[tail].next = -1;
                cache.erase(temp);
            } else {
                elementCount++;
            }
        }
        
    }
private:
    struct Element {
        int value;
        int prev = -1;
        int next = -1;
        Element() {};
        Element(int value) : value(value) {};
    };
    
    std::unordered_map<int, Element> cache{};
    int capacity;
    int elementCount = 0;
    int head;
    int tail;

    void moveToHead(int key) {
        if (key == head) {
            return;
        }
        if (key == tail) {
            tail = cache[key].prev;
            cache[tail].next = -1;
        }

        int p = cache[key].prev;
        int n = cache[key].next;
        if (p != -1) { cache[p].next = n; }
        if (n != -1) { cache[n].prev = p; }

        cache[head].prev = key;
        cache[key].next = head;
        cache[key].prev = -1;
        head = key;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */