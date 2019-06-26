import java.util.ArrayList;

public class AVLTree <K extends Comparable<K>,V> {


	private class Node {
		public K key;
		public V value;
		public Node left, right;
		public int height ;

		public Node(K key, V value) {
			this.key = key;
			this.value = value;
			left = null;
			right = null;
			height = 1;
		}
	}

	private Node root;
	private int size;

	public int getSize() {
		return size;
	}

	public boolean isEmpty() {
		return size == 0;
	}

	public boolean isBST(){
		ArrayList<K> keys = new ArrayList<>() ;
		inOrder(root,keys);
		for(int i = 1; i < keys.size() ; i ++)
			if (keys.get(i-1).compareTo(keys.get(i)) > 0 )
				return false ;
		return true ;
	}

	private void  inOrder(Node node, ArrayList<K> keys){
		if (node ==  null)
			return;
		inOrder(node.left,keys);
		keys.add(node.key) ;
		inOrder(node.right,keys);

	}

	public  boolean isBalanced(){
		return isBalanced(root) ;
	}

	private boolean isBalanced(Node node){
		if (node == null)
			return true ;
		int balanceFactor = getBalanceFactor(node) ;
		if(Math.abs(balanceFactor) > 1)
			return false ;
		return isBalanced(node.left) && isBalanced(node.right) ;
	}


	private int getHeight(Node node){
		if (node == null )
			return 0 ;
		return node.height ;
	}

	private int getBalanceFactor(Node node){
		if (node == null)
			return  0 ;
		return getHeight(node.left) - getHeight(node.right) ;
	}

	private Node  rightRotate(Node y ){
		Node x  = y.left ;
		Node T3 = x.right ;

		y.height = Math.max(getHeight(y.left),getHeight(y.right)) + 1 ;
		x.height = Math.max(getHeight(x.left),getHeight(x.right)) + 1 ;

		return x ;
	}

	private Node leftRotate(Node y ){
		Node x = y.right ;
		Node T2 = x.left ;

		x.left = y ;
		y.right = T2 ;

		y.height = Math.max(getHeight(y.left),getHeight(y.right)) + 1 ;
		x.height = Math.max(getHeight(x.left),getHeight(x.right)) + 1 ;

		return  x ;

	}

	public void add(K key, V value) {
		root = add(root, key, value);
	}

	private Node add(Node node, K key, V value) {

		if (node == null) {
			size += 1;
			return new Node(key, value);
		}
		if (key.compareTo(node.key) < 0)
			node.left = add(node.left, key, value);
		else if (key.compareTo(node.key) > 0)
			node.right = add(node.right, key, value);
		else
			node.value = value;

		node.height = 1 + Math.max(getHeight(node.left),getHeight(node.right)) ;

		int balanceFactor = getBalanceFactor(node);
		if (Math.abs(balanceFactor) > 1)
			System.out.println("unbalanced  : " + balanceFactor);

		//LL
		if (balanceFactor > 1 && getBalanceFactor(node.left) >= 0 )
			return rightRotate(node) ;


		// RR
		if (balanceFactor < -1  && getBalanceFactor(node.right) <= 0)
			return leftRotate(node) ;

		//LR
		if (balanceFactor > 1 && getBalanceFactor(node.left) < 0) {
			node.left  = leftRotate(node.left) ;
			return rightRotate(node) ;
		}

		//RL
		if (balanceFactor < -1 && getBalanceFactor(node.right) <= 0){
			node.right = rightRotate(node.right) ;
		    return leftRotate(node) ;
		}




		return node;
	}

	private Node getNode(Node node, K key) {
		if (node == null)
			return null;

		if (key.compareTo(node.key) == 0)
			return node;
		if (key.compareTo(node.key) < 0)
			return getNode(node.left, key);
		else
			return getNode(node.right, key);
	}

	public V remove(K key) {
		Node node = getNode(root, key);
		if (node != null) {
			root = remove(root, key);
			return node.value;
		}
		return null;
	}

	private Node remove(Node node, K key) {
		if (node == null)
			return null;

		Node retNode;
		if( key.compareTo(node.key) < 0 ){
			node.left = remove(node.left , key);
			// return node;
			retNode = node;
		}
		else if(key.compareTo(node.key) > 0 ){
			node.right = remove(node.right, key);
			// return node;
			retNode = node;
		}
		else{   // key.compareTo(node.key) == 0

			// 待删除节点左子树为空的情况
			if(node.left == null){
				Node rightNode = node.right;
				node.right = null;
				size --;
				// return rightNode;
				retNode = rightNode;
			}

			// 待删除节点右子树为空的情况
			else if(node.right == null){
				Node leftNode = node.left;
				node.left = null;
				size --;
				// return leftNode;
				retNode = leftNode;
			}

			// 待删除节点左右子树均不为空的情况
			else{
				// 找到比待删除节点大的最小节点, 即待删除节点右子树的最小节点
				// 用这个节点顶替待删除节点的位置
				Node successor = mininum(node.right);
				//successor.right = removeMin(node.right);
				successor.right = remove(node.right, successor.key);
				successor.left = node.left;

				node.left = node.right = null;

				// return successor;
				retNode = successor;
			}
		}

		if(retNode == null)
			return null;

		// 更新height
		retNode.height = 1 + Math.max(getHeight(retNode.left), getHeight(retNode.right));

		// 计算平衡因子
		int balanceFactor = getBalanceFactor(retNode);

		// 平衡维护
		// LL
		if (balanceFactor > 1 && getBalanceFactor(retNode.left) >= 0)
			return rightRotate(retNode);

		// RR
		if (balanceFactor < -1 && getBalanceFactor(retNode.right) <= 0)
			return leftRotate(retNode);

		// LR
		if (balanceFactor > 1 && getBalanceFactor(retNode.left) < 0) {
			retNode.left = leftRotate(retNode.left);
			return rightRotate(retNode);
		}

		// RL
		if (balanceFactor < -1 && getBalanceFactor(retNode.right) > 0) {
			retNode.right = rightRotate(retNode.right);
			return leftRotate(retNode);
		}

		return retNode;
	}



	private Node mininum(Node node) {
		if (node.left == null)
			return node;
		return mininum(node.left);
	}

	public V get(K key) {
		Node node = getNode(root, key);
		return node == null ? null : node.value;
	}

	public void set(K key, V newValue) {
		Node node = getNode(root, key);
		if (node == null)
			throw new IllegalArgumentException(key + "doesn't exist ");
		node.value = newValue;

	}

	public boolean contains(K key) {
		return getNode(root, key) != null;
	}




}